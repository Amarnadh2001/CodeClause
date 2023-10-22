#importing the pyshorteners library.....
import pyshorteners
#Enter the input URL... you want to short
url=input("Enter the URL you need to short : ")
shortener=pyshorteners.Shortener()
shortened_url=shortener.tinyurl.short(url)
print("Shortened URL : ",shortened_url)