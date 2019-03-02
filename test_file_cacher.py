import unittest

from file_cacher import FileCacher


class FileCacherTestCase(unittest.TestCase):
    def setUp(self):
        self.large_file = None
        self.normal_file = None
        self.file_cacher_client = FileCacher()

    def test_does_not_accept_file_larger_than_50mb(self):
        with self.assertRaises(ValueError):
            self.file_cacher_client.store(self.large_file)

if __name__ == '__main__':
    unittest.main()