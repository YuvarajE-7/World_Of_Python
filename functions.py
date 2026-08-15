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

