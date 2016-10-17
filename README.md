
# Lists

* You can create a list with the list() function or using two square brackets ([]).

* You can use the plus sign to add items into a list so long you add

*  two lists together (e.g. [1, 2, 3] + [4, 5] would create [1, 2, 3, 4, 5]. [1, 2, 3] + 4 would create a TypeError). You can multiply a list by an integer and get back the content of the list as many times as the value of the integer (e.g. [1, 2] * 2 would produce [1, 2, 1, 2]).

* You can use the .append() method to add a single item to the end of a list.

* You can use the .extend() method to add every item from one list to another list.

* You can use the .remove()method to remove a particular value from a list.


# Index

* Indexes count up from 0 when you start on the lefthand side. In the string "hello", the "h" is at index 0, the "e" is at 1, the first "l" is at 2, and so on.

* Indexes count down from -1 if you start on the righthand side. Using the string "hello", we could get the "o" at the index -1, the second "l" at -2, etc.

* Both strings and lists have a .index() method that will give you the index for a particular value. Using our old friend "hello", if we wanted to find the index for the "e", we could do "hello".index("e").

.index() only gives the index for the first occurrence of whatever you searched for.

# Bools

* The bool() function will tell you whether something (a variable, a comparison (next video!), or anything else) evaluates to true or false. You won't find this used a lot in every day Python programming but it's super-handy for testing your assumptions when you're still learning.

# Operators

* Python has seven comparators, or comparison operators. Each of them returns True or False. Here they are:

Operator	Comparison
==	A is equal to B
!=	A is not equal to B
<	A is less than B
>	A is greater than B
<=	A is less than, or equal to, B
>=	A is greater than, or equal to, B
is	A has the same memory address as B

# In

* in returns whether or not a value is inside of a container. We can use this to see if, for example, a smaller string is in a bigger string or if a certain item is in a list.

Examples

"java" in "javascript" would give back True

5 in [3, 4, 1] would give back False

# Loops

Python has two loop types, for and while.

for loops run a certain number of times and then end themselves. while loops, on the other hand, run until their condition, like an if has, turns False. If it helps, you can think of while loops as repetitious ifs.

For loop

```
numbers = [1, 2, 3, 4]
doubles = []
for number in numbers:
    doubles.append(number*2)
```

This loop will run four times because there are four items in the numbers list. On each iteration of the loop, we're calling the value at the current index number.

While loop

```
start = 99
while start:
    print("{} bottles of milk on the wall, {} bottles of milk.".format(start))
    print("Take one down and pour it on some cereal.")
    start -= 1
    print("{} bottles of milk on the wall.".format(start))
```

This while loop will print out something like the traditional "99 bottles" song many of us used to annoy our parents on road trips. The loop stops when start becomes something False, which will happen when it's reduced to 0.

break

You can stop a loop early by using the keyword break.

```
for letter in "abcdef":
    if letter == "c":
        break
    print(letter)

```

This loop will print "a" and "b" and then stop because of the break when letter is "c".

break can only be used inside of a loop.


continue
```
for letter in "abcdef":
    if letter == "c":
        continue
    print(letter)
```

Nearly the same loop but this one will print "a", "b", "d", "e", and "f". It skips "c" because of the continue, which causes the loop to immediately move on to the next step in the loop.

Like break, continue can only be used inside of a loop.

else

And, finally, we have the else: block for both loops. If the loop ends naturally, meaning it doesn't have a break triggered and no exceptions happen, the loop's else block will happen, if one exists. The else block is entirely optional, just like with if.
```
for num in [2, 4, 6]:
    print(num*10)
else:
    print("That's all of the numbers, multiplied by 10.")
```

This loop can't throw an exception and doesn't have a break in it, so the else will always happen.

# Input

We use the input() function to get information from a user.

input("WHAT is your favorite color? ") takes an optional prompt to use when you need to ask the user a particular question. Python doesn't add any space at the end of the prompt, though, so remember to do that yourself.

The value that comes in from input() is always a string, so if you need a number or something else, you'll need to convert it afterward.


# Functions

The basics of creating a function are always the same.

def function_name(argument):

It always starts with the keyword def. Next comes the function name, which follows the same rules as variable names, so no spaces, hyphens, and it can't start with a number. After that is a set of parentheses which have your function's arguments, if any, in them. And then, of course, the line ends with a colon.

The body of the function should be indented.

If you want your function to be able to give an answer back to wherever it was called, like to a variable name or another function, you need to use the return keyword at the end of the function along with whatever value you want returned.

```
def even(num):
    if num % 2 == 0:
        return True
    else:
        return False
```

This function will return True or False depending on whether or not a number is evenly divisible by 2. As a test, can you think of a simpler way to write this?

# Exceptions

We handle exceptions with two blocks, try and except.

The try block is just that, the word try followed by a colon. Inside of the block, indented, is the code that you think might 'cause an issue.

```
try:
    num = int(input("What is the airspeed velocity of an unladen swallow? "))
```

Now, someone might not give us a number for that and that would cause a ValueError. So let's catch it!

```
except ValueError:
```

This block will only trigger if the code in the try caused a ValueError. If the code in the try triggered a TypeError instead, though, this code would never run.

You'll want to create an except block for every type of exception your try block might cause.

Finally, you'll probably want an else block. This block will happen if your try didn't cause any exceptions.

Example

```
try:
    speed = int(input("What is the airspeed velocity of an unladen swallow? "))
except ValueError:
    print("What? I don't kno-oooooooooooooooo!")
else:
    print("I think a swallow could go faster than {}.".format(speed))
```