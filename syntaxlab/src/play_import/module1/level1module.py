from module2.level2module1 import greetings_leve2module1

def greetings_leve1module():
    print('This is from leve1module @' + __name__)
    greetings_leve2module1()    

if __name__=='__main__':
    greetings_leve1module()      