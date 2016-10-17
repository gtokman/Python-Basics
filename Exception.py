# Try

try:
    count = int(input("Give me a number: "))

except ValueError:
    print("That's not a number!")

else:
    print("Hi \n" * count)

def add(num1, num2):
    try:
        float(num1) + float(num2)
    except:
        return None
    else:
        return num1 + num2


add(1, 2)