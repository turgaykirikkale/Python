import sys

type = sys.argv[1]

if type== "t2.micro":
    print("i will create t2.micro")
elif type=="t2.medium":
    print("i will create t2.medium")
else:
    print("i will not creatae t2.micro")