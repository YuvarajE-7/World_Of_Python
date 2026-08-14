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


"""
10 .Updating Elements in a List

This is straightforward because lists are mutable.

We use indexing to select the element we want to change.

numbers = [10, 20, 30, 40, 50]

Suppose we want to change 30 to 300.

30 is at index 2:

numbers[2] = 300

Now:

print(numbers)

Output:

[10, 20, 300, 40, 50]
You can also use negative indexing
numbers[-1] = 500

Now:

[10, 20, 300, 40, 500]
You can update multiple elements using slicing

For example:

numbers = [10, 20, 30, 40, 50]


numbers[1:3] = [200, 300]


print(numbers)

Output:

[10, 200, 300, 40, 50]

Here:

numbers[1:3]

selects:

20, 30

and we replace them with:

200, 300

"""

"""
11. Adding Element to the List

There are 3 methods you need to know:

append()
insert()
extend()

Let's take them one at a time.

1. append()

append() adds one element to the end of the list.

numbers = [10, 20, 30]


numbers.append(40)


print(numbers)

Output:

[10, 20, 30, 40]

Think:

Before: [10, 20, 30]


append(40)


After:  [10, 20, 30, 40]
                         ↑
                      added
Important

Even if you append multiple values together:

numbers.append([40, 50])

you are adding one element:

[10, 20, 30, [40, 50]]

This is different from extend(), which we'll see next.

2. insert()

insert() lets you add an element at a specific position.

Syntax:

list.insert(index, value)

Example:

numbers = [10, 20, 30]


numbers.insert(1, 100)


print(numbers)

Output:

[10, 100, 20, 30]

We said:

numbers.insert(1, 100)

So Python puts 100 at index 1.

The existing elements shift to the right.

Before:


index:   0    1    2
        10   20   30


After:


index:   0    1    2    3
        10  100   20   30
             ↑
          inserted
3. extend()

extend() adds multiple elements to the end of a list.

numbers = [10, 20, 30]


numbers.extend([40, 50, 60])


print(numbers)

Output:

[10, 20, 30, 40, 50, 60]

Think of it as joining the elements of another list onto the first list.

The important difference
numbers.append([40, 50])

gives:

[10, 20, 30, [40, 50]]

But:

numbers.extend([40, 50])

gives:

[10, 20, 30, 40, 50]

That's one of the most important differences between append() and extend().

Simple rule
Method	What it does
append(x)	Add one element at the end
insert(i, x)	Add one element at a specific position
extend(x)	Add multiple elements

"""

"""
12 .Removing Elements 
We have four things:

remove()
pop()
del
clear()

They all remove things, but they work differently.

1. remove()

remove() removes an element by its value.

numbers = [10, 20, 30, 40]


numbers.remove(30)


print(numbers)

Output:

[10, 20, 40]

You tell Python what value to remove.

numbers.remove(30)
               ↑
             value
If the value doesn't exist?
numbers.remove(100)

You'll get:

ValueError

We'll discuss this more when we learn error handling.

2. pop()

pop() removes an element by its index.

numbers = [10, 20, 30, 40]


numbers.pop(2)


print(numbers)

Output:

[10, 20, 40]

Because index 2 contains 30.

Special thing about pop()

pop() returns the removed element.

numbers = [10, 20, 30, 40]


x = numbers.pop(2)


print(x)
print(numbers)

Output:

30
[10, 20, 40]

This is useful when you actually want to use the removed value.

pop() without an index
numbers.pop()

removes the last element.

numbers = [10, 20, 30, 40]


numbers.pop()


print(numbers)

Output:

[10, 20, 30]



3. del

del can remove an element using its index.

numbers = [10, 20, 30, 40]


del numbers[2]


print(numbers)

Output:

[10, 20, 40]

You can also delete a range using slicing:

numbers = [10, 20, 30, 40, 50]


del numbers[1:4]


print(numbers)

Output:

[10, 50]

So del is more flexible than just removing one element.




4. clear()

clear() removes everything from the list.

numbers = [10, 20, 30, 40]


numbers.clear()


print(numbers)

Output:

[]

The list still exists. It's just empty.

The important difference
Method	Removes using	Example
remove()	value	numbers.remove(30)
pop()	index	numbers.pop(2)
del	index / slice	del numbers[2]
clear()	everything	numbers.clear()
One extra difference

pop() gives you the removed value:

x = numbers.pop(2)

while:

numbers.remove(30)
del numbers[2]

don't give you the removed element.


One more important thing about remove()

If duplicates exist:

numbers = [10, 20, 30, 30, 40]


numbers.remove(30)


print(numbers)

Result:

[10, 20, 30, 40]

It removes the first matching 30.

"""


