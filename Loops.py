# Loops

my_list = ["hello", "what's", "up"]

for word in my_list:
    print(word)

# for letter in "abcdeghijklmnopqrstuvwxyz":
    # print(letter)



for num in [1, 2, 3, 4 , 5]:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")



print("hello")

number = 10

while number:
    number -= 1
    print(number)


names = ["gary", "ross", "damn", "luke"]

for name in names:
    if name == "damn":
        continue
    print(name)

# Challenge

hellos = [
    "Hello",
    "Tungjatjeta",
    "Grüßgott",
    "Вiтаю",
    "dobrý den",
    "hyvää päivää",
    "你好",
    "早上好"
]

for hello in hellos:
    print(hello + " World")