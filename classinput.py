class person:
    name=""
    age=0
print("createing a new person")
P1=person()
P1.name=input("enter your name")
P1.age=int(input("enter your age"))
print("displaying properties of the person")
print("name of the person=")
print(P1.name)
print("age of the person=")
print(P1.age)
