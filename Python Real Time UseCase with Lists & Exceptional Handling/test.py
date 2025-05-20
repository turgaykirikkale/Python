#Read İnput from the USER
#For Loop for every folder
#Identify the Modules
#print files
#handle any known errors
import os

folders  = input("Please provide list of folder names with spaces in between: ").split()

#now we will write for Loop

for folder in folders:
   
   try:
        files = os.listdir(folder)
   except FileNotFoundError:
        print("provide valid folder name, looks like this folder is not exist")
        break
   except PermissionError:
        print("Permission Error please enter good credential")
        break
   for file in files:
      print(file)

#Identify the modules OS modules it talks with the Operating systems within OS modules there is function called os.listdir
#thats a function we are going to use when you do this it will print all the files in that particular directory

#you need to handle if there is error with python.

