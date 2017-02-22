# coding: UTF-8
import os
import fileinput
import re


class TextReplacer:
    def __init__(self):
        self.file = ''

    def replace_text_in_file(self, file_location = '', text_current = '', text_new = ''):
       self.file = file_location
       print('Plan to change ' ,text_current, ' to ',text_new)
       if os.path.isfile(self.file):
           for line in fileinput.input(self.file, inplace=True):
                if re.search(text_current, line):                    
                    line = line.replace(text_current, text_new)
                print(line.replace('\n',''))     


class AssemblyReader:
    def __init__(self):
        self.file = ''
        self.prefix_tag = 'assembly:AssemblyVersion'
        self.assembly_version = ''

    def get_assembly_version(self, assembly_file):
        self.file = assembly_file
        if os.path.isfile(self.file):
            with open(self.file, 'r', encoding='utf8') as file:  # 加上encoding='utf8'才能确保读取文件时正确处理版本字符 ©
                self.assembly_version = [line for line in file if line.strip().replace(' ', '').find(self.prefix_tag) >= 0 > line.strip().find('//')][0].split('"')[1]
        return self.assembly_version


class AssemblyWriter(AssemblyReader):
    def update_assembly_version(self, assembly_file, new_version):
        current_version = self.get_assembly_version(assembly_file)
        if len(current_version) > 0:
            for line in fileinput.input(self.file, inplace=True):
                if re.search(current_version, line):
                    line = line.replace(current_version, new_version)
                print(line.replace('\n',''))
            self.assembly_version = new_version
        return self.assembly_version

'''本方法有个缺陷，即对于多行注释中的文本无法过滤
   形如：
   /*
    [assembly: AssemblyVersion("1.0.*")]
   */
'''


           