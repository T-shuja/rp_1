import requests

url=input("Enter url : ")

url_= "https://"+url

try: 

	x=requests.get(url_)

	print(x.text)

except:

	print("Some error occured")
