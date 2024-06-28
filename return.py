# def hello():
#     return "Hi!"

# print(hello())


def validate():
    if(s_user==user and s_pass==passw):
        return True
    else:
        return False

s_user="admin"
s_pass="admin"

user=input()
passw=input()


print(validate())
