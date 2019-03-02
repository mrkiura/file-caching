"""Helper library to cache a file."""
from pymemcache.client.base import Client
import configparser
import os


class FileCacher:
    MEMCACHE_CONFIG = configparser.ConfigParser()
    MEMCACHE_CONFIG.read('config.ini')
    FILE_SIZE_LIMIT = 524238800
    CHUNK_SIZE = 1000000

    def __init__(self):
        server_address = self.MEMCACHE_CONFIG['DEFAULT']['server_address']
        port = int(self.MEMCACHE_CONFIG['DEFAULT']['port'])
        self.memcache_client = Client((server_address, port))
        self.cache_keys = {}
        
    def store(self, name, infile):
        """
        Store a file to memcache

        :param file_path: Path to the file being stored
        :return: A tuple with a list of keys and a success flag
        """
        if self._check_file_size(infile) > self.FILE_SIZE_LIMIT:
            raise ValueError('File size exceeds the 50 mb limit')
        self.cache_keys[name], statuses = [], []
        with open(infile, 'rb') as file:
            if file:
                for chunk_index, file_chunk in enumerate(iter(lambda: file.read(self.CHUNK_SIZE), b'')):
                    key = f'{name}_chunk{chunk_index}'
                    status = self.memcache_client.set(key, file_chunk)
                    self.cache_keys[name].append(key)
                    statuses.append(status)
        return all(statuses)

    def retrieve(self, name, outfile):
        """
        Retrieve a file from memcache given a name.
        """
        cache_keys = self.cache_keys.get(name)
        file_chunks = self.memcache_client.get_many(cache_keys)
        file_contents = b''.join(file_chunks.values())
        with open(outfile, 'wb') as file:
            file.write(file_contents)
            return file

    def _check_file_size(self, file_path):
        return os.path.getsize(file_path)
