import os

names = []
numbers = []

def add_contact():
    a = input('enter the name: ')
    if a in names:
        print('!already exist!')
    else:
        names.append(a)
        b = input('enter the number: ')
        numbers.append(b)
        print('!Done!')

def search():
    c = input('enter name/number: ')
    try:
        d = int(c)
        if type(d) == int:
            count = 0
            for i in numbers:
                y = i.find(c)
                if y != -1:
                    print(i,'----> ',names[count])
                count += 1
    except:
        count = 0
        for i in names:
            x = i.find(c)
            if x != -1:
                print(i,'----> ',numbers[count])
            count += 1

def delete():
    e = input('enter the neme: ')
    count = 0 
    for i in names:
        if i == e:
            del names[count]
            del numbers[count]
            print('!contact deleted!')
            break
        count += 1
    if count == len(names) and count>0:
        print('!no contact found!')

def edit():
    f = input('enter the name: ')
    count = 0
    for i in names:
        if i == f:
            numbers[count] = input('enter the new number: ')
        count += 1
    print('!Done!')

def back():
    l = input('press any key to go back menu: ')


while True:
    print('***** welcome to the contact book *****')
    print('enter:\n     1 for add contact\n     2 for search a contact\n     3 for edit a contact\n     4 for delete a contact')
    v = input('-')

    try:
        v = int(v)

        if v == 1:
            add_contact()
            back()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif v == 2:
            search()
            back()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif v == 3:
            edit()
            back()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif v == 4:
            delete()
            back()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('wrong')
            back()
            os.system('cls' if os.name == 'nt' else 'clear')
    except:
        print('wrong')
        back()
        os.system('cls' if os.name == 'nt' else 'clear')
