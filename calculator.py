from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

try:
	num1 = int(input("please enter the first number (0 to 1000): "))

	if num1 > 1000 or num1 < 0:
		raise Exception("num1 too large (or small)")

	operation = input("please enter the operation (+ - * /): ")

	if operation not in ["+", "-", "*", "/"]:
		raise Exception("invalid operator")

	num2 = int(input("please enter the second number (0 to 1000): "))

	if num2 > 1000 or num2 < 0:
		raise Exception("num2 too large (or small)")
		
except Exception as err:
	print("you messed up >_< (", err, ")")
	exit(1)

if operation == "*":
	multiply(num1, num2)
elif operation == "/":
	divide(num1, num2)
elif operation == "+":
	add(num1, num2)
elif operation == "-":
	subtract(num1, num2)
