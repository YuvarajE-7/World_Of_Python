"""
Defining and calling functions
def
return
parameters vs arguments
calling a function
why functions are useful
Parameters and arguments
positional arguments
keyword arguments
default arguments
*args and **kwargs
what problem they solve
how to use them
basic practical examples
Scope
local variables
global variables
global keyword
understanding what variables a function can access
Lambda functions
what they are
when they're useful
simple examples
map()****, filter()****, reduce()
map() → transform
filter() → select
reduce() → combine
especially how they work with lambda
Recursion basics
function calling itself
base case
recursive case
a few simple problems

"""




"""
1. What is a function?

A function is a reusable block of code that performs a specific task.

Without a function:

print("Hello")
print("Welcome to Python")

If you wanted to do this 10 times, you'd have to repeat the code.

With a function : 
def greet():
    print("Hello")
    print("Welcome to Python")

Now you can reuse it:

greet()
greet()
greet()

Output:

Hello
Welcome to Python
Hello
Welcome to Python
Hello
Welcome to Python

The important idea:

Define once → call whenever you need it.

2. Creating a function with def

The basic structure is:

def function_name():
    # code

For example:

def greet():
    print("Hello")

Here:

def → tells Python you're defining a function
greet → function's name
() → parameters will go here later
: → starts the function body
indented code → belongs to the function

But defining the function doesn't execute it.

def greet():
    print("Hello")

Nothing happens yet.

You have to call it:

greet()

Now:

Hello
3. Calling a function

Calling simply means:

Tell Python to execute the function.

def greet():
    print("Hello")


greet()

Think of it like:

def greet()     → create the function


greet()         → execute the function

You can call it multiple times:

def greet():
    print("Hello")


greet()
greet()
greet()

4. Why are functions useful?

Suppose you're building a banking application.

You might need:

deposit()
withdraw()
check_balance()
transfer_money()

Instead of putting everything into one huge program, you break it into smaller pieces.

For example:

def deposit():
    print("Money deposited")


def withdraw():
    print("Money withdrawn")


def check_balance():
    print("Balance checked")

Then:

deposit()
withdraw()
check_balance()

This makes programs:

easier to understand
easier to reuse
easier to test
easier to modify

This is one of the biggest reasons functions are important in real projects.

5. return

Now we get to something very important.

A function can produce a value.

Example:

def add():
    return 10 + 20

When we call:

result = add()


print(result)

Output:

30

return sends a value back out of the function.

Think:

function
   ↓
does some work
   ↓
return result
   ↓
value comes back
print vs return

This distinction is extremely important.

def add():
    print(10 + 20)

This displays 30.

But:

def add():
    return 10 + 20

This gives 30 back to whoever called the function.

So we can do:

result = add()

and use result elsewhere.

6. A very important example
def square(number):
    return number * number

Then:

result = square(5)


print(result)

Output:

25

Don't worry too much about number yet. That's our next topic.

For now, notice the structure:

def square(number):
    return number * number

We give the function something → it does something → it gives us something back.


###################################################################
print() → shows something on the screen

return → sends a value back to the caller
###################################################################
"""












"""

The key idea in Python

# Python uses object references passed by value (often called pass-by-object-reference or call-by-sharing).

You don't need to memorize that terminology yet. Understand the behavior.


1. Immutable objects — int, float, str, tuple

Suppose:

def change(x):
    x = 100


a = 10
change(a)


print(a)

Output:

10

Why?

Initially:

a ─────→ 10

When you call:

change(a)

x refers to the same object:

a ─────→ 10
x ─────→ 10

But then:

x = 100

doesn't change 10.

It makes x point to a different object:

a ─────→ 10


x ─────→ 100

So a remains 10.

2. Mutable objects — list, dict, set

Now:

def change(numbers):
    numbers.append(100)


a = [1, 2, 3]


change(a)


print(a)

Output:

[1, 2, 3, 100]

Here:

a ─────→ [1, 2, 3]
          ↑
          x

Both a and numbers refer to the same list.

And:

numbers.append(100)

modifies that existing list.

So you see the change through a too.

But here's the important distinction

It's not simply:

immutable → changes don't affect outside
mutable → changes affect outside

The more accurate rule is:

Changing what the parameter refers to does not affect the caller's variable. Mutating the object that both variables refer to can affect the caller.

For example, even with a list:

def change(numbers):
    numbers = [100, 200]


a = [1, 2, 3]


change(a)


print(a)

Output:

[1, 2, 3]

Because we reassigned numbers; we didn't modify the original list.

Whereas:

def change(numbers):
    numbers.append(100)

modifies the original list.



Reassignment       → doesn't change caller's variable
Mutation            → can change the shared mutable object


"""






"""
2. Parameters vs Arguments

You already saw this:

def greet(name):
    print("Hello", name)


greet("Arjun")

There are two different terms here.

Parameter

name is a parameter.

def greet(name):

A parameter is the variable written in the function definition.

Argument

"Arjun" is an argument.

greet("Arjun")

An argument is the actual value you give to the function when calling it.

So:

def greet(name):
           ↑
       parameter




greet("Arjun")
      ↑
    argument

A simple way to remember:

Parameter = placeholder
Argument = actual value

"""

"""
3.Types Of Arguments


1. Positional arguments

This is the simplest kind.

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Arjun", 20)

Here:

name ← "Arjun"
age  ← 20

Python matches them based on position.

The first argument goes to the first parameter.

The second argument goes to the second parameter.

What if we change the order?
introduce(20, "Arjun")

Now:

name ← 20
age  ← "Arjun"

Python doesn't know that you intended the opposite. It simply follows the positions.

That's why they're called positional arguments.

2. Keyword arguments

Instead of relying on position, you can explicitly say which parameter gets which value:

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce(age=20, name="Arjun")

Even though the order is reversed:

age  → 20
name → "Arjun"

Python knows exactly where each value goes.

That's a keyword argument.

The keyword is the parameter name:

name="Arjun"
age=20
3. Positional vs keyword

Compare:

introduce("Arjun", 20)

Positional

first value  → first parameter
second value → second parameter

versus:

introduce(name="Arjun", age=20)

Keyword

name → "Arjun"
age  → 20

Both produce the same result.

4. Default arguments

Now suppose we want an age to have a default value.

def introduce(name, age=20):
    print(name)
    print(age)

Now:

introduce("Arjun")

Output:

Arjun
20

Because we didn't provide age, Python uses:

age=20

But we can override it:

introduce("Arjun", 21)

Output:

Arjun
21

So:

Default argument = value used when the caller doesn't provide one.



####################
A parameter with a default value normally comes after parameters without defaults:

def greet(name, message="Hello"):
    ...

Valid

But:

def greet(name="Arjun", message):
    ...

Invalid



5. A practical example

Imagine:

def calculate_bill(amount, tax=18):
    print("Amount:", amount)
    print("Tax:", tax)

You can do:

calculate_bill(1000)

Python uses:

amount = 1000
tax = 18

Or:

calculate_bill(1000, 5)

Now:

amount = 1000
tax = 5


"""

