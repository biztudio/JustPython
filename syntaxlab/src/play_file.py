# coding: UTF-8
import string
import os


class AssemblyReader:
    def __init__(self, assembly_file):
        self.file = assembly_file

# @staticmethod
    def check_existence(self, file_location):
        return os.path.isfile(file_location)

    def get_assembly_version(self):
        if self.check_existence(self.file):
            with open(self.file, 'r') as file:
                [print(line.strip(string.punctuation)) for line in file.readlines()]

                return ''
        else:
            print(self.file + ' can not be located')
            return ''


assembly_reader = AssemblyReader('AssemblyInfo.cs')
print(assembly_reader.check_existence('AssemblyInfo.cs'))
version = assembly_reader.get_assembly_version()
print(version)