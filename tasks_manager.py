# =====importing libraries===========
from datetime import date
from datetime import datetime
import os.path

today = date.today()
print("CAPSTONE PROJECT III ")
print("==================")

# =====Section 1: storing Admin Users and their Passwords===========
#   to begin appending new lines, line 1 has to be excluded.
with open("user.txt", "r") as f:
    lines = f.readlines()
    len(f.readline())
    f.seek(len(f.readline()) + 1)
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
    admin_username = first_words[0].replace(',', '')
    admin_password = second_words[0]

    w = first_words[0].replace(',', '')
    x = first_words[1].replace(',', '')
    y = first_words[2].replace(',', '')
    z = first_words[3].replace(',', '')
    a = second_words[1]
    b = second_words[2]
    c = second_words[3]
    d = second_words[4]
f.close()
# ====/end login section=====

# ====Registering Section====
def reg_user():
    if current_user != w:
        print('You dont have admin access\n')
    else:
        # registering a user
        # validating password with retry.
        username_new = input("Enter your username:\t")
        password_new = input("Enter your password:\t")
        password_confirm = input("confirm your password:\t")
        if password_new == password_confirm:
            print("You are now registered!")
            new = (f"{username_new}", f"{password_new}")
            key_new, value_new = new
            with open("./user.txt", 'a+') as f:
                f.write(key_new + ',' + ' ' + value_new + '\n')
        else:
            print("password does not match")
        f.close()


def add_task():
    #   adding new task to the tasks.txt file by the registered user, appending from line 3
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
        len(f.readline())
        f.seek(len(f.readline()) + 2)


    Task = input("Please Task Owner:\t\t\t")
    Title = input("Please Task Title:\t\t\t")
    Description = input("Describe Task:\t\t\t\t")
    Assigned_date = today
    Due_date = input("Enter Due date:\t\t\t\t")
    Completion = "No"


    with open("./tasks.txt", 'a+') as f:
        f.write(Task + ', ' + Title + ', ' + Description + ', ' + f'{Assigned_date}' + ', '
                + Due_date + ', ' + Completion + '\n')

        f.close()


def view_all():
    with open("./tasks.txt", 'r+') as f:
        for pos, line in enumerate(f):
            split_data = line.split(",")
            output = "-----------------------\n"
            output += '\n'
            output += f'Assigned to:\t\t{split_data[0]}\n'
            output += f'Task:\t\t\t\t{split_data[1]}\n'
            output += f'Description:\t\t{split_data[2]}\n'
            output += f'Assigned Date:\t\t{split_data[3]}\n'
            output += f'Due Date:\t\t\t{split_data[4]}\n'
            output += f'Is completed:\t\t{split_data[5]}\n'
            output += '\n'
            output += "-----------------------\n"
            print(output)

        f.close()


def view_mine():
    task_num = 0
    my_tasks = []
    with open('tasks.txt', 'r') as read_tasks_file:
        print("\n=== MY TASKS ===")
        # owner = []
        for line in read_tasks_file:
            rtf_line = line.split(", ")
            # owner.append(rtf_line[0])
            if current_user == rtf_line[0]:
                my_tasks.append(rtf_line)
                print(f"""
                        -------------------[Task: {task_num + 1}]---------------------
                        Task:               {rtf_line[1]}
                        Assigned to:        {rtf_line[0]}
                        Date assigned:      {rtf_line[4]}
                        Due date:           {rtf_line[3]}
                        Task complete?      {rtf_line[-1]}
                        Task description:   
                        {rtf_line[2]}
                        -----------------------------------------------\n""")
            task_num += 1

    num_my_tasks = len(my_tasks)


def display_stat():
    task_num = 0
    with open('tasks.txt', 'r') as read_tasks_file:
        for line in read_tasks_file:
            task_num += 1

    print(f"""
            Total No of users: {len(user1)}
            Total No of tasks: {task_num}
            """)


