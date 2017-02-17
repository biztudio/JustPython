# coding: UTF-8
import os


class AssemblyReader:
    def __init__(self, assembly_file):
        self.file = assembly_file
        self.assembly_version = ''

    def get_assembly_version(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r', encoding='utf8') as file:  # 加上encoding='utf8'才能确保读取文件时正确处理版本字符 ©
                # for line in file.readlines():
                for line in file:  # 相较于readlines, 迭代占用更小的内存，而且更加智能（依赖于Python文件对象的实现），所需文件内容是自动从buffer中按照需要读取
                    # 此处不用.index 是因为有的行没有包含 [assembly:AssemblyVersion( 时，程序直接抛substring not found 的异常，而用 .find 则返回 -1，在能找到的情况下效果则类似
                    find_flag = line.strip().replace(' ', '').find('[assembly:AssemblyVersion(')
                    if find_flag >= 0 > line.strip().find('//'):  # 过滤单行注释文本, 本行布尔判断的写法很好玩
                        self.assembly_version = line.split('"')[1]
        return self.assembly_version


assembly_reader = AssemblyReader('AssemblyInfo.cs')
version = assembly_reader.get_assembly_version()
print(version)

'''本方法有个缺陷，即对于多行注释中的文本无法过滤
   形如：
   /*
    [assembly: AssemblyVersion("1.0.*")]
   */
'''
