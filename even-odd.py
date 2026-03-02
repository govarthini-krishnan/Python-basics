c=int(input("enter the value of c"))
if c>=0 and c%2==0:
    print("c is a positive even number")
elif c<0 and c%2==0:
    print("c is a negative even number")
elif c>0 and c%2!=0:
    print("c is a positive odd number")
else: 
    print("c is a negative odd number "