"""
13. Searching

We have two things:

in
index()

They answer slightly different questions.

1. in

in checks whether a value exists in the list.

numbers = [10, 20, 30, 40, 50]


print(30 in numbers)

Output:

True

Because 30 exists.

print(100 in numbers)

Output:

False
Very useful with if
numbers = [10, 20, 30, 40, 50]


if 30 in numbers:
    print("30 is present")

Output:

30 is present

You can also use not in:

if 100 not in numbers:
    print("100 is not present")
2. index()

index() tells you where a value is located.

numbers = [10, 20, 30, 40, 50]


print(numbers.index(30))

Output:

2

Because:

Value:  10   20   30   40   50
Index:   0    1    2    3    4
                  ↑
in vs index()

This is the key difference:

30 in numbers

asks:

Does 30 exist?

Answer:

True

While:

numbers.index(30)

asks:

Where is 30?

Answer:

2

What if the value doesn't exist?
numbers.index(100)

This produces:

ValueError

So if you're not sure whether something exists, you can first check:

if 100 in numbers:
    print(numbers.index(100))


##########################################
    And yes, if:

numbers = [10, 20, 30, 40, 30, 50]

then:

numbers.index(30)

→ 2

It doesn't return 4, even though another 30 is there.

"""

"""
14.Counting

count() tells you how many times a value appears.

numbers = [10, 20, 30, 30, 40, 30]


print(numbers.count(30))

Output:

3

So:

numbers.count(30)

means:

"How many times does 30 occur in this list?"


###################################
Also

numbers = [10, 20, 30, 30, 40, 30, 50]

numbers.count(100)

does not give an error.

It gives:

0

Because count() simply asks:

"How many times does 100 occur?"

Since it doesn't occur:

0 times



Compare this with index():

numbers.index(100)

→ ValueError

because index() needs to find a position.

But:

numbers.count(100)

→ 0

because zero occurrences is a perfectly valid answer.

Mental model
in       → Does it exist?       → True / False


index()  → Where is it?         → index


count()  → How many times?      → number


"""



"""
15. Sorting List

We have four things:

sort()
sorted()
reverse()
reversed()

Let's not mix them up. We'll start with sort().

1. sort()

sort() sorts the original list.

numbers = [40, 10, 30, 20, 50]


numbers.sort()


print(numbers)

Output:

[10, 20, 30, 40, 50]

Notice something important:

numbers.sort()

changes numbers itself.

Before:

[40, 10, 30, 20, 50]

After:

[10, 20, 30, 40, 50]
Descending order

You can use:

numbers.sort(reverse=True)

Example:

numbers = [40, 10, 30, 20, 50]


numbers.sort(reverse=True)


print(numbers)

Output:

[50, 40, 30, 20, 10]
2. sorted()

sorted() is different.

It creates and returns a new sorted list.

numbers = [40, 10, 30, 20, 50]


new_numbers = sorted(numbers)


print(new_numbers)
print(numbers)

Output:

[10, 20, 30, 40, 50]
[40, 10, 30, 20, 50]

Notice:

sort()    → changes original list
sorted()  → leaves original list unchanged

That's the main difference.

Think about it this way
numbers.sort()

means:

"Sort this list."

While:

new_numbers = sorted(numbers)

means:

"Give me a sorted version of this list."

Quick comparison
sort()                 sorted()
  ↓                       ↓
changes original       creates new list

Example:

numbers = [30, 10, 20]


numbers.sort()


# numbers → [10, 20, 30]

versus:

numbers = [30, 10, 20]


result = sorted(numbers)


# numbers → [30, 10, 20]
# result  → [10, 20, 30]
Now let's understand reverse()

Don't confuse reverse with sorting descending.

numbers = [10, 20, 30, 40, 50]


numbers.reverse()


print(numbers)

Output:

[50, 40, 30, 20, 10]

reverse() simply reverses the current order.

It doesn't sort.

For example:

numbers = [30, 10, 50, 20]


numbers.reverse()


print(numbers)

Output:

[20, 50, 10, 30]

It simply went:

30  10  50  20
 ↓   ↓   ↓   ↓
20  50  10  30

It did not become:

[50, 30, 20, 10]
reversed()

reversed() gives you a reversed iterator rather than directly changing the list.

For now, the important difference is:

numbers.reverse()

→ changes the original list.

reversed(numbers)

→ does not change the original list.

If you want a new list:

numbers = [10, 20, 30]


result = list(reversed(numbers))


print(result)

Output:

[30, 20, 10]

Your mental model
Operation	Changes original?	Result
sort()	     Yes	sorted list
sorted()	 No    new sorted list
reverse()	 Yes	reversed list
reversed()	 No	    reversed iterator


"""





"""
16. Copying List


There are three things to understand first:

Assignment
copy()
list()

Then we'll understand shallow copy.

1. Assignment is NOT copying

Suppose:

numbers = [10, 20, 30]

Now:

new_numbers = numbers

You might think:

"I created another list."

But you didn't.

Both variables refer to the same list.

numbers ──────┐
              ↓
         [10, 20, 30]
              ↑
              │
new_numbers ──┘

So:

numbers = [10, 20, 30]


new_numbers = numbers


new_numbers[0] = 100


print(numbers)
print(new_numbers)

Output:

[100, 20, 30]
[100, 20, 30]

 Why did numbers change?

Because there is still only one list.

numbers and new_numbers are just two names referring to it.

2. copy()

If you actually want a separate list:

numbers = [10, 20, 30]


new_numbers = numbers.copy()

Now there are two lists:

numbers      → [10, 20, 30]


new_numbers  → [10, 20, 30]

Changing one doesn't change the other:

new_numbers[0] = 100


print(numbers)
print(new_numbers)

Output:

[10, 20, 30]
[100, 20, 30]

That's an actual copy.

3. list()

You can also create a copy using:

numbers = [10, 20, 30]


new_numbers = list(numbers)

Now:

new_numbers[0] = 100


print(numbers)
print(new_numbers)

Output:

[10, 20, 30]
[100, 20, 30]

So for a simple list:

numbers.copy()

and

list(numbers)

both create a new list.

The important difference
Assignment
new = old

 Doesn't create a new list.

copy()
new = old.copy()

 Creates a new list.

list()
new = list(old)

 Creates a new list.


"""

