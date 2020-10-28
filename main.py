import os, time, db_menu, diva_tools.dex, diva_tools.diva_menu

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

if not os.path.exists('Resources'):
    os.mkdir('Resources')


def FRCheck():  # Simple first run check
    if not os.path.exists('Resources\\FirstRun.dat'):
        print("Welcome to P'y'D Tool v0.0.-1a")
        time.sleep(2)
        print("This application (if you can call it that) is currently still under heavy beta, with barely any features")
        time.sleep(2)
        user_accepts = input("If you understand this, Please type 'Yes'\n> ")

        if user_accepts == "Yes" or "yes":
            with open('Resources\\FirstRun.dat', 'w') as f:
                f.write('User claims to understand')
            print("Preparing PyD_Tool")
            time.sleep(5)
            clear()

        else:
            print("Exiting")
            time.sleep(3)
            exit()


def main():
    FRCheck()
    print("??????????????????????????")
    print("?1. DB Tools             ?")
    print("?2. DIVA Conversion Tools?")
    print("??????????????????????????")

    user_choice = input()

    if user_choice == "1":
        clear()
        db_menu.main_menu()
    elif user_choice == "2":
        clear()
        diva_tools.diva_menu.menu()


if __name__ == "__main__":
    main()
