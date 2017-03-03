from module1.level1module import greetings_leve1module

def greetings_user_interface():
    print('This is from user_interface @' + __name__)
    greetings_leve1module()    

if __name__=='__main__':
    greetings_user_interface()      