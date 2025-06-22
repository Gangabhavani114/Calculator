a = int(input("enter first number: "))
sign = input("enter sign: ")
b = int(input("enter second number: "))
if(sign == '+'):
     print("total: "+str(a+b))
elif(sign == '-'):
     print("total: "+str(a-b))
elif(sign == '*'):
    print("total: "+str(a*b))
elif(sign == '/'):
    print("total: "+str(a/b))
else:
    print("check again")