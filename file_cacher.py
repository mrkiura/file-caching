"""Helper library to cache a file."""
from pymemcache.client.base import Client
import configparser


class FileCacher:
    MEMCACHE_CONFIG = configparser.ConfigParser()
    MEMCACHE_CONFIG.read('config.ini')
    def __init__(self):
        server_address = self.MEMCACHE_CONFIG['DEFAULT']['server_address']
        port = self.MEMCACHE_CONFIG['DEFAULT']['port']
        self.client = Client((server_address, port))
        
    def store(self, file_path):
        pass

    def retrieve(self, filename):
        pass

    def _store_to_memcache(self):
        pass

    def _retrieve_from_memcache(self):
        pass