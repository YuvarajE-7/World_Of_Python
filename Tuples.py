"""
Tuples



1. Basics of Tuples
What is a tuple?
Why do we use tuples?
Creating tuples
Empty tuples
Tuples with one element
Tuples with multiple elements
Tuples with different data types
Tuple constructor — tuple()
Tuple packing
Tuple unpacking



2. Immutability
What does immutable mean?
Why tuples are immutable
Trying to update a tuple
Trying to add elements to a tuple
Trying to remove elements from a tuple
Mutable objects inside tuples
Difference between tuple immutability and list mutability



3. Indexing
What is indexing?
Positive indexing
Negative indexing
Accessing individual elements
Index out of range
Using len() with tuples



4. Slicing
What is tuple slicing?
tuple[start:end]
Start omitted
End omitted
Both omitted
Step
tuple[start:end:step]
Reverse slicing
Copying a tuple using slicing



5. Tuple Operations
Concatenating tuples — +
Repeating tuples — *
Membership — in
Not membership — not in
Comparing tuples
Tuple equality
Tuple ordering


6. Tuple Methods
count()
index()

Tuples have far fewer methods than lists because tuples cannot be modified.

7. Built-in Functions with Tuples
len()
min()
max()
sum()
sorted()
any()
all()



8. Iterating Through Tuples
Looping through a tuple
Tuple with for
Tuple with while
Tuple with conditions
Using enumerate() with tuples
Nested loops with tuples
9. Tuple Unpacking — Important
Basic unpacking
Number of variables must match
Unpacking with *
Extended unpacking
Unpacking in loops
Swapping variables using tuples

Example:

a, b, c = (10, 20, 30)



10. Nested Tuples
Tuple inside tuple
Accessing nested tuples
Indexing nested tuples
Slicing nested tuples
Iterating through nested tuples

Example:

data = ((10, 20), (30, 40))


11. Tuple and List Relationship
Converting list → tuple
Converting tuple → list
Why convert between them?
Modifying a tuple indirectly using a list
tuple() and list()

Example:

numbers = (10, 20, 30)


temp = list(numbers)
temp.append(40)


numbers = tuple(temp)



12. Tuple Packing and Unpacking in Real Use
Returning multiple values from functions
Receiving multiple values
Swapping variables
Multiple assignment
Looping through pairs
Using tuples for fixed records

Example:

def get_data():
    return "Arjun", 20


13. Tuples and Functions
Passing a tuple to a function
Returning a tuple from a function
*args and tuples
Tuple as a function argument


14. Tuples and Dictionaries
Tuples as dictionary keys
Dictionary items() returning tuples
Iterating through dictionary key-value pairs
Why tuples can be dictionary keys but lists cannot

Example:

data = {
    (10, 20): "Point A"
}


15. Tuples and Sets
Tuples inside sets
Why tuples can be set elements
Lists vs tuples as set elements



16. Practical Uses
Coordinates
point = (10, 20)
RGB values
red = (255, 0, 0)
Student records
Returning multiple values
Fixed configuration data
Representing fixed collections


17. Tuple vs List
Tuple vs list
Mutable vs immutable
Methods available
Performance differences
Memory considerations
When to use a tuple
When to use a list
18. Important Concepts / Common Mistakes
The comma creates a tuple
One-element tuple
x = (10,)    # tuple
x = (10)     # integer
Parentheses are sometimes optional
Tuple assignment
Attempting to modify tuples
Mutable elements inside tuples
Index errors
Unpacking errors


19. Time Complexity
Accessing an element
Searching with in
index()
count()
Iteration
Concatenation
Comparing tuples

"""


