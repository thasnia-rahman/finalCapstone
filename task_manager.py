('''Capstone project: Task 21 Compulsory task 1.
This program is for a small business that can
help it to manage tasks assigned to each member of the team.\n''')

# ====Login Section====

#Stores usernames and passwords
usernames = {}
passwords = {}

#Reads the usernames and passwords from the user.txt file.
with open('user.txt', 'r') as f:
    for line in f:

#Manipulates the data and adds to dictionaries.
        line = line.replace(',', '').split()
        usernames[line[1]] = line[0]
        passwords[line[0]] = line[1]
while True:

#Validates if the user name and password is registered.
    username = input('Please enter your username: \n').lower()
    password = input('Please enter your password: \n').lower()
    if username not in passwords or password not in usernames:
        print('You have entered a username or password that is not registered !')
    continue 
    elif username == usernames[password] and password == passwords[username]:
    break
    elif username == usernames[password] or password != passwords[username]:
        print('You have entered an invalid username or password !')
    continue

while True:
# Validate if the user is authorized to register user's.
    if username == 'admin' and password == 'adm1n':
# Present the 'admin' only menu to the user.
        menu = input('''Select one of the following Options below
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        gr - generate reports
        ds - display statistics
        e - Exit
        : ''').lower()
        
    def displayMenu_Admin():
        global menu_input
        menu_input = input("""
        Please enter one of the following options:
        r - register user
        a - add task
        va- view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit
        """)

    if menu_input == "r":
        register()
    elif menu_input == "a":
        add_task()
    elif menu_input == "va":
        view_all()
    elif menu_input == "vm":
        view_more()
    elif menu_input == "gr":
        reports()
    elif menu_input == "ds":
        statistics() 
    elif menu_input == "e":
        exit()
    return menu_input
    
else:
#Presents the other menu to the user's.
    menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    : ''').lower()

#Registers new user's.
    if menu == 'r' and username == 'admin' and password == 'adm1n':

#Adds new user and password
        new_username = input('Please enter your username: \n').lower()
        new_password = input('Please enter your password: \n').lower()
        password_confirm = input('Please confirm your password: \n').lower()


#Modifies the reg_user to avoid duplicating usernames when a new user is added to user.txt.
    def reg_user():
        if username == "admin":
            new_userLogin = False
            new_usersName = input("Enter username: ")
            register = open("user.txt", "r+")
            
            while new_userLogin == False:
                 for names in text:
                    v_user, v_password = map(str.strip, lines.split(", "))
                    if new_usersName != v_user:
                        v_user, v_password = map(str.strip, lines.split(", "))
                        new_userPass = input("Enter password: ")
                        validate = input("Confirm password: ")
        elif new_usersName == v_user:
            print("That username is unavailable. Pick another one")
            new_usersName = input("Enter username: ")
            new_userPass = input("Enter password: ")
            validate = input("Confirm password: ")
            if new_userPass == validate:
                new_userLogin = True
            if new_userPass != validate:
                print("password did not match. Try again")
            if new_userPass == validate:
                print("password matches. New user created")
                append_me = open("user.txt", "a")
                append_me.write("\n" + str(new_usersName) + ", " + str(validate))
                append_me.close()
            
            if username != "admin":
                print("Only admin can add a new user.")
            if choices == "r":
                register = reg_user()
                print(register)

#Validates new password
    if new_password != password_confirm:
        print('You have entered an invalid password !')
    elif new_password == password_confirm:

# Adds new username and password to the user.txt file
    with open('user.txt', 'a') as f:
        f.write(f'{new_username}, {new_password}\n')
        print('\nUsername and password successfully registered.\n')

#Views tasks and user's statistics 'admin only'
    elif menu == 's' and username == 'admin' and password == 'adm1n':

#Reads all the task from the task.txt file
    with open('tasks.txt', 'r') as ff:
#Gets the number of tasks in the task.txt file
        total_tasks = len(ff.readlines())

#Reads all the user's from the user.txt file.
    with open('user.txt', 'r') as f:
#Gets the number of user's in the user.txt file.
        total_users = len(f.readlines())
        print(f'''

Total number of tasks added is {total_tasks}\n
Total number of user's registered is {total_users}\n''')

#Gets the task information
    elif menu == 'a':
        assignee = input('Enter the username of the user assigned to the task: \n').lower()

