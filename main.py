'''
Here is a  program to build a simple Student Management System using Python. 
In order to ensure the data entry is in standardised format. Some of the input validation is added to the system, e.g num_check(), name_validation(),
name_duplication() and name_found(). 
To fullfil the functions of following, add(), view(), view_all(), delete_item() and edit() funcations are created in this programme. 
- Add record 
- Delete record 
- View
- View all 
- Update record 
- Exist programme 

Test cases coverage : 
- txt file is created 
- Add a record which can be found in txt file 
- Delect a record 
- Update a record which is allowing user to change name (as it is the unique key for data, extra steps are added to the program and it allow
    user to re-consider whether they want change the name) 
- check name duplication for entry, assumed no duplcation data is allowed in the system in which unique id would be the student name
- All input data should have a standard format e.g 
    - Student name should be Englist letter only, format example = Steven Lung
    - Age should be integer within the range of 10 - 120
    - Gender should be either "F" or "M"
'''


def num_check(number):
    while True:
        try:
            number = int(number)
        except ValueError:
            number = input("Pleas input integer number Only : ")
        else:
            break
    check_num = number
    return check_num


def name_validation(name):
    name = name.strip()
    while True:
        if "".join(name.split(" ")).isalpha():
            break
        else:
            name = input("Please input student name with characters English letter only : ", )
    input_name = name.strip().title()
    return input_name


def name_duplication(name, existing_list):
    namelower = name.lower()
    while any(namelower in s.lower() for s in existing_list):
        name = input("This student name is duplicated, please retry :", )
        new_name = name.strip()
        name = name_validation(new_name)
        namelower = name.lower()
    input_name = name.strip().title()
    return input_name


def name_found(name, existing_list):
    namelower = name.lower()
    while True:
        if any(namelower in s.lower() for s in existing_list):
            break
        else:
            name = input("The student record cannot be found, Please re-enter : ", )
            name = name_validation(name)
            namelower = name.lower()
    input_name = namelower
    return input_name


def add():
    f = open("student_database.txt", mode='r', encoding='utf-8')
    elist = f.readlines()
    f.close()
    student_name = input("\nPlease input the name of the student : ", )
    student_name = name_validation(student_name)
    student_name = name_duplication(student_name, elist)
    gender = input("Please input the gender of the student : ", )
    while gender != "F" and gender != "f" and gender != "M" and gender != "m":
        gender = input("Please enter 'M' or 'F' for your gender : ")
    gender = gender.upper()
    age = input("Please input the age of the student :　", )
    age = num_check(age)
    while age not in range(10, 120, 1):
        age = input("Please enter the correct age again : ")
        age = num_check(age)
    f = open('student_database.txt', 'a', encoding='utf-8')
    f.write("'Student name': '" + student_name + "', 'gender': '" + gender + "', 'age': '" + str(age) + "'\n")
    f.close()
    if f.closed:
        f = open('student_database.txt', 'r', encoding='utf-8')
        elist = f.readlines()
        f.close()
        if any(student_name in s for s in elist):
            print("Added successfully\n")
        else:
            print("Something went wrong, Please contact support !!!\n")


def view():
    f = open("student_database.txt", mode='r', encoding='utf-8')
    elist = f.readlines()
    f.close()
    search_item = input("\nPlease input the name of the student : ", )
    search_item = name_validation(search_item)
    search_itemlower = name_found(search_item, elist)
    for i in range(len(elist)):
        if elist[i].lower().find(search_itemlower) != -1:
            print(elist[i], end="\n")


def view_all():
    f = open("student_database.txt", 'r', encoding='utf-8')
    elist = f.readlines()
    print("\nAll the students' information is as follows :")
    for i in elist:
        print(i, end="")
    print("")


