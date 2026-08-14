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



"""
6.Indexing

Indexing is simply accessing an element from a list using its position.

numbers = [10, 20, 30, 40, 50]

Each element has a position:

Value:    10    20    30    40    50
Index:     0     1     2     3     4
Positive indexing

Python starts counting from 0, not 1.

numbers[0]   # 10
numbers[1]   # 20
numbers[2]   # 30

Example:

numbers = [10, 20, 30, 40, 50]


print(numbers[0])
print(numbers[3])

Output:

10
40
Negative indexing

You can also count from the end:

Value:          10    20    30    40    50
Positive:        0     1     2     3     4
Negative:       -5    -4    -3    -2    -1

So:

numbers[-1]   # 50
numbers[-2]   # 40
numbers[-3]   # 30
One important connection

Because lists are mutable, indexing also lets us change an element:

numbers = [10, 20, 30]


numbers[1] = 200


print(numbers)

Output:

[10, 200, 30]

So the basic pattern is:

list[index]


#########################For:

numbers = [10, 20, 30, 40, 50]
Answers
Expression	Result
numbers[0]	10
numbers[3]	40
numbers[-1]	50
numbers[-4]	20
numbers[5]  Error

The last one gives:

IndexError: list index out of range

"""


"""
7.Slicing — list[start:end]

Slicing means taking a portion of a list instead of taking just one element.

Let's use:

numbers = [10, 20, 30, 40, 50]

Remember the indexes:

Value:    10   20   30   40   50
Index:     0    1    2    3    4
1. Basic slicing
numbers[1:4]

Output:

[20, 30, 40]

Why not 50?

Because Python uses:

start → included
end   → excluded

So:

numbers[1:4]
          ↑
       stop before 4

It takes indexes:

1, 2, 3
2. More examples
numbers[0:3]
[10, 20, 30]
numbers[2:5]
[30, 40, 50]
numbers[1:2]
[20]

Notice that slicing returns a list, even if you select only one element.

Compare:

numbers[1]      # 20
numbers[1:2]    # [20]

That's an important difference.

3. Omitting start
numbers[:3]

means:

Start from the beginning and stop before index 3.

Result:

[10, 20, 30]

So:

numbers[:3]

is basically:

numbers[0:3]
4. Omitting end
numbers[2:]

means:

Start at index 2 and go until the end.

Result:

[30, 40, 50]
5. Both omitted
numbers[:]

gives:

[10, 20, 30, 40, 50]

It selects the whole list.

The main rule

Remember this:

list[start:end]


       ↓
start = included
end   = excluded

For example:

numbers[1:4]

means:

1 → 2 → 3

not 4.

"""

"""
8. Slicing with Step Value

Step

Slicing can have three parts:

list[start:end:step]

For example:

numbers = [10, 20, 30, 40, 50, 60]


numbers[0:6:2]

Output:

[10, 30, 50]

Why?

index:   0   1   2   3   4   5
value:  10  20  30  40  50  60
         ↑       ↑       ↑
         0       2       4

step = 2 means:

Take an element, then skip one, take the next.

Another:

numbers[0:6:3]

Output:

[10, 40]

Because it takes indexes:

0 → 3
You can also omit start/end
numbers[::2]

Output:

[10, 30, 50]

This means:

Start from beginning → go to end → take every 2nd element.

"""

"""
9. Reverse Slicing
his is how we do reverse slicing.

numbers = [10, 20, 30, 40, 50, 60]

Try:

numbers[::-1]

Output:

[60, 50, 40, 30, 20, 10]

Why?

The -1 means:

Move backward one position at a time.

You can also do:

numbers[5:1:-1]

Output:

[60, 50, 40, 30]

Remember the same rule:

Start is included, end is excluded.

So indexes:

5 → 4 → 3 → 2

#################
Let's understand exactly what this means:

numbers[5:1:-1]

Suppose:

numbers = [10, 20, 30, 40, 50, 60]

Indexes:

Value:    10   20   30   40   50   60
Index:     0    1    2    3    4    5

Now:

numbers[5:1:-1]

Break it into:

start = 5
end   = 1
step  = -1
Follow the indexes

Because the step is -1, we move backward:

5 → 4 → 3 → 2 → STOP

We do not include index 1.

Therefore:

[60, 50, 40, 30]
Think of it like this
numbers[5:1:-1]
        ↓   ↓  ↓
      start end step


        5 → 4 → 3 → 2
        ↓   ↓   ↓   ↓
       60  50  40  30

So the general rule still remains:

Start is included, end is excluded.

The only difference is that with a negative step, we're moving backward.

"""