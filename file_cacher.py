"""Helper library to cache a file."""
from pymemcache.client.base import Client
import configparser
import os


class FileCacher:
    MEMCACHE_CONFIG = configparser.ConfigParser()
    MEMCACHE_CONFIG.read('config.ini')
    FILE_SIZE_LIMIT = 524238800
    CHUNK_SIZE = 1048576

    def __init__(self):
        server_address = self.MEMCACHE_CONFIG['DEFAULT']['server_address']
        port = self.MEMCACHE_CONFIG['DEFAULT']['port']
        self.memcache_client = Client((server_address, port))
        
    def store(self, file_path):
        """
        Store a file to memcache

        :param file_path: Path to the file being stored
        :return: A tuple with a list of keys and a success flag
        """
        if self._check_file_size(file_path) > self.FILE_SIZE_LIMIT:
            raise ValueError('File size exceeds the 50 mb limit')
        keys, statuses = [], []
        with open(file_path, 'rb') as file:
            if file:
                for chunk_index, file_chunk in enumerate(iter(lambda: file.read(self.CHUNK_SIZE), b'')):
                    key = file_path + chunk_index
                    status = self.memcache_client.set(key, file_chunk)
                    keys.append(key)
                    statuses.append(status)
        return keys, all(statuses)

    def retrieve(self, filename, cache_keys):
        """
        Retrieve a file from memcache.
        """
        pass

    def _check_file_size(self, file_path):
        return os.path.getsize(file_path)

    def _store_to_memcache(self):
        pass

    def _retrieve_from_memcache(self):
        pass