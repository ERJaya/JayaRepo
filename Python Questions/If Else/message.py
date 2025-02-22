gender=str(input("Please Enter your gender M or F: ")).lower()
#here .lower() converts all the input to lower case. you can enter M also.
if gender=='m':
    print("Good morning Sir!")
elif gender=='f':
    print("Good morning Madam!")
else:
    print("Wrong Input!")