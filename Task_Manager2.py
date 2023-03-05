#   Many thanks for the feedback.
# =====importing libraries===========
from datetime import date
from datetime import datetime

today = date.today()

print("CAPSTONE PROJECT II ")
print("Compulsory Tasks 2")
print("===================")
usernames = []
# =====Section 1: Start by reading all usernames in file into a usernames array.===========

with open("./user.txt", "r") as f:
    for line in f:
        words = line.split()
        if words:
            usernames.append(words[0].replace(',', ''))
f.close()

print("Admin Users to input Credentials")
with open('./user.txt', 'a+') as f:
    # check the usernames array if we have our nominated admin usernames already in the file,
    # if not, add them first. Ref: Live Lectures

    NewAdmin1 = input("Enter your Admin name and password separated by comma:\t").lower()
    NewAdmin2 = input("Enter your Admin name and password separated by comma:\t").lower()
    NewAdmin3 = input("Enter your Admin name and password separated by comma:\t").lower()

    f.write(f'{NewAdmin1}' + '\n')
    f.write(f'{NewAdmin2}' + '\n')
    f.write(f'{NewAdmin3}' + '\n')
f.close()
# ====/end section=====

# ====Login Section====
#   to have Admin and Password assigned for logging in, first word and second wor is extracted from the file.
with open("./user.txt", 'r+') as f:
    first_words = []
    second_words = []
    for line in f:
        words = line.split()
        if words:
            first_words.append(words[0])
            second_words.append(words[1])

    w = first_words[0].replace(',', '')
    x = first_words[1].replace(',', '')
    y = first_words[2].replace(',', '')
    z = first_words[3].replace(',', '')
    a = second_words[0]
    b = second_words[1]
    c = second_words[2]
    d = second_words[3]

#   to use stored Admin and password for validating log-in, using loop.
complete = False
adminUsers = [[w, a], [x, b], [y, c], [z, d]]
loggedInAdminUser = None

# ====/end login section=====
print("===================")
print("Logged in Admin to Assign Tasks ")
# ==== Define Functions ====

def registerUser():
    # registering a user
    # validating entered password with retry.
    NewUser = input("Enter the new user name:\t")
    NewUserPassword = input("Enter a password:\t")
    NewUserPasswordConfirmation = input("confirm the password:\t")
    if NewUserPasswordConfirmation == NewUserPassword:
        new = (f"{NewUser}", f"{NewUserPassword}")
        key, value = new
        with open("./user.txt", 'a+') as f:
            f.write(key + ',' + ' ' + value + '\n')
        f.close()
        print("You have now registered a new user with username " + NewUser + "!\n")
    else:
        print("The passwords you entered do not match.\n")


def addTask():
    #   adding new task to the tasks.txt file by the logged in admin user
    Task = input("Please Name Task Owner:\t\t\t")
    Title = input("Please State Task Title:\t\t\t")
    Description = input("Describe Task:\t\t\t\t")
    AssignedDate = today.strftime("%d %b %Y")
    DueDate = input("Enter Due date in the format (dd MMM yyyy):\t\t\t\t")
    Completion = input("Is task completed? Enter 'Yes' or 'No':\t")

    with open("./tasks.txt", 'a+') as f:
        f.write(Task + ', ' + Title + ', ' + Description + ', ' + f'{AssignedDate}' + ', '
                + DueDate + ', ' + Completion + '\n')
    f.close()


def viewAll():
    taskNum = 0
    with open('tasks.txt', 'r') as f:
        print("\n=== ALL TASKS ===")
        for line in f:
            rtf_line = line.split(", ")
            print(f"""
                    ---------------[Task: {taskNum + 1}]-------------
                    Task:               {rtf_line[1]}
                    Assigned to:        {rtf_line[0]}
                    Task description:   {rtf_line[2]}                        
                    Date assigned:      {rtf_line[3]}
                    Due date:           {rtf_line[4]}
                    Task complete?      {rtf_line[5]}
                    -----------------------------------------------\n""")
            taskNum += 1
        print(f"Total no of all tasks: {taskNum}\n")
        f.close()


def viewMine():
    taskNum = 0
    with open('tasks.txt', 'r') as f:
        print("\n=== MY TASKS ===")
        for line in f:
            rtf_line = line.split(", ")
            if username == rtf_line[0]:
                print(f"""
                        ---------------[Task: {taskNum + 1}]-------------
                        Task:               {rtf_line[1]}
                        Assigned to:        {rtf_line[0]}
                        Task description:   {rtf_line[2]}                        
                        Date assigned:      {rtf_line[3]}
                        Due date:           {rtf_line[4]}
                        Task complete?      {rtf_line[5]}
                        -----------------------------------------------\n""")
                taskNum += 1
        print(f"Total no of my tasks: {taskNum}\n")


def generateReports():
    totalTasks = 0
    currentDate = date.today().strftime("%d %B %Y")
    completedTasks = 0
    uncompletedTasks = 0
    overdueTasks = 0

    with open('user.txt', 'r') as f:
        first_words = []

        for line in f:
            words = line.split()
            if words:
                first_words.append(words[0])
    f.close()

    with open('tasks.txt', 'r') as f:
        for line in f:
            totalTasks += 1
            rtf_line = line.split(", ")
            if rtf_line[5].replace('\n', '') == 'Yes':
                completedTasks += 1
            else:
                uncompletedTasks += 1

            if datetime.strptime(rtf_line[4], "%d %b %Y").date() < today and rtf_line[5].replace('\n', '') == 'No':
                overdueTasks += 1
    f.close()

    print(f"""
            Current date:\t\t\t{currentDate}\n
            Total no of users:\t\t\t{len(first_words)}
            Total no of tasks:\t\t\t{totalTasks}
            No of completed tasks:\t\t{completedTasks}
            No of uncompleted tasks:\t\t{uncompletedTasks}
            No of overdue tasks:\t\t{overdueTasks}\n
            """)


# ====/end functions =====


# ====Login Section====
#   username must be admin, and username and password combination must match resord in user.txt.
authenticated = False
while not authenticated:
    username = input("Enter your username to log in:\t")
    password = input("Enter your password:\t")
    for n in range(len(adminUsers)):
        if username == adminUsers[n][0]:

            if password == adminUsers[n][1]:
                loggedInAdminUser = username
    if username != loggedInAdminUser:
        print("The username " + username + " does not have permission to use this programme.\n")
    else:
        with open("./user.txt", 'r+') as f:
            for lineNumber, line in enumerate(f, start=1):
                word = username + ',' + ' ' + password + '\n'
                if word in line:
                    authenticated = True
                    break
        f.close()

        if not authenticated:
            print("The credentials you entered are invalid.\n")
        else:
            print("===================")
            print("Your credentials are correct! You have Admin rights.")
            print(f"You may now proceed, {username}!\n")

# ====/end login section=====

# ====Main program Section====
while True:
    # presenting additional menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - View my task
                    ds - Display statistics
                    e - Exit
                    : ''').lower()

    if menu == 'r':
        # use the register_user function
        registerUser()
        pass

    elif menu == 'a':
        # use the add_task function
        addTask()
        pass

    elif menu == 'va':
        # use the view_all function
        viewAll()

    elif menu == 'vm':
        # Use the view_mine function
        viewMine()

    elif menu == 'ds':
        # Use the generate_reports functions
        generateReports()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

# ====/end main program section=====
