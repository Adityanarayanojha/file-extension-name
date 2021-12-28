fn= input("Enter Filename: ")

f = fn.split(".")
a= f[-1]
print ("Extension of the file is : " + a)
if (a=="py"):
    {
        print("python")
    }
else:
    print("wrong Input")
