student_List =  ["Ali", "Veli", "Paron"]
student_List.append("Turgay")
print(student_List)
student_List.remove(student_List[0])
print(student_List)

#we can use list some EC2 machines or etc..


if student_List[0]=="Ali":
    print(" Ata bak")
else:
    print("First Element : " , student_List[0] )

new_List = student_List[1:4]
print(new_List)