"""
1. Tuple Basics



1.1 What is a Tuple?

A tuple is a collection of multiple values stored together in a single variable.

Example:

numbers = (10, 20, 30, 40)

Here:

numbers → variable name
(10, 20, 30, 40) → tuple
10, 20, 30, 40 → elements of the tuple

You can think of a tuple as similar to a list, but with one major difference:

A tuple is immutable, meaning we cannot directly change its elements after creating it.

Example:

numbers = (10, 20, 30)


print(numbers)

Output:

(10, 20, 30)


1.2 Why Do We Use Tuples?

We use tuples when we have a collection of values that should not be changed.

For example, suppose we have the coordinates of a point:

point = (10, 20)

Usually, we want (10, 20) to represent one fixed point.

Another example:

rgb = (255, 0, 0)

This represents a red color.

Another example:

days = ("Monday", "Tuesday", "Wednesday")

If these values are intended to remain fixed, a tuple is useful.

Simple idea

List → data that may change

marks = [80, 90, 75]

Tuple → data that should remain fixed

coordinates = (10, 20)

We'll study the difference between lists and tuples in detail later.



1.3 Creating a Tuple

The most common way is to use parentheses ().

numbers = (10, 20, 30)

Another example:

names = ("Arun", "Rahul", "Kiran")

Another:

fruits = ("apple", "banana", "mango")

The values inside the parentheses are called elements.



1.4 Empty Tuple

An empty tuple contains zero elements.

numbers = ()

Now:

print(numbers)

Output:

()

We can check its type:

numbers = ()


print(type(numbers))

Output:

<class 'tuple'>

So:

()

is an empty tuple.

1.5 Tuple With One Element

This is very important.

Suppose you write:

x = (10)

You might think this is a tuple.

It is not.

x = (10)


print(type(x))

Output:

<class 'int'>

Why?

Because parentheses by themselves don't create a tuple.

To create a one-element tuple, we need a comma.
x = (10,)


print(type(x))

Output:

<class 'tuple'>

So remember:

(10)     # integer
(10,)    # tuple
The comma is important.

You can even write:

x = 10,


print(x)

Output:

(10,)

This is also a tuple.



1.6 Tuple With Multiple Elements

For multiple elements, separate them using commas.

numbers = (10, 20, 30, 40)

We can have any number of elements:

numbers = (10, 20)
numbers = (10, 20, 30, 40, 50)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



1.7 Tuples Can Store Different Data Types

A tuple doesn't have to contain only numbers.

It can contain different Python data types.

data = (10, "Arjun", 3.14, True)

Here:

Element	Data type
10	int
"Arjun"	str
3.14	float
True	bool

So tuples can contain:

integers
floats
strings
booleans
lists
other tuples
dictionaries
etc.

Example:

data = (10, "hello", 3.14, True, [1, 2, 3])

This is perfectly valid.




1.8 Tuple Can Contain Another Tuple

A tuple can contain another tuple.

This is called a nested tuple.

data = ((10, 20), (30, 40))

Here:

data
 ├── (10, 20)
 └── (30, 40)

We'll study nested tuples separately later.



1.9 Creating a Tuple Using tuple()

Python also provides a built-in function called tuple().

Example:

numbers = tuple([10, 20, 30])


print(numbers)

Output:

(10, 20, 30)

Here we started with a list:

[10, 20, 30]

and converted it into:

(10, 20, 30)

We can also create an empty tuple:

numbers = tuple()


print(numbers)

Output:

()

We'll study conversions between lists and tuples later.



1.10 Checking Whether Something Is a Tuple

Use type():

numbers = (10, 20, 30)


print(type(numbers))

Output:

<class 'tuple'>

You can also use isinstance():

numbers = (10, 20, 30)


print(isinstance(numbers, tuple))

Output:

True

For now, type() is enough.

1.11 Important: Parentheses Are Not Always Required

Python allows us to create a tuple without explicitly writing parentheses.

numbers = 10, 20, 30

This is still a tuple.

print(numbers)
print(type(numbers))

Output:

(10, 20, 30)
<class 'tuple'>

Why?

Because the commas create the tuple.

For example:

x = 10, 20

is a tuple.

x = (10, 20)

is also a tuple.

So remember:

The comma is what really matters for tuple creation.

This becomes especially important with the one-element tuple:

x = (10,)


1.12 Tuple vs List — Basic Difference

You already learned lists, so connect the two concepts.

List
numbers = [10, 20, 30]

Uses:

[ ]

Lists are mutable.

Tuple
numbers = (10, 20, 30)

Uses:

( )

Tuples are immutable.

We'll study exactly what mutable and immutable mean in the next major topic.

#############################


 Most important points to remember



x = ()          # empty tuple


x = (10,)       # one-element tuple


x = (10, 20, 30)  # multiple elements


x = 10, 20, 30    # also a tuple


x = (10)        # NOT a tuple

The comma is the key to tuple creation.


Also 

Tuple Packing

For example:

numbers = 10, 20, 30

Python automatically packs these values into a tuple:

(10, 20, 30)

10. Tuple Unpacking

The opposite process:

numbers = (10, 20, 30)


a, b, c = numbers

Now:

a → 10
b → 20
c → 30

"""


