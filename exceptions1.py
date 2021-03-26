import sys
x = int(input("x: "))
y = int(input("y: "))
try:
    result=x/y
except ZeroDivisionError:
    print("Error: Cannot divided by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result} ")