"""
17. Shallow Copy

Start simple
numbers = [10, 20, 30]

Think:

numbers ─────→ [10, 20, 30]

When you do:

new_numbers = numbers

Python doesn't create another list.

numbers ───────┐
               ↓
          [10, 20, 30]
               ↑
new_numbers ───┘

That's why changing one changes the other.

Now copy()
new_numbers = numbers.copy()

Python creates a new outer list:

numbers ───────→ [10, 20, 30]


new_numbers ──→ [10, 20, 30]

Two different lists. 

Now the interesting part

Suppose:

numbers = [[1, 2], [3, 4]]

Think of it as:

numbers
   ↓
┌───────────────┐
│      ●        │────→ [1, 2]
│      ●        │────→ [3, 4]
└───────────────┘

Then:

new_numbers = numbers.copy()

Python copies the outer container, but it doesn't recursively copy everything inside it.

So:

numbers
   ↓
┌───────────────┐
│      ●──────────────→ [1, 2]
│      ●──────────────→ [3, 4]
└───────────────┘


new_numbers
   ↓
┌───────────────┐
│      ●──────────────→ [1, 2]
│      ●──────────────→ [3, 4]
└───────────────┘

Notice:

Two outer lists
but
the same inner lists.

That's why:

new_numbers[0].append(100)

changes the shared inner list.

Why does Python work this way?

Because copying everything recursively can be expensive and unnecessary.

Imagine:

company = [
    [1000 employees],
    [500 projects],
    [200 departments],
    [many other objects...]
]

If Python automatically copied everything inside everything, a simple .copy() could potentially duplicate a huge amount of data.

Instead, a shallow copy says:

"Give me a new outer container, but keep references to the existing objects inside."


If you have a list containing other lists:

numbers = [[1, 2], [3, 4]]

and make a shallow copy:

new_numbers = numbers.copy()

then:

The outer lists are separate 
The inner lists are shared 

So if you change an inner list, both appear to change:

new_numbers[0].append(100)


print(numbers)
print(new_numbers)

Both become:

[[1, 2, 100], [3, 4]]
But this is important:

If you change the outer list itself, they don't affect each other.

new_numbers.append([5, 6])

Now:

numbers
→ [[1, 2], [3, 4]]


new_numbers
→ [[1, 2], [3, 4], [5, 6]]

So remember:

Shallow copy = outer list is copied, inner objects are shared.

"""


"""
18. Combining Lists

You have two things in your syllabus:

+
extend()

You already learned extend(), so this should be quick.

+

+ creates a new list by combining two lists.

a = [10, 20]
b = [30, 40]


c = a + b


print(c)

Output:

[10, 20, 30, 40]

Importantly, a and b remain unchanged.

a → [10, 20]
b → [30, 40]
c → [10, 20, 30, 40]

Compare that with extend():

a = [10, 20]
b = [30, 40]


a.extend(b)

Now:

a → [10, 20, 30, 40]
b → [30, 40]

So the key difference:

a + b
→ creates a new combined list


a.extend(b)
→ modifies a


"""







"""
19. List Unpacking

You have:

numbers = [10, 20, 30]

Normally, you access elements using indexes:

numbers[0]  # 10
numbers[1]  # 20
numbers[2]  # 30

But unpacking lets you take the elements out into separate variables:

a, b, c = numbers

Now:

a → 10
b → 20
c → 30

So:

print(a)
print(b)
print(c)

gives:

10
20
30
The important rule

The number of variables should normally match the number of elements.

This works:

numbers = [10, 20, 30]


a, b, c = numbers

But this doesn't:

a, b = numbers

because Python has:

3 values
2 variables

So you'll get:

ValueError



⭐ Extended unpacking

Python also allows *.

numbers = [10, 20, 30, 40, 50]


a, *b = numbers

Now:

a → 10
b → [20, 30, 40, 50]

The *b says:

"Put all the remaining elements into b."

Another example:

a, b, *c = numbers

Gives:

a → 10
b → 20
c → [30, 40, 50]

And:

*a, b = numbers

Gives:

a → [10, 20, 30, 40]
b → 50
Don't overthink * yet

The basic idea is:

a, b, c = [10, 20, 30]

→ each value goes into one variable.

And:

a, *b = [10, 20, 30, 40]

→ a gets the first, b gets the remaining values as a list.

"""