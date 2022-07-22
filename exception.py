# try, except,else,raise,finally

# def concat():
#     try:
#         print(10+"abc")
#     except BaseException as b:
#         print("Unable to concatenate integer and string")
#     finally:
#         print("abc")

# concat()


def A():
    try:
        a=10
        c=a/0
        print(c)
    except ZeroDivisionError:
        print("Error")
    else:
        print(a)
A()



