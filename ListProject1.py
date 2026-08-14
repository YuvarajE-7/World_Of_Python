"""
🧑‍🎓 Project: Student Marks Manager

We're going to build a console-based Python application for managing students and their marks.

For now, we'll intentionally use only the concepts you've learned. As you learn more Python concepts, we can improve the project.

1. Data Structure

Start with:

students = [
    ["Arun", [80, 75, 90]],
    ["Rahul", [60, 85, 70]],
    ["Priya", [95, 88, 92]]
]

Each student is:

[name, marks]

For example:

["Arun", [80, 75, 90]]
2. Main Menu

Your program should repeatedly show:

===== STUDENT MARKS MANAGER =====


1. Add student
2. View all students
3. Search student
4. Add marks
5. Update marks
6. Remove student
7. Calculate student total
8. Calculate student average
9. Find highest scorer
10. Find lowest scorer
11. Count students
12. Exit

The user chooses an option.

3. Add Student

Ask for:

Enter student name:

Then create a student with an empty marks list.

For example:

Enter student name: Kiran


Student added successfully.

The data should become:

students = [
    ["Arun", [80, 75, 90]],
    ["Rahul", [60, 85, 70]],
    ["Priya", [95, 88, 92]],
    ["Kiran", []]
]

Concepts: lists, append().

4. View All Students

Display every student.

Example:

===== STUDENTS =====


Arun   [80, 75, 90]
Rahul  [60, 85, 70]
Priya  [95, 88, 92]
Kiran  []

Concepts: nested lists, loops, indexing.

5. Search Student

Ask:

Enter student name:

If found:

Student found
Name: Rahul
Marks: [60, 85, 70]

If not:

Student not found.

Concepts: loops, conditions, strings, ==.

6. Add Marks

Ask:

Enter student name:
Enter mark:

Example:

Enter student name: Kiran
Enter mark: 85


Mark added.

If Kiran had:

["Kiran", []]

it becomes:

["Kiran", [85]]

If you add another:

Enter mark: 90

it becomes:

["Kiran", [85, 90]]

Concepts: nested lists, append().

7. Update Marks

Ask:

Enter student name:
Enter mark position:
Enter new mark:

Example:

Rahul
Position: 1
New mark: 75

Before:

["Rahul", [60, 85, 70]]

After:

["Rahul", [60, 75, 70]]

Concepts: indexing + updating.

8. Remove Student

Ask:

Enter student name:

Example:

Enter student name: Rahul


Rahul removed successfully.

The entire nested list should be removed.

Concepts: remove(), loops, conditions.

9. Calculate Student Total

Ask:

Enter student name:

Example:

Student: Arun
Marks: [80, 75, 90]


Total: 245

You must calculate it using a loop.

Don't use:

sum()

yet.

Concepts: nested lists, loops, accumulation.

10. Calculate Average

Ask:

Enter student name:

Example:

Student: Arun
Total: 245
Average: 81.67

You'll need:

total / number of marks

Concepts: loops, len(), arithmetic.

11. Find Highest Scorer

Look through all students and determine who has the highest total.

Example:

===== HIGHEST SCORER =====


Name: Priya
Marks: [95, 88, 92]
Total: 275

Don't use max().

You'll need the pattern you just learned:

largest value
+
student associated with that value

This is an important problem.

12. Find Lowest Scorer

Same idea, but find the student with the lowest total.

Example:

===== LOWEST SCORER =====


Name: Rahul
Marks: [60, 85, 70]
Total: 215

Don't use min().


 Exit

Option 12 should display:

Thank you for using Student Marks Manager!

and terminate the program.

Final Program Flow

The finished application should behave roughly like:

===== STUDENT MARKS MANAGER =====


1. Add student
2. View all students
3. Search student
4. Add marks
5. Update marks
6. Remove student
7. Student total
8. Student average
9. Highest scorer
10. Lowest scorer
11. Count students
12. Exit


Enter choice: 1


Enter student name: Kiran


Student added successfully.


===== STUDENT MARKS MANAGER =====


Enter choice: 4


Enter student name: Kiran
Enter mark: 85


Mark added.

Then the menu appears again.

"""



