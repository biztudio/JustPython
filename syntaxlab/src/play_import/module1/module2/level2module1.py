from level2module2 import greetings_leve2module2

def greetings_leve2module1():
    print('This is from level2module1 @' + __name__)
    greetings_leve2module2()    

if __name__=='__main__':
    greetings_leve2module1()        