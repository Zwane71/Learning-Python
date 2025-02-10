print('**** Comparison program (Odd or Even number) ****')
num1 = int(input('Enter your number: '))


if num1 % 2 == 0 and num1 > 0:
    print(f"{num1} is a positve even number") 
elif num1 % 2 == 1 and num1 < 0:
    print(f"{num1} is a negative odd number")
elif num1 == 0:
    print(f"{num1} is not divisible")
else:
    print("number entered is invalid")