students = [
    ["Arun", [80, 75, 90]],
    ["Rahul", [60, 85, 70]],
    ["Priya", [95, 88, 92]],
    ["Kiran", [72, 68, 80]],
    ["Anjali", [85, 91, 78]],
    ["Vijay", [55, 64, 70]],
    ["Sneha", [90, 82, 89]],
    ["Rohit", [76, 73, 81]],
    ["Divya", [88, 95, 91]],
    ["Suresh", [67, 72, 65]],
    ["Meena", [92, 86, 94]],
    ["Ajay", [58, 61, 69]],
    ["Kavya", [81, 79, 85]],
    ["Naveen", [74, 83, 77]],
    ["Pooja", [89, 90, 87]],
    ["Manoj", [63, 71, 68]],
    ["Swathi", [96, 93, 97]],
    ["Hari", [70, 66, 75]],
    ["Lakshmi", [84, 78, 88]],
    ["Gokul", [62, 80, 73]]
]


print("----------------------------------------------------------------------------------")
print("                           Student Marks Manager                                                    ")
print("----------------------------------------------------------------------------------")
while (True):
    print("1. Add student \n2. View all students \n3. Search student \n4. Add marks \n5. Update marks \n6. Remove student \n7. Calculate student total \n8. Calculate student average \n9. Find highest scorer \n10. Find lowest scorer \n11. Exit")
    menu_choice = int(input("Enter Your Choice : "))

    if menu_choice == 1:
        Student_name = input("Enter Your Name : ")
        new_list = [Student_name ,[]]
        students.append(new_list)
        
    elif menu_choice == 2:
        for name , marks in students:
            print(name,marks)

    elif menu_choice == 3:
         to_find_student_name = input("Enter Students Name : ")
         for student in students:
             if student[0] == to_find_student_name:
                 print("Student Found")
                 print(student[0])
                 print(student[1])
    elif menu_choice == 4:
        to_add_mark_student_name = input("Enter Students Name : ")
        to_add_mark_student_mark = int(input("Enter Student mark :"))
        for student in students:
              if student[0] == to_add_mark_student_name:
                    student[1].append(to_add_mark_student_mark)

    elif menu_choice == 5:
        to_update_mark_student_name = input("Enter Students Name : ")
        to_update_mark_position = int(input("Enter the Position to update:"))
        to_update_mark_student_mark = int(input("Enter Student mark :"))
        for student in students:
                      if student[0] == to_update_mark_student_name:
                           student[1][to_update_mark_position] = to_update_mark_student_mark
                           
    elif menu_choice == 6:
        to_remove_student_name = input("Enter Student name : ")
        for student in students:
                if student[0] == to_remove_student_name:
                     students.remove(student)
                     print("Remove Successfully")

    elif menu_choice == 7:
        to_find_total_student_name = input("Enter Student name : ")
        sum = 0
        for student in students:
             if student[0] == to_find_total_student_name:
                  for i in student[1]:
                       sum += i
        print(f"Total mark of {to_find_total_student_name} is {sum}")
             
    elif menu_choice == 8:
         to_find_average_student_name = input("Enter Student name : ")
         sum = 0
         for student in students:
                if student[0] == to_find_total_student_name:
                        for i in student[1]:
                            sum += i
                            avg = sum/3
         print(f"Average of {to_find_total_student_name} is {avg}")
    elif menu_choice == 9:
        Highest = 0
        Highest_mark_student = ""
        for student in students:
             sum = 0
             for mark in student[1]:
                  sum += mark
                  if sum > Highest:
                       Highest = sum 
                       Highest_mark_student = student[0]
        print(Highest)
        print(Highest_mark_student)          
                  
    elif menu_choice == 10:
          low = None
          low_mark_student = ""
          for student in students:
                      sum = 0
                      for mark in student[1]:
                           sum += mark
                      if low is None or sum < low:
                                low = sum 
                                low_mark_student = student[0]
          print(low)
          print(low_mark_student)  
        
    elif menu_choice == 12:
        exit()
