"""
1. Lists

They should cover:

What is a list?
Creating lists
Empty lists
Lists with different data types
Mutable nature of lists
Indexing
Positive indexing
Negative indexing
Slicing
list[start:end]
Step
Reverse slicing
Updating elements
Adding elements
append()
insert()
extend()
Removing elements
remove()
pop()
del
clear()
Searching
in
index()
Counting
count()
Sorting
sort()
sorted()
reverse()
reversed()
Copying
Assignment vs copy
copy()
list()
Shallow copy
Combining lists
+
extend()
List unpacking
Iterating through lists
Lists with loops
Lists with conditions
Nested lists
List of lists
List as a stack
append()
pop()
Time complexity of common list operation

"""

"""
1. What is a list?

A list is a Python data structure used to store multiple values in a single variable.

Instead of:

student1 = "Arjun"
student2 = "Rahul"
student3 = "Anu"

we can use:

students = ["Arjun", "Rahul", "Anu"]
Now students contains three values.

A list is written using square brackets [].

students = ["Arjun", "Rahul", "Anu"]

Think of it like a row of containers:

students
   ↓
["Arjun", "Rahul", "Anu"]
    0        1       2

The positions are called indexes. We'll learn indexing properly next.

"""






"""
2. Creating and How to input List?

//Basic Method of creating List

empty_list = []

names =["Sachin","Dhoni","Virat","Rohit","Bumrah"]

jersy_num =[10,7,18,45,93]

avg=[55.7,47.2,59.2,50.5,16.5]

is_bowler = [True,False,False,False,True]

print(names)
print(jersy_num)
print(avg)
print(is_bowler)


// Creating list using list()

nums = list()  # creates empty list 


num = list("Doremon")
print(num)   # output ['D', 'o', 'r', 'e', 'm', 'o', 'n']

"""
"""
# for taking interger inputs

list_as_input = list(map(int,input().split()))
print(list_as_input)

# Output
# 10 20 30 40 50
#[10, 20, 30, 40, 50]

"""

#How it works ?
"""
Understand what is happening

input()

takes:

"10 20 30 40 50"

Then:

.split()

breaks it into:

["10", "20", "30", "40", "50"] 

Then:

map(int, ...)

converts each string to an integer.

Finally:

list(...)

"""

"""
4. Lists can contain different data types


#Python lists don't require every element to have the same type.

data = [10, "Arjun", 3.14, True]

Here:

10       → int
"Arjun"  → str
3.14     → float
True     → bool

#You can even put another list inside a list:

data = [10, "Arjun", [1, 2, 3]]

"""

"""
5. The important property: Lists are mutable

This is one of the most important things to understand.

Mutable means:

We can change the contents of an existing list.

Example:

numbers = [10, 20, 30]


numbers[0] = 100


print(numbers)

Output:

[100, 20, 30]

We didn't create a new list.

We changed the existing list.

Compare:

numbers = [10, 20, 30]


numbers[0] = 100

Before:

[10, 20, 30]

After:

[100, 20, 30]

This mutable nature becomes very important when we learn copying lists later.

"""
