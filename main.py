num = input("Please enter a 10 digit mobile number: ")

# Check if number length is greater or less then 10
if len(num) > 10 or len(num) < 10:
    print("Number is not valid (Enter a 10 digit number)")
else:
    # Check if first number is 7 or 8 or 9
    if num[0] == '7' or num[0] == '8' or num[0] == '9':
        try:
            num = int(num)
            print("Your number is valid")
        except:
            print('Number is not valid (A number should not contain any characters)')
    else:
        print("Number is not valid (A number should start with 7 or 8 or 9)")
