import sys
import random

print('Please enter a card number')
number = input()



# Check that input is only numbers
try:
   val = int(number)
   print("The card number you entered is : ", val)
except ValueError:
  try:
    val = float(number)
    print("You can't have decimals as your card number")
    sys.exit()
  except ValueError:
      print("Input must be numbers")
      sys.exit()

def CheckCardValid(number):
    lastNumber = number[-1:] # Get last number of credit card
    lastNumber = int(lastNumber) # Set it as an integer value
    number = number[:-1] # Drop final number
    number = number[::-1] # Reverse Number
    numberVal= [int(a) for a in str(number)] # Put number into list
    numberVal[::2] = [x*2 for x in numberVal[::2]] # Double every second number
    for i in range(len(numberVal)): # Checks if a number is greater than 9. If it is, subtract by 9
      if numberVal[i] > 9:
         numberVal[i] -= 9
    total = sum(numberVal) # Find the total sum of all numbers in the list
    checksum = total % 10 # Mod by 10 and get remainder
    checksum = abs(checksum - 10) # Subtract 10 and get the abs value
    if checksum == 10: # fix bug
        checksum = 0;

    if (lastNumber == checksum): # Compare remainder with last number
        print("This is a valid number")
    else:
        print("This is NOT a valid number. Last digit should be", checksum)

        checksum = str(checksum)
        return checksum

    #print("number value: ",numberVal)
    #print("total: ",total)
    #print("lastnumber: ",lastNumber)
    #print("Checksum: ",checksum)


def CheckVendor():
    vendor = number[0:4] # Get first 4 numbers of card

    if 2221 <= int(vendor) <= 2720:
        print("That's a Mastercard")
    elif 3000 <= int(vendor) <= 3050:
        print("That's a Diners Club")
    elif 3400 <= int(vendor) <= 3499:
        print("That's an American Express")
    elif 3528 <= int(vendor) <= 3589:
        print("That's a JCB")
    elif 3700 <= int(vendor) <= 3799:
        print("That's an American Express")
    elif 4000 <= int(vendor) <= 4999:
        print("That's a Visa")
    elif 5600 <= int(vendor) <= 6900:
        print("That's a Maestro")
    elif int(vendor) == 6011:
        print("That's a Discover Card")
    else:
        print("This card does not have a vendor")

CheckCardValid(number)
CheckVendor()

print("Press Enter to continue")
a = input()

print('Select a vendor') # Select Vendor
print('1 = Visa')
print('2 = Maestro')
print('3 = American Express')
print('4 = Diners Club')
vendorSelection = input()
vendorSelection = int(vendorSelection)
cardNumber = 0
min = 0 # Randomly Assigned min value
max = 0 # Randomly Assigned max value
if vendorSelection == 1: # Visa
    min = 4000
    max = 4999
elif vendorSelection == 2: # Maestro
    min = 5600
    max = 6900
elif vendorSelection == 3: # American Express
    min = 3700
    max = 3799
elif vendorSelection == 4: # Diners Club
    min = 3000
    max = 3050
else:
    print("That's not a choice ")


cardNumber = random.randint(min,max) # Assign Random vendor ID
otherCardNumber = random.randint(100000000000,999999999999) # Assign random remaining numbers
fullCardNumber = int(str(cardNumber) + str(otherCardNumber)) # Frankenstein them two together into one
fullCardNumber = str(fullCardNumber) # Make them a string
print("Randomly Generated Card Number: ",fullCardNumber)
aaaaahhhhh = CheckCardValid(fullCardNumber) # Check the valid checksum of the generated card numbers
print("aaaahhhh",aaaaahhhhh)
fullCardNumber = fullCardNumber[:-1] # Drop last number
aaaaahhhhh = str(aaaaahhhhh) # Convert the checksum to a string
veryFullCardNumber = str(fullCardNumber) + str(aaaaahhhhh) # Frankenstein them two together into one yet again to make a valid card

print("--------------------------------------------------")
CheckCardValid(veryFullCardNumber) # Check the newly created number to see if it is valid (which it will be)
print("Your New Card Number Is: ",veryFullCardNumber)
print("--------------------------------------------------")

print("Press Enter to continue")
b = input()

print("Enter 12 Digits and I'll give you the last 4 numbers")

val2 = input()
print("The card number you entered is : ", val2)
val3 = random.randint(1000,9999)
full16 = int(str(val2) + str(val3)) # Frankenstein them two together into one
full16 = str(full16) # Make them a string
ooooooohhhhh = CheckCardValid(full16) # Check the valid checksum of the generated card numbers
full16 = full16[:-1] # Drop last number
ooooooohhhhh = str(ooooooohhhhh) # Convert the checksum to a string
veryFull16 = str(full16) + str(ooooooohhhhh) # Frankenstein them two together into one last time to make a valid card

print("--------------------------------------------------")
CheckCardValid(veryFull16) # Check the newly created number to see if it is valid (which it will be)
print("Your New Card Number Is: ",veryFull16)
print("--------------------------------------------------")
