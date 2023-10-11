# декораторы 

# def my_decorator(func):
#     def wrapper():
#         print("То что выходит до функции")
#         func()
#         print("То что выходит после функции")
#     return wrapper

# @my_decorator
# def hello():
#     print ('Hello world')


# hello()

# def my_decorator(func):
#     def wrapper():
#         print("То что выходит до функции")
#         print(func())
#         b = func()
#         print(b + 10)
#     return wrapper

# @my_decorator
# def hello():
#     h = 5 + 5 
#     return h


# hello()


# def repeat(num):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(num):
#                 func(*args,**kwargs)
#         return wrapper
#     return decorator

# @repeat(13)
# def say_hallo():
#     print('hallo')

# say_hallo()


def auth_decor(func):
    def wrapper(username,passwors,*args,**kwargs):
        if username== 'admin' and passwors == 'secret':
            resilt = func(*args,**kwargs)
        else:
            resilt = 'Error'

        return resilt
    return wrapper


@auth_decor
def my_func():
    return 'доступ разрешен'


print(my_func('admin','secret'))