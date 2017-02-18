# coding: UTF-8
import unittest
import play_file


class TestAssemblyReader(unittest.TestCase):
    def test_version_reader(self):
        assembly_reader = play_file.AssemblyReader()
        version = assembly_reader.get_assembly_version('AssemblyInfo.cs')
        self.assertEqual(version, '7.3.1.0210')

    def test_version_writer(self):
        new_version = '7.3.1.0228'
        assembly_writer = play_file.AssemblyWriter()
        version = assembly_writer.update_assembly_version('AssemblyInfo.cs', new_version)
        self.assertEqual(version, new_version)



