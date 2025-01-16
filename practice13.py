# #How to list the all files of directory in python
#
# from os import listdir
# from os.path import isfile,join
#
# files_list =[f for f in listdir('/home') if isfile(join('/home',f))]

# import sys #check the version of python
#
# print('Python version : ',sys.version_info)
# import datetime
# now = datetime.datetime.now()
# print("Date and Time is : ")
# print(now.strftime("%y-%m-%d %H-%M:%S"))
from math import pi

r = float(input("What is the radius of the Cirle ? "))
print(type(r))
area = pi * (r)**2
print("Area is : ",float(area))