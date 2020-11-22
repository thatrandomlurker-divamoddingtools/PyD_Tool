import diva_tools.dex, main, vmd_tools.vmd_defs
import os
import tkinter as tk
from tkinter import filedialog


def menu():
    print("1. Classic DEX Converter (F/AFT/FT/MM)")
    print("2. VMD to DEX Json (PD_Tool)")

    user_choice = input()
    if user_choice == "1":
        main.clear()
        diva_tools.dex.menu()
    if user_choice == "2":

        file_path = filedialog.askopenfilename(filetypes=[("MAIN VMD FILE", "*.vmd")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as dex_main_f:
            with open(f'{ext[0][:-4]}eyes.vmd', 'rb') as dex_eyes_f:
                with open(f'{ext[0]}.json', 'w') as j:
                    vmd_tools.vmd_defs.Read_Main_Morphs_to_EXP(dex_main_f, dex_eyes_f, j)
        main.clear()