#Calculator Program
is_running = True

while is_running != False: 
	print("------Calculator program------")
	num1 = float(input("Enter 1st number: "))
	num2 = float(input("Enter 2nd number: "))
	operator = str(input("What are you going to do ( + , / , * , - ):  "))
	if operator == "+":
		answer = num1 + num2
		print(f"answer is: {answer}")
	elif operator == "-":
		answer = num1 - num2
		print(f"answer is: {answer}")

	elif operator == "/":
		answer = num1 / num2
		print(f"answer is: {answer}")

	elif operator == "*":
		answer = num1 * num2
		print(f"answer is: {answer}")

	else :
	    print(f"This is not a valid operator: {operator}")
	
	command = str(input("press q to quit:  "))
	if command.lower() == "q":
		break
	else :
	   print(f" command {command}: not found")
	   continue

