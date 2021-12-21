import os
import unittest
from unittest.mock import mock_open, patch

class FileOperations:

    def readFile(self, file):
        with open(file, 'r') as f:
            data = f.read()
        return data

    def writeFile(self, file, data):
        with open(file, 'w') as f:
            f.write(data)
        return True

    def deleteFile(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            raise Exception("File not found")

    
class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.temp = FileOperations()

    def test_file_operations_read(self):
        with patch("builtins.open", mock_open(read_data="data")) as mockFile:
            self.assertEqual(self.temp.readFile('some/file/path/file.txt'), "data")
            mockFile.assert_called_with('some/file/path/file.txt', "r")

    def test_file_operations_write(self):
        with patch("builtins.open", mock_open(read_data="data")) as mockFile:
            self.temp.writeFile('some/file/path/file.txt', "newData")
            mockFile.assert_called_with('some/file/path/file.txt', 'w') 
    
    @patch('os.path.exists')
    @patch('os.remove')
    def test_file_operations_remove_file_that_exists(self, mock_exsists, mock_remove):
        mock_exsists.return_value = True
        self.temp.deleteFile('some/file/path/file.txt')
        mock_remove.assert_called_with('some/file/path/file.txt')

    @patch('os.path.exists')
    def test_file_operations_remove_file_that_dont_exists(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(Exception):
            self.temp.deleteFile('some/file/path/file.txt')

    def tearDown(self):
        self.temp = None
    