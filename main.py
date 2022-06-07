import re
while True:
  input_code = input("Enter your country code : ")
  valid_code = False
  if (len(input_code)<2 or len(input_code)>3):
    print("Not valid ! Total digits should be betwwen 2-3 in country code")
    continue
  elif not re.search("[+]",input_code):
    print("Not valid ! [+] should exist in phone number")
    continue
  elif not re.search("[0-9]",input_code):
    print("Not valid ! Should contain only digits between [0-9]")
    continue
  else:
    valid_code = True
    break
if(valid_code==True):
 
    num = input("Please enter a 10 digit mobile number: ")
if len(num) > 10 or len(num) < 10:
    print("Number is not valid (Enter a 10 digit number)")
else:
    if num[0] == '6' or num[0] == '7' or num[0] == '8' or num[0] == '9':
        try:
            num = int(num)
            print("Your number is valid")
        except:
            print('Number is not valid (A number should not contain any characters)')
    else:
        print("Number is not valid (A number should start with 7 or 8 or 9)")