def delete_item():
    f = open("student_database.txt", 'r', encoding='utf-8')
    elist = f.readlines()
    f.close()
    d_item = input("\nPlease input the name of the student : ", )
    d_item = name_validation(d_item)
    d_itemlower = name_found(d_item, elist)
    d_element = int()
    valid = ""
    for i in range(len(elist)):
        if elist[i].lower().find(d_itemlower) != -1:
            d_element = i
            print(elist[i])
            valid = input("Do you want to delete the above record ? (Y / N) ", )
            while valid != "Y" and valid != "y" and valid != "N" and valid != "n":
                valid = input("Incorrect input, Please retry (Y / N)",)
            valid = valid.upper()
    if valid == "Y":
        del elist[d_element]
        f = open("student_database.txt", 'w', encoding='utf-8')
        f.writelines(elist)
        f.close()
        if f.closed:
            f = open("student_database.txt", 'r', encoding='utf-8')
            elist = f.readlines()
            if any(d_itemlower in s.lower() for s in elist):
                print("Something went wrong, Please contact support !!!")
            else:
                print("Deleted successfully!\n")
    elif valid == "N":
        print("No record will be deleted\n")


def edit():
    f = open("student_database.txt", 'r+', encoding='utf-8')
    elist = f.readlines()
    f.close()
    edit_item = input("\nPlease input the name of the student : ", )
    edit_item = name_validation(edit_item)
    # it is the validation for your input is valid and can be found in the list
    edit_item = name_found(edit_item, elist)
    edit_itemlower = edit_item.lower()
    edit_element = int()
    change_name = input("Would you like to edit student name ? (Y / N) ")
    while change_name != "Y" and change_name != "y" and change_name != "N" and change_name != "n":
        change_name = input("Incorrect input, Please retry (Y / N)",)
    if change_name.upper() == "Y":
        new_name = input("Please input updated student name :　",)
        new_name = name_validation(new_name)
        new_name = name_duplication(new_name, elist)
        student_name = new_name.title()
    else:
        student_name = edit_item.title()
    gender = input("Please input the gender of the student : ", )
    while gender != "F" and gender != "f" and gender != "M" and gender != "m":
        gender = input("Please enter 'M' or 'F' for your gender : ")
    gender = gender.upper()
    age = input("Please input the age of the student :　", )
    age = num_check(age)
    while age not in range(10, 120, 1):
        age = input("Please enter the correct age again : ")
        age = num_check(age)
    for i in range(len(elist)):
        if elist[i].lower().find(edit_itemlower) != -1:
            edit_element = i
    elist[edit_element] = "'Student name': '" + student_name + "', 'gender': '" + gender + "', 'age': '" + str(age) + "'\n"
    f = open("student_database.txt", 'w+', encoding='utf-8')
    f.writelines(elist)
    f.close()
    if f.closed:
        f = open("student_database.txt", 'r', encoding='utf-8')
        elist = f.readlines()
        if any(student_name in s for s in elist):
            print("Update successfully!\n")
        else:
            print("Something went wrong, Please contact support !!!\n")


while True:
    try:
        file = open("student_database.txt", mode='r', encoding='utf-8')
    except FileNotFoundError:
        file = open("student_database.txt", mode='x', encoding='utf-8')
        file.close()
    else:
        break
close_action = "N"
operation_code = 0
while operation_code != 6 or close_action != "Y":
    print("************** Student Management System **************")
    print("---------------------- 1. Add -------------------------")
    print("---------------------- 2. Delete ----------------------")
    print("---------------------- 3. Update ----------------------")
    print("---------------------- 4. Search ----------------------")
    print("---------------------- 5. Display All -----------------")
    print("---------------------- 6. Exit ------------------------")
    operation_code = input("Please input the number of the operation : ", )
    operation_code = num_check(operation_code)
    while operation_code not in range(1, 7, 1):
        operation_code = input("The number of the operation is incorrect, Please retry: ")
        operation_code = num_check(operation_code)
    if operation_code == 6:
        close_action = input("Do you want to Exit? Yes(Y)or No(N):", )
        close_action = close_action.upper()
        if close_action == "Y":
            print("Thanks, you have successfully exited the system!")
        else:
            print("", end="\n")
    elif operation_code == 5:
        view_all()
    elif operation_code == 4:
        view()
    elif operation_code == 3:
        edit()
    elif operation_code == 1:
        add()
    elif operation_code == 2:
        delete_item()
