import diva_tools.dex_menu, main

def menu():
    print("1. DEX Tools")

    user_choice = input()
    if user_choice == "1":
        main.clear()
        diva_tools.dex_menu.menu()