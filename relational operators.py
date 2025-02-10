is_running = True

while is_running != False:
    num1 = int(input('Enter your 1st number: '))
    num2 = int(input('Enter your 2st number: '))

    if num1 == num2:
        print(f"{num1} and {num2} are equal")
        break
    elif num1 != num2:
            print(f"{num1} and {num2} are not equal")
            if  num1 > num2:
                    print(f"{num1} is greater than {num2}")
                    break
            elif num1 < num2:
                 print(f"{num1} is less than {num2}")
                 break
            elif num1 >= num2:
                    print(f"{num1} might be greater or equals to {num2}")
                    break
            elif num1 <= num2 :
                    print(f"{num1} is less or equal to {num2}")
                    break

    
    else:
        print("you didn't enter the intergers (e.g: 1,2,3)")
        break
    
    