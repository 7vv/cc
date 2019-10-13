import requests
print("          {+}Extract the Coockie{+}\n          {+}BY:941k{+}")
CoockieExtract = input("[1]Instagram \n[2]Twitter \n[3]FaceBook \n[4]Other \n   Enter Number : ")
if CoockieExtract == "1":
    session = requests.Session()
    print(session.cookies.get_dict())
    response = session.post("https://www.instagram.com/")
    print(response.cookies.get_dict())
if CoockieExtract == "2":
    session = requests.Session()
    print(session.cookies.get_dict())
    response = session.post("https://twitter.com")
    print(response.cookies.get_dict())
if CoockieExtract == "3":
    session = requests.Session()
    print(session.cookies.get_dict())
    response = session.post("https://www.facebook.com/")
    print(response.cookies.get_dict())
if CoockieExtract == "4":
    other = input("Enter Web Sit : ")
    session = requests.Session()
    print(session.cookies.get_dict())
    response = session.post(other)
    print(response.cookies.get_dict())