"""

4.*args — Variable-Length Positional Arguments

You already know this:

def add(a, b):
    return a + b

It expects exactly 2 arguments:

add(10, 20)       # 
add(10, 20, 30)   # 

But sometimes we don't know how many arguments we'll receive.

For example, we might want:

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)

That's where *args comes in.

1. Basic idea
def add(*args):
    print(args)

Now:

add(10, 20)

gives:

(10, 20)

And:

add(10, 20, 30, 40)

gives:

(10, 20, 30, 40)

So *args collects all positional arguments into a tuple.

Think:

add(10, 20, 30)


       ↓


args = (10, 20, 30)
2. args is just a variable name

This is important.

The * is what gives the special meaning.

You could technically write:

def add(*numbers):
    print(numbers)

Then:

add(10, 20, 30)

gives:

(10, 20, 30)

So:

*args

is just the common convention.

You might see:

def add(*numbers):

and it works exactly the same way.

3. Why is it called variable-length?

Because the number of arguments can vary.

add()

→ args = ()

add(10)

→ args = (10,)

add(10, 20)

→ args = (10, 20)

add(10, 20, 30, 40)

→ args = (10, 20, 30, 40)

The function doesn't need to know beforehand how many arguments it will receive.

4. Using the values inside args

Since args is a tuple, you can loop through it.

def show_numbers(*args):
    for num in args:
        print(num)


show_numbers(10, 20, 30, 40)

Output:

10
20
30
40

You can also use indexing:

def show_first(*args):
    print(args[0])


show_first(10, 20, 30)

Output:

10

Because:

args = (10, 20, 30)
        ↑
      args[0]
5. Practical example — adding any number of numbers

Now *args becomes useful.

def add(*args):
    total = 0


    for num in args:
        total += num


    return total

Now:

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40, 50))

Output:

30
60
150

One function handles any number of numbers.

6. *args doesn't mean "accept everything"

It specifically collects positional arguments.

def show(*args):
    print(args)


show(10, 20, 30)

works.

But keyword arguments are different:

show(a=10, b=20)

Those aren't collected by *args.

That's where **kwargs comes in.

"""


"""
5.  **kwargs

Suppose we have:

def student(name, age):
    print(name, age)

We can call:

student(name="Arjun", age=20)

But what if we want to accept any number of keyword arguments?

We can do:

def student(**kwargs):
    print(kwargs)

Then:

student(name="Arjun", age=20)

Output:

{'name': 'Arjun', 'age': 20}

**kwargs collects keyword arguments into a dictionary.

8. Think of the difference like this
*args
def test(*args):

Collects:

test(10, 20, 30)

into:

args = (10, 20, 30)

Tuple

**kwargs
def test(**kwargs):

Collects:

test(name="Arjun", age=20)

into:

kwargs = {
    "name": "Arjun",
    "age": 20
}

Dictionary

So remember:

*args       → positional arguments → tuple


**kwargs    → keyword arguments   → dictionary
9. Practical **kwargs example
def student(**details):
    for key, value in details.items():
        print(key, ":", value)

Now:

student(
    name="Arjun",
    age=20,
    branch="CSE"
)

Output:

name : Arjun
age : 20
branch : CSE

We didn't have to define:

name
age
branch

beforehand.

The function can accept whatever keyword information we give it.

10. You can use both

You can have:

def test(*args, **kwargs):
    print(args)
    print(kwargs)

Then:

test(10, 20, 30, name="Arjun", age=20)

produces conceptually:

args:
(10, 20, 30)


kwargs:
{'name': 'Arjun', 'age': 20}

So:

10, 20, 30
      ↓
    *args


name="Arjun", age=20
      ↓
   **kwargs

   
#############################################
   Why .items()?

This is important because kwargs is a dictionary.

When you do:

show_details(name="Arjun", age=20, city="Chennai")

inside the function, Python creates:

kwargs = {
    "name": "Arjun",
    "age": 20,
    "city": "Chennai"
}

A dictionary contains key → value pairs.

Without .items()

If you do:

def show_details(**kwargs):
    for i in kwargs:
        print(i)

you get only the keys:

name
age
city

Because looping directly over a dictionary gives you its keys.

With .items()
def show_details(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

.items() gives you the key and value together.

Conceptually:

kwargs.items()


("name", "Arjun")
("age", 20)
("city", "Chennai")

So:

for i, j in kwargs.items():

means:

i = key
j = value

Therefore:

name Arjun
age 20
city Chennai



"""




