# coding=utf-8


FILENAME = "members.csv"
OTCHET_SVOD = "report.csv"


def my_input():
    """Displays a list of commands and reads the entered command."""
    choice = ""
    choices = {'1', '2', '3', '4'}
    while choice not in choices:
        print("Введите номер команды:\n"
              "1 - Вывести все отделы\n"
              "2 - Вывести сводный отчёт по отделам\n"
              "3 - Сохранить сводный отчёт в виде csv\n"
              "4 - Выход\n")
        choice = input()
    return choice


def read_file(file):
    """Creates a dictionary of departments, and lists the salaries of their employees"""
    divisions = {}
    lines = file.readlines()
    for line in lines:
        params = line.split("; ")
        if divisions.get(params[2]) is None:
            d = {params[2]: [params[4]]}
            divisions.update(d)
        else:
            divisions.get(params[2]).append(params[4])
    return divisions


def report(divisions):
    """Generates a list of divisions with summary data"""
    my_report = []
    for key in divisions:
        payments = [int(item) for item in divisions.get(key)]
        my_report.append(key + " Численность: " + str(len(payments)) + ", Макс зп: " + str(max(payments)) + ", Мин зп: "
                      + str(min(payments)) + ", Ср зп:" + str(sum(payments) // len(payments)))
    return my_report


def work_cycle(divisions):
    """Implements the main work with the user, outputs commands, receives them, and executes"""
    while 1:
        choice = my_input()
        if choice == "1":
            for otdel in divisions.keys():
                print(otdel)
        elif choice == "2":
            for otdel in report(divisions):
                print(otdel)
        elif choice == "3":
            f = open(OTCHET_SVOD, 'w')
            for otdel in report(divisions):
                f.write(otdel + "\n")
            f.close()
            print("Отчет сохранен")
        elif choice == "4":
            break


if __name__ == '__main__':
    f = open(FILENAME, 'r')
    divisions = read_file(f)
    f.close()
    work_cycle(divisions)
