# try:
#     result = 2/0
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     result = 1

# print(result)

class CustomError(Exception):
    print("err")
    pass

try:
    raise CustomError()
except Exception as error:
    print("custom error")