# coding: UTF-8
import os


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


'''本方法有个缺陷，即对于多行注释中的文本无法过滤
   形如：
   /*
    [assembly: AssemblyVersion("1.0.*")]
   */
'''