"""
6. Scope 

1. What is Scope?

Scope defines where a variable can be accessed and used in a program.

For functions, the two important scopes are:

Local scope → inside a function
Global scope → outside functions


2. Local Variables

A variable created inside a function is a local variable.

def greet():
    name = "Arjun"
    print(name)


greet()

Here, name is local to greet().

It cannot normally be accessed outside:

def greet():
    name = "Arjun"


greet()
print(name)   # Error


Key point

A local variable belongs to the function in which it is created.





3. Global Variables

A variable created outside all functions is a global variable.

name = "Arjun"


def greet():
    print(name)


greet()

Output:

Arjun

A function can read a global variable.




4. Local vs Global Variable with Same Name
x = 10


def test():
    x = 20
    print(x)


test()
print(x)

Output:

20
10

Why?

There are two different variables:

Global x → 10
Local x  → 20

The local x does not change the global x.



5. What Variables Can a Function Access?

A function can access:

Its own local variables

def test():
    x = 10
    print(x)



Global variables

x = 10

def test():
    print(x)

But a function cannot access another function's local variable:

def first():
    x = 10


def second():
    print(x)   # Error

x belongs only to first().

6. Reading a Global Variable

Reading a global variable inside a function is allowed.

x = 10


def test():
    print(x)


test()

Output:

10

You do not need the global keyword just to read it.

7. Assignment Creates a Local Variable

This is an important rule.

x = 10


def test():
    x = 20


test()


print(x)

Output:

10

The x = 20 creates a new local x.

It does not modify the global x.

8. Why UnboundLocalError Happens

Consider:

x = 10


def test():
    print(x)
    x = 20


test()

This causes:

UnboundLocalError
Why?

Because Python sees:

x = 20

inside the function.

Therefore, Python treats x as local throughout the function.

So this:

print(x)

is trying to read the local x before it has been assigned a value.

Conceptually:

test()
 ↓
local x exists
 ↓
print(x)     ← x has no value yet ❌
 ↓
x = 20



9. global Keyword

The global keyword tells Python:

Use the global variable instead of creating a local variable.

Example:

x = 10


def test():
    global x
    x = 20


test()


print(x)

Output:

20

Now x = 20 modifies the global x.

10. Reading + Modifying a Global Variable

Without global:

x = 10


def test():
    print(x)
    x = 20

❌ UnboundLocalError

With global:

x = 10


def test():
    global x
    print(x)
    x = 20


test()


print(x)

Output:

10
20

Because global x tells Python that both:

print(x)
x = 20

refer to the same global variable.

11. Important Rule

Remember this:

Reading a global variable → global not required.

x = 10


def test():
    print(x)

✅

Assigning to a global variable → global required.

x = 10


def test():
    global x
    x = 20

✅
  
12. Scope Summary
                    Program
                       │
             ┌─────────┴─────────┐
             │                   │
        Global Scope        Function Scope
             │                   │
          x = 10              y = 20
             │                   │
             │             local variable
             │
       accessible inside
          functions


Quick reference
Situation	Result
Variable created outside function	Global
Variable created inside function	Local

Function reads global	✅ Allowed
Function creates local	✅ Allowed
Local variable accessed outside function	❌ Error
Function modifies global without global	❌ Not allowed
global x inside function	Allows modification of global x
Read global variable	No global needed
The one rule I'd remember most

Python sees an assignment to x inside a function → x is treated as local unless you explicitly say global x.


"""



"""
7.Lambda Functions

1. What is a Lambda Function?

A lambda function is a small function written in a single line.

Normal function:

def square(x):
    return x * x

The same idea using lambda:

square = lambda x: x * x

Then:

print(square(5))

Output:

25

So you can think of:

lambda x: x * x

as:

"Take x and return x * x."

2. Lambda Syntax

The basic syntax is:

lambda parameters: expression

For example:

lambda x: x * 2

Break it down:

lambda   → tells Python we're creating a lambda
x        → parameter
:        → separates parameter from the expression
x * 2    → expression/result

Compare with a normal function:

def double(x):
    return x * 2

Lambda:

double = lambda x: x * 2

Both do the same thing.

3. Lambda with Multiple Parameters

You can have multiple parameters:

add = lambda a, b: a + b


print(add(5, 3))

Output:

8

Equivalent normal function:

def add(a, b):
    return a + b
4. Lambda Doesn't Need an Explicit return

Normal function:

def square(x):
    return x * x

Lambda:

square = lambda x: x * x

The expression after : is automatically the result.

So don't write:

lambda x: return x * x

❌ That's invalid.

5. Lambda with Conditions

You can also use a conditional expression.

check = lambda x: "Even" if x % 2 == 0 else "Odd"


print(check(4))
print(check(7))

Output:

Even
Odd

Don't worry about making complicated lambdas. They're intended for small operations.

6. Why Do We Need Lambda?

This is the important question.

Suppose you need a function only once:

def double(x):
    return x * 2


numbers = [1, 2, 3, 4]

Creating a named function just for one small operation can sometimes be unnecessary.

Lambda lets you write the function directly:

lambda x: x * 2

This becomes especially useful with:

map()
filter()
reduce()
sorting with custom conditions

You'll see why when we reach those topics.

7. Lambda vs Normal Function
Normal function
def square(x):
    return x * x

Good when:

Function is reused
Logic is more complicated
Function needs multiple statements
You want a descriptive function name
Lambda
lambda x: x * x

Good when:

Operation is very small
Function is used temporarily
You don't need a full named function

Think:

Lambda = small, temporary/simple function.

8. Important Limitation

A lambda is limited to one expression.

This is fine:

square = lambda x: x * x

But you can't write a normal multi-line function with several statements inside a lambda.

So don't think:

"Lambda is a better version of def."

It's not.

It's simply a convenient way of creating a small function.



"""

