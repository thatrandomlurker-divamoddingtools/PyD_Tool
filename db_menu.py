import main
import os
import mirai_tools.mirai_db_tools
import tkinter as tk
from tkinter import filedialog


def mirai_menu():
    print("1. Sprite DB Converter")
    print("2. AET DB Converter")
    print("3. NintendoWare DB Converter (Not Implemented)")

    user_choice = input()

    if user_choice == "1":
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(filetypes=(('SPRDB BIN File', '*.bin'), ('SPRDB JSON File', '*.json')))
        ext = os.path.splitext(file_path)
        if ext[1] == '.bin':
            with open(file_path, 'rb') as f:
                with open(f'{ext[0]}.json', 'w') as o:
                    mirai_tools.mirai_db_tools.Read_SPRDB_To_Json(f, o)
        elif ext[1] == '.json':
            with open(file_path, 'rb') as f:
                with open(f'{ext[0]}.bin', 'wb') as o:
                    mirai_tools.mirai_db_tools.Write_SPRDB_To_Bin(f, o)

        main.clear()
        main.main()

    elif user_choice == "2":
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(filetypes=(('AETDB BIN File', '*.bin'), ('AETDB JSON File', '*.json')))
        ext = os.path.splitext(file_path)
        if ext[1] == '.bin':
            with open(file_path, 'rb') as f:
                with open(f'{ext[0]}.json', 'w') as o:
                    mirai_tools.mirai_db_tools.Read_AETDB_To_Json(f, o)
        elif ext[1] == '.json':
            with open(file_path, 'rb') as f:
                with open(f'{ext[0]}.bin', 'wb') as o:
                    mirai_tools.mirai_db_tools.Write_AETDB_To_Bin(f, o)

        main.clear()
        main.main()

    elif user_choice == "3":
        print('REALLY unimplemented')


def main_menu():
    print("1. DIVA Database Tools")
    print("2. MIRAI Database Tools")

    user_choice = input()

    if user_choice == "1":
        print('Unimplemented')
        main.clear()
        main.main()
    elif user_choice == "2":
        main.clear()
        mirai_menu()
