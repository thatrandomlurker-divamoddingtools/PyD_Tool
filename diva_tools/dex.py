import struct
import misc.ulsr
import time
import json
import tkinter as tk
from tkinter import filedialog
import os
import main


class EXPFrame(object):
    def __init__(self):  # Formatted like PD_Tool to maintain compatibility
        self.F = 0  # Frame
        self.B = 0  # Both, Only used for eyes
        self.I = 0  # ID
        self.V = 0  # Value
        self.T = 0  # Transition


def ReadClassicEXPToJson(f, j):  # All the reading should be finished now, just gotta shove it into a json file
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

def WriteJsonToClassicDex(j, f):
    dex = json.load(j)
    



def menu():
    print("1. Convert Classic DEX to JSON")
    print("2. Convert JSON to Classic DEX")

    user_choice = input()
    if user_choice == "1":
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("Classic DEX File", "*.bin")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as f:
            with open(f'{ext[0]}.json', 'w') as j:
                ReadClassicEXPToJson(f, j)
        main.clear()
        main.main()