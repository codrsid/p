import urllib.request
x= input("enter the name you want to give to the image")
y=input("enter the entension of the image(file type)")
u= input("enter the url of the image")
name = x + "." + y
urllib.request.urlretrieve(u,name)