"""
8. map() function


1. What is map()?

map() is a built-in Python function used to apply a function to every element of an iterable and produce the transformed results.

Simple definition

map() → transform every element.

For example, if you have:

numbers = [1, 2, 3, 4]

and want to double every number:

[2, 4, 6, 8]

map() can do this directly.

2. Syntax

The basic syntax is:

map(function, iterable)

Example:

numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(list(result))

Output:

[2, 4, 6, 8]
Parts
map(lambda x: x * 2, numbers)
    │              │
    │              └── iterable
    └── function

map() takes:

A function — what operation should be performed?
An iterable — which elements should it be performed on?
3. How map() Works

Suppose:

numbers = [1, 2, 3, 4]

and:

map(lambda x: x * 2, numbers)

Conceptually, map() does:

1 → 1 × 2 → 2
2 → 2 × 2 → 4
3 → 3 × 2 → 6
4 → 4 × 2 → 8

Result:

[2, 4, 6, 8]

The function is applied once to each element.

4. map() with a Normal Function

You don't have to use lambda.

You can define a normal function:

def double(x):
    return x * 2

Then:

numbers = [1, 2, 3, 4]


result = map(double, numbers)


print(list(result))

Output:

[2, 4, 6, 8]

Here:

map(double, numbers)

means:

Apply double() to every element in numbers.

Conceptually:

double(1) → 2
double(2) → 4
double(3) → 6
double(4) → 8
5. Why Don't We Write double()?

This is important.

Correct:

map(double, numbers)

Incorrect:

map(double(), numbers)

Why?

double

means:

Give map() the function itself.

double()

means:

Call the function immediately.

map() needs the function, because map() will call it for each element.

Think:

double     → function
double()   → result of calling the function
6. map() with Lambda

This is where lambda becomes particularly useful.

Instead of:

def double(x):
    return x * 2


result = map(double, numbers)

you can write:

result = map(lambda x: x * 2, numbers)

Both perform the same transformation.

Normal function
def square(x):
    return x * x


result = map(square, numbers)
Lambda
result = map(lambda x: x * x, numbers)

Lambda is convenient when the function is small and only needed for this operation.

7. map() Returns a Map Object

Consider:

numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(result)

You won't get:

[2, 4, 6, 8]

Instead, you'll see something representing a map object.

That's because map() returns a map object rather than directly returning a list.

8. Converting the Result to a List

Most beginner examples use:

list(result)

Example:

numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(list(result))

Output:

[2, 4, 6, 8]

So remember:

map() → map object
list() → converts it to a list
9. map() Does Not Modify the Original Iterable

Example:

numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(numbers)
print(list(result))

Output:

[1, 2, 3, 4]
[2, 4, 6, 8]

The original list is unchanged.

map() creates transformed results rather than changing the original list.

10. Different Transformations

map() isn't only for multiplication.

Square
numbers = [1, 2, 3, 4]


result = map(lambda x: x * x, numbers)


print(list(result))
[1, 4, 9, 16]
Add 10
result = map(lambda x: x + 10, numbers)
[11, 12, 13, 14]
Convert to strings
numbers = [1, 2, 3]


result = map(lambda x: str(x), numbers)


print(list(result))
['1', '2', '3']
Convert strings to uppercase
names = ["arjun", "rahul", "kiran"]


result = map(lambda name: name.upper(), names)


print(list(result))
['ARJUN', 'RAHUL', 'KIRAN']

So the operation can be almost anything that makes sense for each element.

11. map() with Multiple Iterables

map() can work with more than one iterable.

Syntax:

map(function, iterable1, iterable2, ...)

Example:

a = [1, 2, 3]
b = [10, 20, 30]


result = map(lambda x, y: x + y, a, b)


print(list(result))

Output:

[11, 22, 33]
How?

Corresponding elements are passed together:

a       b


1  +   10  → 11
2  +   20  → 22
3  +   30  → 33

So:

lambda x, y: x + y

receives:

x = 1, y = 10
x = 2, y = 20
x = 3, y = 30
12. Multiple Iterables Require Multiple Parameters

If you have:

map(function, list1, list2)

your function needs two parameters.

Example:

map(lambda x, y: x + y, list1, list2)

Here:

2 iterables → 2 parameters

For three:

map(lambda x, y, z: x + y + z, a, b, c)
3 iterables → 3 parameters
13. Different-Length Iterables

Suppose:

a = [1, 2, 3, 4]
b = [10, 20]

Then:

result = map(lambda x, y: x + y, a, b)


print(list(result))

Output:

[11, 22]

map() stops when the shortest iterable is exhausted.

Conceptually:

1 + 10 → 11
2 + 20 → 22
3 + ?  → stop
4 + ?  → stop
14. map() Can Work with Other Iterables

map() doesn't only work with lists.

It can work with iterables such as:

Lists
Tuples
Strings
Sets
Other iterable objects

Example with a tuple:

numbers = (1, 2, 3)


result = map(lambda x: x * 2, numbers)


print(list(result))
[2, 4, 6]
15. map() with Built-in Functions

You don't always need lambda or your own function.

Example:

numbers = ["1", "2", "3", "4"]


result = map(int, numbers)


print(list(result))

Output:

[1, 2, 3, 4]

Here:

map(int, numbers)

means:

Apply int() to every element.

Conceptually:

"1" → int("1") → 1
"2" → int("2") → 2
"3" → int("3") → 3
"4" → int("4") → 4

This is a very useful real-world pattern.

16. map() vs for Loop

The same operation can usually be written both ways.

Using a loop
numbers = [1, 2, 3, 4]


result = []


for x in numbers:
    result.append(x * 2)


print(result)
Using map()
numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(list(result))

Both produce:

[2, 4, 6, 8]
Difference

The loop gives you more control over complicated logic.

map() clearly expresses:

"Apply this transformation to every element."

17. map() vs filter()

This distinction is extremely important.

map() → Transform
numbers = [1, 2, 3, 4]


map(lambda x: x * 2, numbers)

Result:

[2, 4, 6, 8]

Every element is transformed.

filter() → Select
numbers = [1, 2, 3, 4]


filter(lambda x: x % 2 == 0, numbers)

Result:

[2, 4]

Only some elements remain.

Remember:

map() asks: "What should each element become?"

filter() asks: "Should this element stay?"

18. Common Mistakes
Mistake 1 — Calling the function

❌

map(double(), numbers)

✅

map(double, numbers)
Mistake 2 — Forgetting to convert when you need a list
result = map(lambda x: x * 2, numbers)


print(result)

This doesn't display the transformed list.

Use:

print(list(result))

when you need a list representation.

Mistake 3 — Using the wrong number of parameters

For:

map(lambda x, y: x + y, a, b)

there are two iterables, so the function needs two parameters.

Mistake 4 — Thinking map() changes the original list
numbers = [1, 2, 3]


map(lambda x: x * 2, numbers)


print(numbers)

The original remains:

[1, 2, 3]
19. Important Concept: map() Is Lazy

This is slightly more advanced, but useful to know.

map() doesn't necessarily calculate and store all transformed values immediately.

It produces values as they are requested.

For example:

result = map(lambda x: x * 2, numbers)

creates a map object.

When you do:

list(result)

Python requests the values and collects them into a list.

This behavior is called lazy evaluation.

For your current level, you don't need to study the internals. Just remember:

map() returns a map object that produces transformed values when iterated over.

20. Important Concept: Map Object Can Be Consumed

Because map() is an iterator-like object, once you've consumed its values, they aren't available again from that same object.

Example:

numbers = [1, 2, 3]


result = map(lambda x: x * 2, numbers)


print(list(result))
print(list(result))

Output:

[2, 4, 6]
[]

Why?

The first list(result) consumed the values.

If you need them again:

result = map(lambda x: x * 2, numbers)


values = list(result)


print(values)
print(values)

Now both work because values is a list.

21. General Mental Model

Whenever you see:

map(function, iterable)

think:

              function
                  ↓
element 1 ─────────────→ result 1
element 2 ─────────────→ result 2
element 3 ─────────────→ result 3
element 4 ─────────────→ result 4

Example:

map(lambda x: x + 5, [1, 2, 3, 4])

becomes:

1 → 6
2 → 7
3 → 8
4 → 9

Result:

[6, 7, 8, 9]
22. Quick Reference
map()
│
├── Purpose
│   └── Transform every element
│
├── Syntax
│   └── map(function, iterable)
│
├── Function can be
│   ├── Normal function
│   ├── Lambda
│   └── Built-in function
│
├── Returns
│   └── map object
│
├── Common conversion
│   └── list(result)
│
├── Multiple iterables
│   └── map(function, iterable1, iterable2, ...)
│
├── Original iterable
│   └── Not modified
│
└── Key idea
    └── "Transform each element"


The 5 things you should remember
map() transforms every element.
It takes a function + iterable.
Lambda is commonly used when the transformation is small.
map() returns a map object, often converted with list().
With multiple iterables, corresponding elements are passed to the function.
One-line memory trick



"""


