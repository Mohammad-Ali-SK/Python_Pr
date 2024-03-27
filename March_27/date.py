# Know about this data from CODE With Harry--------****
# import time
# # print(time.time())


# def lim(func):
#     def wrapper(*args,**kwargs):
#         start = time .time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f'{func.__name__} ran in {start - end}')
#         return result
#     return wrapper

# @lim
# def my_io():
#     time.sleep(2)
#     print('Hello Mohammad')
    
# my_io()
import time

t = time.localtime()

# formatted_time = time.strftime("Date_ %d-%m-%Y  Time_ %H:%M:%S %p" , t)
# formatted_time = time.strftime("%Y")

# print(formatted_time)

# import datetime

# x  = datetime.datetime.now()
# year = x.strftime("%B")
# print(year)