#Gets the title of a task.
task = input('Enter the title of the task: \n')

#Gets the description of the task.
description = input('Enter the description of the task: \n')

#Gets the due date of the task.
due_date = input('Enter the task due date eg.(DD/MM/YYYY): \n')

#Gets the current date of the task.
date = input('Enter date task assigned: \n')

#Includes the 'No' to indicate if the task is complete.
completed = input('Task Completed (Yes/No): \n')

#Adds the data to the file task.txt as a.
with open('tasks.txt', 'a') as ff:
    ff.write(f'{assignee}, {task}, {completed}, {due_date}, {date}, {description} \n')
    print('\nTask added successfully\n.')

#View all the saved tasks.
elif menu == 'va':

#Reads the data from tasks.txt file.
with open('tasks.txt', 'r') as ff:
    for line in ff:
#Splits the line with the comma and space
        line = line.split(',' + ' ')
#Prints out in an easier to read format.     
        print(f'''
        Task: {line[1]}
        Assign to: {line[0]}
        Date assinged: {line[4]}
        Due date: {line[3]}
        Task Completed? {line[2]}
        Task description: {line[5]}''')

#Views specific's user's task information
elif menu == 'vm':

#Reads the task data from tasks.txt file.
with open('tasks.txt', 'r') as ff:
    for line in ff:
#Splits the line with the comma and space.
        line = line.split(',' + ' ')

#Validates if logged username is in user.txt file
if username in line[0]:
# Print out in an easier to read format
    print(f'''
    Task: {line[1]}
    Assign to: {line[0]}
    Date assinged: {line[4]}
    Due date: {line[3]}
    Task Completed? {line[2]}
    Task description: {line[5]}''')

elif menu == 'gr':
 #Generates the task overview text file.
    def generate_task_overview():
        task_dictionary = task_dict()
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0

    with open('tasks.txt', 'w', encoding='utf-8') as tasks:
        for count in task_dictionary:
            tasks = task_dictionary[count]
            if 'Yes' == task['task_complete']:
                completed_tasks += 1
            elif 'No' == tasks['task_complete']:
                uncompleted_tasks += 1

# Comparing the dates to check if the task is overdue.
    datetime_object = datetime.strptime(task['date_due'], '%d %b %Y') # 'strptime()' parses a string representing a time according to a format.
    if datetime_object < datetime.today() and 'No' == task['task_complete']: # 'today()' method of date class under datetime module returns a date object which contains the value of Today's date.
        overdue_tasks += 1

        percentage_incomplete = (uncompleted_tasks * 100)/(len(task_dictionary))
        percentage_overdue = (overdue_tasks * 100)/(len(task_dictionary))

        # Print / write everything to the file.
        tasks.write(f"Total number of tasks generated using Task Manager: {len(task_dictionary)}\n")
        tasks.write(f"Number of completed tasks: {completed_tasks}\n")
        tasks.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        tasks.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
        tasks.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
        tasks.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")

        print("Tasks.txt written.")
elif menu == 'ds':
#Modifying the menu option: allows the admin to display statistics so that the reports generated are read from task_overview.txt and user_overview.txt.
#Display_admin_stats(): function called when the user wants to display statistics
def display_admin_stats():
#If task_overview.txt and user_overview.txt don't exist, calls function to generate statistics.
#Then reads data from txt files, and displays it on the screen.
    if not os.path.exists('tasks.txt') and not os.path.exists('user.txt'):
        generate_task_overview()
        generate_user_overview()
    print("Displaying statistics for admin:\n")
    user_dictionary = user_dict()
    task_dictionary = task_dict()
    print(f"Total number of tasks: {len(task_dictionary)}")
    print(f"Total number of users: {len(user_dictionary)}")
#If task.txt and user.txt exist, checks if statistics have been generated.
    with open('task.txt', 'r', encoding='utf-8') as tasks:
        print('\nTASK STATS:\n')
        for line in tasks:
            print(line.strip())

    with open('user.txt', 'r', encoding='utf-8') as tasks:
        print('\nUSER STATS:\n')
        for line in tasks:
            print(line.strip())
#Function to exit the menu.
    exit_menu()


elif menu == 'e':
    print('Goodbye!!!')
    exit()

else:
    print("You have made a wrong choice, Please Try again")