"""
9. filter()

filter() is a built-in Python function used when you want to keep only the elements that satisfy a condition.

The easiest way to remember:

map() → transform every element
filter() → select some elements

1. Basic Syntax
filter(function, iterable)

There are two parts:

function → decides whether an element should be kept
iterable → list, tuple, set, string, etc.

The function should return:

True → keep the element
False → remove the element
Example
numbers = [1, 2, 3, 4, 5, 6]


result = filter(lambda x: x % 2 == 0, numbers)


print(list(result))

Output:

[2, 4, 6]

For each number:

1 → False → remove
2 → True  → keep
3 → False → remove
4 → True  → keep
5 → False → remove
6 → True  → keep
2. Why do we use filter()?

Suppose you have:

numbers = [10, 15, 20, 25, 30]

and you only want numbers greater than 20.

Without filter()
result = []


for num in numbers:
    if num > 20:
        result.append(num)


print(result)

Output:

[25, 30]
With filter()
result = filter(lambda x: x > 20, numbers)


print(list(result))

Output:

[25, 30]

So filter() is basically a compact way of expressing:

"Go through the elements and keep the ones satisfying this condition."

3. filter() returns a filter object

This is VERY important.

numbers = [1, 2, 3, 4]


result = filter(lambda x: x % 2 == 0, numbers)


print(result)

You won't get:

[2, 4]

Instead, you'll see something similar to:

<filter object at 0x...>

Why?

Because filter() returns an iterator.

Usually, you'll convert it to a list:

result = list(filter(lambda x: x % 2 == 0, numbers))

Now:

[2, 4]
4. filter() with a normal function

You don't have to use lambda.

def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]


result = filter(is_even, numbers)


print(list(result))

Output:

[2, 4, 6]

Here:

filter(is_even, numbers)

means:

Apply is_even() to every element and keep the elements for which it returns True.

5. filter() with strings

You can filter characters too.

letters = ['a', 'b', '1', 'c', '2', '3']


result = filter(lambda x: x.isdigit(), letters)


print(list(result))

Output:

['1', '2', '3']

Another example:

words = ["apple", "cat", "elephant", "dog"]


result = filter(lambda word: len(word) > 3, words)


print(list(result))

Output:

['apple', 'elephant']
6. filter() with tuples
numbers = (10, 15, 20, 25, 30)


result = filter(lambda x: x > 20, numbers)


print(tuple(result))

Output:

(25, 30)

The output type depends on what you convert the filter object into.

list(result)
tuple(result)
set(result)
7. filter() with sets
numbers = {1, 2, 3, 4, 5, 6}


result = filter(lambda x: x % 2 == 0, numbers)


print(set(result))

Output:

{2, 4, 6}

Remember that sets don't maintain duplicates.

8. filter() with dictionaries

This is an important area.

When you iterate over a dictionary directly, you get its keys.

data = {
    "a": 10,
    "b": 20,
    "c": 30
}


result = filter(lambda key: data[key] > 15, data)


print(list(result))

Output:

['b', 'c']

Because:

data

iterates over:

"a"
"b"
"c"
Filtering dictionary items

If you want to filter based on values:

data = {
    "a": 10,
    "b": 20,
    "c": 30
}


result = filter(lambda item: item[1] > 15, data.items())


print(list(result))

Output:

[('b', 20), ('c', 30)]

Here:

data.items()

produces:

('a', 10)
('b', 20)
('c', 30)

and:

item[1]

means the value.

9. The None case

filter() has a special behavior.

You can write:

filter(None, iterable)

In this case, Python keeps elements that are truthy.

Example:

numbers = [0, 1, 2, 0, 3, 0]


result = filter(None, numbers)


print(list(result))

Output:

[1, 2, 3]

Because:

0 → False
1 → True
2 → True
0 → False
3 → True
0 → False

So:

filter(None, iterable)

roughly means:

Remove falsy values.

10. What are falsy values?

Common falsy values:

False
None
0
0.0
""
[]
()
{}
set()

Example:

data = [0, 1, "", "hello", None, False, 5]


print(list(filter(None, data)))

Output:

[1, 'hello', 5]
11. filter() with a normal condition

You can use any function that returns a Boolean.

def is_positive(x):
    return x > 0


numbers = [-5, -2, 0, 3, 7]


print(list(filter(is_positive, numbers)))

Output:

[3, 7]

The important thing is not the function's name.

The important thing is:

return True

or

return False
12. filter() with multiple conditions

You can use and, or, etc.

Example: even AND greater than 10
numbers = [5, 8, 12, 14, 17, 20]


result = filter(
    lambda x: x % 2 == 0 and x > 10,
    numbers
)


print(list(result))

Output:

[12, 14, 20]
Example: less than 10 OR greater than 20
numbers = [5, 8, 12, 18, 22, 25]


result = filter(
    lambda x: x < 10 or x > 20,
    numbers
)


print(list(result))

Output:

[5, 8, 22, 25]
13. filter() vs list comprehension

You can achieve the same thing with list comprehension.

filter()
numbers = [1, 2, 3, 4, 5, 6]


result = list(filter(lambda x: x % 2 == 0, numbers))
List comprehension
result = [x for x in numbers if x % 2 == 0]

Both produce:

[2, 4, 6]
Which should you know?

Both.

List comprehensions are often more readable in Python.

But filter() is important because:

it's a built-in functional programming tool
it works with functions directly
it returns an iterator
it becomes especially useful when combined with map()
14. filter() vs map()

This distinction is very important.

map()

map() means:

Transform every element.

Example:

numbers = [1, 2, 3, 4]


result = map(lambda x: x * 2, numbers)


print(list(result))

Output:

[2, 4, 6, 8]

Every element is transformed.

filter()

filter() means:

Select elements based on a condition.

numbers = [1, 2, 3, 4]


result = filter(lambda x: x % 2 == 0, numbers)


print(list(result))

Output:

[2, 4]

Only some elements remain.

Remember:
MAP    → CHANGE
FILTER → CHOOSE

or:

map()    → "What should I do to each element?"
filter() → "Which elements should I keep?"
15. Using filter() + map()

This is one of the most important patterns.

Suppose:

numbers = [1, 2, 3, 4, 5, 6]

You want:

Keep only even numbers
Square them

Expected:

[4, 16, 36]

First, filter:

even_numbers = filter(lambda x: x % 2 == 0, numbers)

Then map:

squared = map(lambda x: x ** 2, even_numbers)

Finally:

print(list(squared))

Output:

[4, 16, 36]
16. Think of the process like a pipeline

This is the best mental model.

Original data
     ↓
   filter()
     ↓
Selected data
     ↓
    map()
     ↓
Transformed data

For:

numbers = [1, 2, 3, 4, 5, 6]

we have:

[1, 2, 3, 4, 5, 6]
          ↓
       filter
          ↓
      [2, 4, 6]
          ↓
        map
          ↓
      [4, 16, 36]
17. filter() + map() in one expression

You can combine them:

numbers = [1, 2, 3, 4, 5, 6]


result = map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, numbers)
)


print(list(result))

Output:

[4, 16, 36]

Read it from the inside outward:

filter(lambda x: x % 2 == 0, numbers)

First:

[1,2,3,4,5,6]
        ↓
     filter
        ↓
     [2,4,6]

Then:

map(lambda x: x ** 2, ...)

becomes:

[2,4,6]
   ↓
  map
   ↓
[4,16,36]
18. Another practical example

Suppose you have student marks:

marks = [35, 72, 48, 90, 65, 28]

You want students who passed.

Assume pass mark = 40.

passed = filter(lambda mark: mark >= 40, marks)


print(list(passed))

Output:

[72, 48, 90, 65]

Now suppose you want to add 5 bonus marks to only the passed students.

marks = [35, 72, 48, 90, 65, 28]


passed = filter(lambda mark: mark >= 40, marks)


bonus = map(lambda mark: mark + 5, passed)


print(list(bonus))

Output:

[77, 53, 95, 70]

That's a very natural filter → map pipeline.

19. Another practical example with strings
names = ["Arun", "Raj", "Alexander", "Sam", "Christopher"]

Suppose we want names with more than 4 characters and then convert them to uppercase.

Step 1 — filter
long_names = filter(lambda name: len(name) > 4, names)

Result conceptually:

["Alexander", "Christopher"]
Step 2 — map
upper_names = map(lambda name: name.upper(), long_names)
Final
print(list(upper_names))

Output:

['ALEXANDER', 'CHRISTOPHER']
20. Order matters

Compare:

filter()
→
map()

with:

map()
→
filter()

They can produce different results.

Example:

numbers = [1, 2, 3, 4, 5]
Filter first

Keep even numbers:

filter(lambda x: x % 2 == 0, numbers)

Then square:

[2,4]
 ↓
[4,16]
Map first

Square everything:

map(lambda x: x ** 2, numbers)

Result:

[1,4,9,16,25]

Then filter numbers greater than 10:

[16,25]

So:

filter → map

and

map → filter

are not automatically interchangeable.

21. filter() is lazy

This is another important concept.

When you write:

result = filter(lambda x: x > 10, numbers)

Python doesn't immediately create a new list containing all the results.

It creates a filter iterator.

The values are produced when you ask for them.

For example:

result = filter(lambda x: x > 10, [5, 15, 20, 25])


print(list(result))

The list() consumes the iterator.

22. Filter objects can be consumed only once

Example:

numbers = [1, 2, 3, 4]


result = filter(lambda x: x % 2 == 0, numbers)


print(list(result))
print(list(result))

Output:

[2, 4]
[]

Why?

Because the iterator was already consumed.

If you need to use the result multiple times:

result = list(filter(lambda x: x % 2 == 0, numbers))


print(result)
print(result)

Now:

[2, 4]
[2, 4]
23. filter() does not modify the original list

Example:

numbers = [1, 2, 3, 4]


result = list(filter(lambda x: x % 2 == 0, numbers))


print(numbers)
print(result)

Output:

[1, 2, 3, 4]
[2, 4]

The original list remains unchanged.

24. Passing a normal function vs lambda

Both are valid.

Lambda
numbers = [1, 2, 3, 4, 5]


result = list(
    filter(lambda x: x > 3, numbers)
)
Normal function
def greater_than_three(x):
    return x > 3


result = list(filter(greater_than_three, numbers))

Use a lambda when the condition is simple.

Use a normal function when:

the condition is complicated
you'll reuse it
you want clearer code
25. Common mistakes
Mistake 1 — Forgetting list()
result = filter(lambda x: x > 5, numbers)


print(result)

This prints a filter object.

Use:

print(list(result))
Mistake 2 — Returning the element instead of a condition

Bad:

filter(lambda x: x * 2, numbers)

This technically works based on truthiness, but it's not a clear filtering condition.

Better:

filter(lambda x: x % 2 == 0, numbers)
Mistake 3 — Confusing map() and filter()

If you're changing values:

map()

If you're deciding which values survive:

filter()
Mistake 4 — Trying to use if/else as the main filter logic

For example:

filter(lambda x: "Even" if x % 2 == 0 else "Odd", numbers)

This is not doing what you probably intend, because both "Even" and "Odd" are truthy.

For filtering, return a Boolean condition:

filter(lambda x: x % 2 == 0, numbers)
26. filter() + map() + lambda relationship

These three often appear together, so keep their roles separate.

lambda

Creates a small anonymous function.

lambda x: x * 2
map()

Applies that function to every element.

map(lambda x: x * 2, numbers)
filter()

Uses a function to decide which elements survive.

filter(lambda x: x > 10, numbers)

So:

lambda → provides the logic
map    → applies transformation
filter → applies selection
27. The general pattern
Filter
filter(condition, iterable)

Think:

element → condition → True/False
                         ↓
                    True = keep
                    False = remove
Map
map(transformation, iterable)

Think:

element → transformation → new value
28. Complexity

For:

filter(lambda x: x > 10, numbers)

if there are n elements, you potentially examine every element.

Time complexity
O(n)

For:

map(lambda x: x * 2, numbers)

also:

O(n)

For:

map(
    lambda x: x * 2,
    filter(lambda x: x > 10, numbers)
)

the overall work is still generally:

O(n)

because you go through the input elements.

29. Important interview/exam points

Know these:

filter()
filter(function, iterable)
Built-in Python function
Used to select elements
Function should generally return a Boolean/truthy value
Returns a filter object
Filter object is an iterator
Usually converted using list()
Does not modify the original iterable
Lazy evaluation
Can be combined with map()
filter(None, iterable) removes falsy values
30. Quick comparison table
Feature	map()	filter()
Purpose	Transform	Select
Works on	Every element	Every element
Output	Transformed values	Selected original values
Function	Transformation	Condition
Function usually returns	New value	Boolean/truthy value
Returns	map object	filter object
Lazy	Yes	Yes
Example	Square numbers	Keep even numbers
31. Most important patterns to remember
Pattern 1 — Filter even numbers
list(filter(lambda x: x % 2 == 0, numbers))
Pattern 2 — Filter positive numbers
list(filter(lambda x: x > 0, numbers))
Pattern 3 — Filter strings
list(filter(lambda x: len(x) > 5, words))
Pattern 4 — Remove falsy values
list(filter(None, values))
Pattern 5 — Filter then transform
list(
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)
🧠 Final mental map
                 FUNCTIONAL TOOLS
                        │
          ┌─────────────┴─────────────┐
          │                           │
        map()                     filter()
          │                           │
     TRANSFORM                    SELECT
          │                           │
   "Change every item"        "Keep some items"
          │                           │
    x → x * 2                  x → x > 10
          │                           │
   [1,2,3] → [2,4,6]          [5,15,20] → [15,20]

And when combined:

DATA
 ↓
filter()
 ↓
SELECT WHAT YOU NEED
 ↓
map()
 ↓
TRANSFORM IT
 ↓
FINAL RESULT
The one sentence you should remember

filter() selects elements based on a condition, while map() transforms elements.

"""


