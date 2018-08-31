#Question 1
import datetime as dt
print(dt.date.today())

#Question 2
import webbrowser
b=input("search anything")
webbrowser.open_new_tab('http://google.com/search?q=%s'%b)

#Question 3
import os
path='C:/Users/10/PycharmProjects/untitled/New folder'
files=os.listdir(path)
i=1
for file in files:
    a=input("enter name of file")
    os.rename(os.path.join(path,file),os.path.join(path, a+'.jpg'))
    i=i+1