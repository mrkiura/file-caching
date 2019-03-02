import unittest

from file_cacher import FileCacher


class FileCacherTestCase(unittest.TestCase):
    def setUp(self):
        self.very_large_file = 'test_large_file'
        self.large_file = 'test_snall_file'
        self.file_cacher_client = FileCacher()

    def test_does_not_accept_file_larger_than_50mb(self):
        with self.assertRaises(ValueError):
            self.file_cacher_client.store(self.very_large_file)

    def test_storing_a_large_file(self):
        self.assertTrue(self.file_cacher_client.store(self.large_file)[1])

    def test_retrieving

if __name__ == '__main__':
    unittest.main()