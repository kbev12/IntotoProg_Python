# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# kbeverly,8.9.2022,Added code to complete assignment 5
# kbeverly, 8.10.2022, Updated print in option 1
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None
strFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionary rows (like Lab 5-2)
try:
    objFile = open(strFile, "r")
    for row in objFile:
        FirstRow = row.split(",")
        dicRow = {"Task": FirstRow[0], "Priority": FirstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    print(strFile + ' was not found')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Task' + '|' + 'Priority')
        print('-'*15)
        for row in lstTable:
            print(row['Task'] + '|' + str(row['Priority']))

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        str_task = str(input("Enter a task: "))
        str_priority = str(input("Enter the task's priority: "))
        dicRow = {"Task": str_task, "Priority": str_priority}
        lstTable.append(dicRow)

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        str_remove = str(input("Enter a task to remove: "))
        for row in lstTable:
            if row['Task'].lower() == str_remove.lower():
                lstTable.remove(row)
                print('Task has been removed: ' + str_remove)

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        obj_file = open(strFile, "w")
        for row in lstTable:
            obj_file.write(str(row['Task']) + ',' + str(row['Priority']) + "\n")
        obj_file.close()
        print("Date was saved!")

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Thank you, goodbye...')
        break  # and Exit the program
