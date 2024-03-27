def menu():
    print('calculator program')
    print('these are the menus : ')
    print('1. triangle area')
    print('2. rectangular area')
    print('3. quit')

    choose_menu = int(input('choose the menu : '))

    if choose_menu > 0 and choose_menu <= 3:
        if choose_menu == 1:
            print('you choosed triangle area menu ')
            length_value = int(input('input the length: '))
            height_value = int(input('input the height'))
            result = 0.5 * length_value * height_value
            print(f'the result is {result}')
            decision = input('do you want to repeat the program?')
            if decision == 'yes':
                menu()
            else:
                exit()

        elif choose_menu == 2:
            print('you choosed rectangular area menu')
            length_value = int(input('input the length: '))
            width_value = int(input('input the height'))
            result = length_value * width_value
            print(f'the result is {result}')
            if decision == 'yes':
                menu()
            else:
                exit()

        elif choose_menu == 3:
            print('thanks for coming')
            exit()
    else:
        print('you typed the wrong number')
menu()
    