"""
10. reduce()


1. What is reduce()?

reduce() is used when you want to repeatedly combine elements of an iterable until only one final value remains.

Think:

map() → transform
filter() → select
reduce() → combine

Example:

numbers = [1, 2, 3, 4]

Suppose we want the sum.

reduce() works conceptually like:

1 + 2 → 3
3 + 3 → 6
6 + 4 → 10

Final answer:

10
2. Where does reduce() come from?

Unlike map() and filter(), reduce() is not directly available as a built-in function.

You import it from functools:

from functools import reduce

Then:

reduce(function, iterable)
3. Basic syntax
from functools import reduce


reduce(function, iterable)

Example:

from functools import reduce


numbers = [1, 2, 3, 4]


result = reduce(lambda x, y: x + y, numbers)


print(result)

Output:

10
4. How does reduce() actually work?

This is the most important concept.

Given:

numbers = [1, 2, 3, 4]

and:

reduce(lambda x, y: x + y, numbers)

Python does:

Step 1:
x = 1
y = 2
1 + 2 = 3


Step 2:
x = 3
y = 3
3 + 3 = 6


Step 3:
x = 6
y = 4
6 + 4 = 10

So:

[1, 2, 3, 4]
     ↓
  1 + 2
     ↓
     3
     ↓
  3 + 3
     ↓
     6
     ↓
  6 + 4
     ↓
    10

The important idea:

The result from the previous operation becomes the first argument of the next operation.

5. Why does the function take TWO arguments?

This is different from map() and filter().

map()

Usually:

lambda x: ...

One element at a time.

filter()

Usually:

lambda x: condition

One element at a time.

reduce()
lambda x, y: ...

It combines two values at a time.

Example:

reduce(lambda x, y: x + y, numbers)

Here:

x → accumulated result
y → next element
6. The accumulator concept

This is the key word to learn:

Accumulator

The accumulated result keeps changing.

For:

[1, 2, 3, 4]

we can think:

accumulator    next value


     1             2
     ↓
     3


     3             3
     ↓
     6


     6             4
     ↓
    10

So conceptually:

accumulator = previous result

and:

next value = next element
7. reduce() for multiplication
from functools import reduce


numbers = [1, 2, 3, 4]


result = reduce(lambda x, y: x * y, numbers)


print(result)

Output:

24

Process:

1 × 2 = 2
2 × 3 = 6
6 × 4 = 24

This is essentially calculating:

1 × 2 × 3 × 4
8. reduce() for finding the largest number
from functools import reduce


numbers = [10, 25, 7, 40, 15]


result = reduce(lambda x, y: x if x > y else y, numbers)


print(result)

Output:

40

Process:

10 vs 25 → 25
25 vs 7  → 25
25 vs 40 → 40
40 vs 15 → 40

So:

final = 40
9. Using a normal function

You don't have to use lambda.

from functools import reduce


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4]


result = reduce(add, numbers)


print(result)

Output:

10

This is often easier to understand while learning.

10. reduce() with an initializer

There is another form:

reduce(function, iterable, initializer)

The third argument is called the initializer.

Example:

from functools import reduce


numbers = [1, 2, 3, 4]


result = reduce(lambda x, y: x + y, numbers, 10)


print(result)

Output:

20

Why?

Instead of starting with:

1 + 2

it starts with:

10 + 1

Then:

11 + 2 = 13
13 + 3 = 16
16 + 4 = 20

So:

initializer = starting accumulator
11. Visualizing the initializer

Without initializer:

[1, 2, 3, 4]


1 + 2 → 3
3 + 3 → 6
6 + 4 → 10

With initializer 10:

10 + 1 → 11
11 + 2 → 13
13 + 3 → 16
16 + 4 → 20

Very important:

The initializer becomes the initial accumulator.

12. Why use an initializer?

It is useful when you want a specific starting value.

For example:

from functools import reduce


numbers = [1, 2, 3]


result = reduce(lambda x, y: x + y, numbers, 100)


print(result)

Output:

106

Because:

100 + 1 = 101
101 + 2 = 103
103 + 3 = 106
13. What happens with an empty list?

Consider:

numbers = []

If you do:

reduce(lambda x, y: x + y, numbers)

Python doesn't have a first value to use as the accumulator.

So it raises an error.

But with an initializer:

reduce(lambda x, y: x + y, numbers, 0)

the result is:

0

This is another reason initializers can be useful.

14. reduce() vs normal loop

Suppose:

numbers = [1, 2, 3, 4]
Normal loop
total = 0


for num in numbers:
    total += num


print(total)
reduce()
from functools import reduce


total = reduce(lambda x, y: x + y, numbers)


print(total)

Both give:

10

So reduce() is essentially expressing an accumulation operation in functional style.

15. reduce() vs sum()

This is important.

For simply adding numbers:

sum(numbers)

is generally clearer than:

reduce(lambda x, y: x + y, numbers)

So don't use reduce() just because you can.

For example:

sum([1, 2, 3, 4])

is better than:

reduce(lambda x, y: x + y, [1, 2, 3, 4])

reduce() becomes more interesting when the operation is something more general.

16. reduce() vs map() vs filter()

This is the big picture.

Function	Purpose	Example
map()	Transform every element	Square numbers
filter()	Select elements	Keep even numbers
reduce()	Combine elements into one result	Sum/product

Think:

MAP
↓
Many inputs → Many outputs


FILTER
↓
Many inputs → Fewer outputs


REDUCE
↓
Many inputs → One output

This mental model is extremely useful.

17. Combining filter() and reduce()

Now we can start combining the concepts you've learned.

Suppose:

numbers = [1, 2, 3, 4, 5, 6]

We want:

Find the sum of only the even numbers.

First:

filter(lambda x: x % 2 == 0, numbers)

gives:

[2, 4, 6]

Then reduce:

reduce(lambda x, y: x + y, ...)

So:

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]


result = reduce(
    lambda x, y: x + y,
    filter(lambda x: x % 2 == 0, numbers)
)


print(result)

Output:

12

Pipeline:

[1,2,3,4,5,6]
       ↓
    filter
       ↓
   [2,4,6]
       ↓
    reduce
       ↓
      12
18. Combining filter() + map() + reduce()

Now we can combine all three.

Suppose:

numbers = [1, 2, 3, 4, 5, 6]

We want:

Keep even numbers
Square them
Add them

Expected:

2² + 4² + 6²
= 4 + 16 + 36
= 56

Code:

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]


result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)


print(result)

Output:

56

Pipeline:

Original
[1,2,3,4,5,6]
       ↓
    filter
       ↓
    [2,4,6]
       ↓
     map
       ↓
   [4,16,36]
       ↓
    reduce
       ↓
      56

This is the complete functional-programming pipeline you've been learning.

19. How to read nested map/filter/reduce

When you see:

reduce(
    function,
    map(
        function,
        filter(
            condition,
            data
        )
    )
)

read it from inside → outside:

filter first
     ↓
map second
     ↓
reduce last

This is extremely important when reading code.

20. reduce() with strings

You can also combine strings.

from functools import reduce


words = ["Python", "is", "awesome"]


result = reduce(lambda x, y: x + " " + y, words)


print(result)

Output:

Python is awesome

Process:

Python + is
       ↓
Python is


Python is + awesome
       ↓
Python is awesome
21. reduce() for finding maximum

Although Python already has:

max(numbers)

you can understand how reduction works by implementing it:

from functools import reduce


numbers = [10, 25, 7, 40, 15]


maximum = reduce(
    lambda x, y: x if x > y else y,
    numbers
)


print(maximum)

Output:

40

This is a good learning example because you're repeatedly reducing two values into one.

22. reduce() and data types

The accumulator doesn't necessarily have to remain the same type.

For example, you could technically construct more complex results, but for now focus on operations where the accumulator and elements interact predictably:

number + number
number × number
string + string
comparison → selected value

That's enough for your current Python level.

23. Important concept: reduction doesn't necessarily mean arithmetic

This is a common misconception.

reduce() doesn't mean:

"Do mathematical calculations."

It means:

Repeatedly combine values using a function until one result remains.

Addition is just one example.

You can:

add
multiply
find maximum
find minimum
concatenate
combine objects

etc.

24. When NOT to use reduce()

Don't force reduce() into every problem.

For example:

sum(numbers)

is clearer than:

reduce(lambda x, y: x + y, numbers)

Similarly:

max(numbers)

is clearer than manually reducing to the maximum.

Use reduce() when it makes the combination logic useful or when you're learning functional programming.

25. Common mistakes
Mistake 1 — Forgetting the import

Wrong:

reduce(lambda x, y: x + y, numbers)

Correct:

from functools import reduce
Mistake 2 — Using one parameter

Wrong:

reduce(lambda x: x + 1, numbers)

Normally reduce() needs a function that combines two values:

lambda x, y: x + y
Mistake 3 — Confusing reduce() with map()
map()

creates a transformed value for each element.

reduce()

keeps combining until there is one final result.

🧠 The complete mental map
             FUNCTIONAL TOOLS
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
     map()       filter()     reduce()
       │            │            │
   TRANSFORM      SELECT       COMBINE
       │            │            │
   Many → Many   Many → Fewer  Many → One
Example
numbers
[1,2,3,4,5,6]
       │
       ▼
    filter()
       │
       ▼
    [2,4,6]
       │
       ▼
     map()
       │
       ▼
   [4,16,36]
       │
       ▼
    reduce()
       │
       ▼
      56


"""