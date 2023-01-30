class student:
    name=""
    clas=0
    marks=0
print("input detail of student")
print("Enter name of student")
s1=student()
s1.name=input("Enter the student name")
print("Enter the class of",s1.name)
s1.clas=int(input())
print("class of ",s1.name,"is",s1.clas)
print("Enter marks of ",s1.name)
s1.marks=int(input())
if s1.marks>=33:
    print(s1.name,"pass")
else:
    print(s1.name,"fail")
