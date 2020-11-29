import diva_tools.dex_menu, main, dsc_tools.future.ft_menu_main, diva_tools.litlib

def menu():
    print("1. DEX Tools")
    print("2. Future Tone DSC Tools")
    print("3. LIT Tools")

    user_choice = input()
    if user_choice == "1":
        main.clear()
        diva_tools.dex_menu.menu()
    if user_choice == "2":
        main.clear()
        dsc_tools.future.ft_menu_main.main()
    if user_choice == "3":
        main.clear()
        diva_tools.litlib.menu()
