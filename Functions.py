# Functions

def hows_the_parrot():
    print("hello world!")


hows_the_parrot()


def lumberjack(name, pronoun):
    if name.lower() == "gary":
        print("{} is a lumberjack and {} is OK!".format(name, pronoun))
    else:
        print("Not gary")


lumberjack("gary", "he's")


def average(num1, num2):
    return (num1 + num2) / 2


avg = average(25, 5)

print(avg)
