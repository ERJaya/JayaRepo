name=str(input("Enter your Name :"))
a=int(input("Enter your age :"))
if a>=18:
    print(f"Hello {name} you are Eligible for voter")
elif a<18 and a>0:
    print(f"Sorry {name} you are not Eligible for Voter")
else:
    print("Please provide valid information")