def generate_reports():
    with open('./tasks.txt', 'r') as read_tasks_file:
        tasks_file_content = read_tasks_file.readlines()

    total_tasks = len(tasks_file_content)

    current_date = date.today().strftime("%d %B %Y")

    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    for line in tasks_file_content:
        split_line = line.split(', ')
        if 'Yes' in split_line[-1]:
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            task_due_date = split_line[-3]

            obj_current_date = datetime.strptime(current_date, "%d/%m/%Y")
            obj_task_due_date = datetime.strptime(task_due_date, "%d/%m/%Y")
            if obj_task_due_date < obj_current_date:
                overdue_tasks += 1

    with open('task_overview.txt', 'w+') as write_task_overview_file:
        write_task_overview_file.write(f""" 
            -----------------------------------------------
                TASK OVERVIEW REPORT: {current_date}

                Total tasks:        | {total_tasks}
                    Completed:      | {completed_tasks}
                    Incomplete:     | {uncompleted_tasks}
                    Overdue:        | {overdue_tasks}
                    % Incomplete:   | {int((uncompleted_tasks / total_tasks) * 100)}%
                    % Overdue:      | {int((overdue_tasks / total_tasks) * 100)}%

            -----------------------------------------------
                """)

    with open('user.txt', 'r') as read_user_file:
        users = read_user_file.readlines()

        all_users = []

        for line in users:
            split_line = line.split(', ')

            if split_line[0] not in all_users:
                all_users.append(split_line[0])
            else:
                pass

        total_users = len(all_users)

        write_user_overview_file = open('user_overview.txt', 'w+')
        new_file_content = (f""" 
            -----------------------------------------------
                USER OVERVIEW REPORT: {current_date}

                Total users:        | {total_users}
                Total tasks:        | {total_tasks}

                USER DETAILS:""")

    #

    obj_current_date = datetime.strptime(current_date, "%d/%m/%Y")

    read_tasks_file = open('tasks.txt', 'r')

    user_stats_dict = {}

    for user in all_users:
        user_stats_dict[user] = {'Total tasks': 0,
                                 'Complete tasks': 0,
                                 'Incomplete tasks': 0,
                                 'Overdue tasks': 0,
                                 '% Complete': 0,
                                 '% Incomplete': 0,
                                 '% Overdue': 0, }

    for line in read_tasks_file:
        split_line = line.split(', ')
        current_user = split_line[0]
        user_stats_dict[current_user]['Total tasks'] += 1
        if 'No' in split_line[-1]:  #
            user_stats_dict[current_user][
                'Incomplete tasks'] += 1
            task_due_date = split_line[-3]
            obj_task_due_date = datetime.strptime(task_due_date, "%d/%m/%Y")
            if obj_task_due_date < obj_current_date:
                user_stats_dict[current_user]['Overdue tasks'] += 1
        elif 'Yes' in split_line[-1]:
            user_stats_dict[current_user]['Complete tasks'] += 1

    for user in all_users:
        try:
            user_stats_dict[user]['% Complete'] = int(
                user_stats_dict[user]['Complete tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Complete'] = 0

        try:
            user_stats_dict[user]['% Incomplete'] = int(
                user_stats_dict[user]['Incomplete tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Incomplete'] = 0

        try:
            user_stats_dict[user]['% Overdue'] = int(
                user_stats_dict[user]['Overdue tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Overdue'] = 0

    for user in user_stats_dict:
        new_file_content += (f"""

        USER: {user}

        Total Tasks:                | {user_stats_dict[user]['Total tasks']}
            % of All Tasks:         | {int(user_stats_dict[user]['Total tasks'] / total_tasks * 100)}%

            Complete Tasks:         | {user_stats_dict[user]['Complete tasks']}
                % Complete:         | {user_stats_dict[user]['% Complete']}%
            Incomplete Tasks:       | {user_stats_dict[user]['Incomplete tasks']}
                % Incomplete:       | {user_stats_dict[user]['% Incomplete']}%
            Overdue Tasks:          | {user_stats_dict[user]['Overdue tasks']}
                % Overdue Tasks:    | {user_stats_dict[user]['% Overdue']}%

        -----------------------------------------------""")

    read_tasks_file.close()

    with open('user_overview.txt', 'w+'):
        write_user_overview_file.write(new_file_content)

    print(f"\n✨ Report generated, please see text files. ✨\n")


def report():
    if os.path.exists('task_overview.txt') and os.path.exists('user_overview.txt'):
        if os.stat("task_overview.txt").st_size == 0:
            generate_reports()
    else:
        generate_reports()

    #   to use stored Admin and password for validating log-in, using loop.
# ====/end section=====

# ==== Using stored Admin Section====

complete = False
user1 = [[w, d], [x, a], [y, b], [z, c]]
current_user = ''

while not complete:
    username = input("Enter your username:\t")
    password = input("Enter your password:\t")
    for n in range(len(user1)):
        if username == user1[n][0] or admin_username == username:
            if password == user1[n][1] or password == admin_password:
                print("You can now proceed to assigned Task,", username)
                current_user = username
                complete = True
            else:
                break

    if not complete:
        print("Incorrect Username or Password !")

while True:

    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - view my task
e - Exit
: ''').lower() if current_user == 'admin' else input('''Select one of the following Options below:
a - adding a task
va - View all tasks
vm - view my task
gr - generate reports
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        report()
    elif menu == 'ds':
        display_stat()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
# ====/end main program section=====

