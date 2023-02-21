import os, time
my_events = []


def pretty_print():
    print()
    for row in my_events:
        print(f"{row[0] : ^15} {row[1] :^15}")
    print()


while True:
    menu = input("1:Add, 2: Remove\n ")
    if menu == "1":
        event = input("what event?:").capitalize()
        date = input("what date ? : ")
        row = [event, date]
        my_events.append(row)
        pretty_print()
    else:
        criteria = input("what event do you want to remove?:").tittle()
        for row in my_events:
            if criteria in row:
                my_events.remove(row)
        pretty_print()

    f = open("calendar.txt", "w")
    os.system("clear")
    f.write(str(my_events))
    f.close()
