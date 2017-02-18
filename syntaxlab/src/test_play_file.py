# coding: UTF-8
import unittest
import play_file


class TestAssemblyReader(unittest.TestCase):
    def test_version_reader(self):
        assembly_reader = play_file.AssemblyReader()
        version = assembly_reader.get_assembly_version('AssemblyInfo.cs')
        self.assertEqual(version, '7.3.1.0210')
