import struct
import misc.ulsr
import time
import json
import tkinter as tk
from tkinter import filedialog
import os
import main
from vmd_tools import json_to_csv, exp_translator_eyes, exp_translator_main
import re


class EXPFrame(object):
    def __init__(self):  # Formatted like PD_Tool to maintain compatibility
        self.F = 0  # Frame
        self.B = 0  # Both, Only used for eyes
        self.I = 0  # ID
        self.V = 0  # Value
        self.T = 0  # Transition


def ReadClassicEXPToJson(f, j):  # Reads all data into a json object
    internal_read_tracker = int(0)
    MotOffsetsList = []
    MotNamesList = []
    MotDataList = []
    EXPFormat = struct.unpack("I", f.read(4))[0]
    if EXPFormat != 100:
        print("Invalid exp_*.bin File. Maybe you meant to use the Modern converter?")
        time.sleep(2)
        return 'failed'
    MotionCount = struct.unpack("I", f.read(4))[0]
    MotionExpressionsOffset = struct.unpack("I", f.read(4))[0]
    MotionNamesOffset = struct.unpack("I", f.read(4))[0]
    # Should be safe now to jump ahead

    f.seek(MotionExpressionsOffset)
    for i in range(0, MotionCount):
        MotGroupList = []
        Motion_MAIN_Offset = struct.unpack("I", f.read(4))[0]
        Motion_EYES_Offset = struct.unpack("I", f.read(4))[0]
        MotGroupList.append(Motion_MAIN_Offset)
        MotGroupList.append(Motion_EYES_Offset)
        MotOffsetsList.append(MotGroupList)
    # Okay, now just to be safe we seek to the right position
    f.seek(MotionNamesOffset)
    for i in range(0, MotionCount):
        Name_Offset = struct.unpack("I", f.read(4))[0]
        Name = misc.ulsr.Str_Read_At_Offset(Name_Offset, f)
        MotNamesList.append(Name)
    # Now, we seek to the keys
    for MotGroupList in MotOffsetsList:
        for Mot in MotGroupList:
            motdat = []
            f.seek(Mot)
            while True:
                frame = EXPFrame()
                frame.F = int(struct.unpack("f", f.read(4))[0])
                frame.B = struct.unpack("H", f.read(2))[0]
                frame.I = struct.unpack("H", f.read(2))[0]
                frame.V = struct.unpack("f", f.read(4))[0]
                frame.T = int(struct.unpack("f", f.read(4))[0])

                if frame.F == float(999999):
                    break

                motdat.append(frame)

            MotDataList.append(motdat)

    # Alright, I'm slightly unsure about this code but let's do it
    EXPJson = {"Dex": []}

    for i in range(0, MotionCount):
        MotEntry = {}
        MotEntry["Name"] = MotNamesList[i]
        MotEntry["Main"] = []
        MotEntry["Eyes"] = []
        motdat_main = MotDataList[internal_read_tracker]
        internal_read_tracker += 1
        motdat_eyes = MotDataList[internal_read_tracker]
        internal_read_tracker += 1
        for frame in motdat_main:
            MotEntry["Main"].append(frame.__dict__)
        for frame in motdat_eyes:
            MotEntry["Eyes"].append(frame.__dict__)

        EXPJson["Dex"].append(MotEntry)

    json.dump(EXPJson, j, indent=2)

def ReadDexJsonToVMD(f, p_dir):
    json_obj = json.load(f)
    index_for_delWhenFin = int(0)
    for i in range(0, len(json_obj["Dex"])):
        delWhenFin1Main = json_to_csv.JsonToCSVMain(json_obj, p_dir, index_for_delWhenFin)
        delWhenFin1Eyes = json_to_csv.JsonToCSVEyes(json_obj, p_dir, index_for_delWhenFin)
        print(delWhenFin1Main, delWhenFin1Eyes)
        transMainTempPath = delWhenFin1Main[0].split('.')[0]
        transEyesTempPath = delWhenFin1Eyes[0].split('.')[0]
        with open(delWhenFin1Main[0], 'r') as MainToTranslate:
            delWhenFin2Main = exp_translator_main.TranslateMain(MainToTranslate, transMainTempPath)
        with open(delWhenFin1Eyes[0], 'r') as EyesToTranslate:
            delWhenFin2Eyes = exp_translator_eyes.TranslateEyes(EyesToTranslate, transEyesTempPath)

        # Now let's finish this
        with open(transMainTempPath[0:-5] + '.vmd','wb') as vmdfile:
            vmdfile.write(b'Vocaloid Motion Data 0002\x00\x00\x00\x00\x00')
            NameREd = re.findall('(?<=exp_)\w+', transMainTempPath)[0][0:-5]
            NameBytes = bytes(NameREd, 'Shift-JIS')
            if len(NameBytes) <= 20:
                while len(NameBytes) < 20: NameBytes += b'\x00'
            elif len(NameBytes) > 20:
                NameBytes = NameBytes[0:19]
            vmdfile.write(NameBytes)
            vmdfile.write(b'\x00\x00\x00\x00')
            vmdfile.write(struct.pack('I', int(delWhenFin1Main[1] + delWhenFin1Eyes[1])))
            with open(delWhenFin2Eyes, 'r') as Eyes:
                with open(delWhenFin2Main, 'r') as Main:
                    for line in Main.readlines():
                        Name = bytes(line.split(',')[0], 'Shift-JIS')
                        Frame = line.split(',')[1]
                        Value = line.split(',')[2].split(',')[0]
                        if len(Name) < 15:
                            while len(Name) < 15: Name += b'\x00'
                        elif len(Name) > 15:
                            Name = Name[0:14]
                        vmdfile.write(Name)
                        vmdfile.write(struct.pack('I', int(Frame)))
                        vmdfile.write(struct.pack('f', float(Value)))
                    for line in Eyes.readlines():
                        Name = bytes(line.split(',')[0], 'Shift-JIS')
                        Frame = line.split(',')[1]
                        Value = line.split(',')[2].split(',')[0]
                        if len(Name) < 15:
                            while len(Name) < 15: Name += b'\x00'
                        elif len(Name) > 15:
                            Name = Name[0:14]
                        vmdfile.write(Name)
                        vmdfile.write(struct.pack('I', int(Frame)))
                        vmdfile.write(struct.pack('f', float(Value)))

            os.remove(delWhenFin1Main[0])
            os.remove(delWhenFin1Eyes[0])
            os.remove(delWhenFin2Main)
            os.remove(delWhenFin2Eyes)

        index_for_delWhenFin += 1



def menu():
    print("1. Convert Classic DEX to JSON")
    print("2. Convert Classic DEX to VMD")

    user_choice = input()
    if user_choice == "1":
        root = tk.Tk().withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("Classic DEX File", "*.bin")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as f:
            with open(f'{ext[0]}.json', 'w') as j:
                ReadClassicEXPToJson(f, j)
        main.clear()
        main.main()

    elif user_choice == "2":
        root = tk.Tk().withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("DEX Json", "exp_*.json")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as f:
            ReadDexJsonToVMD(f, ext[0])
        main.clear()
        main.main()