n=int(input("Enter the number of entries:"))
student={}
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value")
    student[key]=value
print(student)