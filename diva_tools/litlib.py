import struct
import json
import main

class LightEntry(object):
    def LightEntry(self):
        self.ID = 0
        self.Flags = 0
        self.Type = 0
        self.AmbientR = 0
        self.AmbientG = 0
        self.AmbientB = 0
        self.AmbientI = 0
        self.DiffuseR = 0
        self.DiffuseG = 0
        self.DiffuseB = 0
        self.DiffuseI = 0
        self.SpecularR = 0
        self.SpecularG = 0
        self.SpecularB = 0
        self.SpecularI = 0
        self.PositionX = 0
        self.PositionY = 0
        self.PositionZ = 0
        self.CurveStartPoint = 0
        self.CurveEndPoint = 0
        self.CurveBlendFactor = 0


def litReaderX(f, j):
    # The header is 0x40 bytes long, in decimal 64 bytes
    # so let's just bypass that for now
    f.seek(0x40, 1)
    # It also seems like it actually uses the POF sections
    # So any offsets need to have 0x40 added to them
    # Right now we should be at an area that has very little useful info
    # so let's skip it
    f.seek(8, 1)  # just to get to the main data offset
    MainDataOffset = struct.unpack('Q', f.read(8))[0] + 0x40
    f.seek(MainDataOffset)
    LightMaxIndex = struct.unpack('Q', f.read(8))[0]
    LightDataOffset = struct.unpack('Q', f.read(8))[0] + 0x40
    f.seek(LightDataOffset)
    LightEntryList = []
    for i in range(0, LightMaxIndex):
        LE = LightEntry()
        LE.ID = struct.unpack('I', f.read(4))[0]
        LE.Flags = struct.unpack('I', f.read(4))[0]
        LE.Type = struct.unpack('I', f.read(4))[0]
        f.seek(24, 1)  # Just because there's an unexplainable number of padding bytes
        LE.AmbientR = struct.unpack('f', f.read(4))[0]
        LE.AmbientG = struct.unpack('f', f.read(4))[0]
        LE.AmbientB = struct.unpack('f', f.read(4))[0]
        LE.AmbientI = struct.unpack('f', f.read(4))[0]
        LE.DiffuseR = struct.unpack('f', f.read(4))[0]
        LE.DiffuseG = struct.unpack('f', f.read(4))[0]
        LE.DiffuseB = struct.unpack('f', f.read(4))[0]
        LE.DiffuseI = struct.unpack('f', f.read(4))[0]
        LE.SpecularR = struct.unpack('f', f.read(4))[0]
        LE.SpecularG = struct.unpack('f', f.read(4))[0]
        LE.SpecularB = struct.unpack('f', f.read(4))[0]
        LE.SpecularI = struct.unpack('f', f.read(4))[0]
        LE.PositionX = struct.unpack('f', f.read(4))[0]
        LE.PositionY = struct.unpack('f', f.read(4))[0]
        LE.PositionZ = struct.unpack('f', f.read(4))[0]
        f.seek(28, 1)  # Again, unknown padding...
        LE.CurveStart = struct.unpack('f', f.read(4))[0]
        LE.CurveEnd = struct.unpack('f', f.read(4))[0]
        LE.CurveBlendFactor = struct.unpack('f', f.read(4))[0]
        f.seek(16, 1)  # Final Padding
        print(LE.__dict__)

        LightEntryList.append(LE.__dict__)

    # Setup the json dump
    root = {"LITC": {"Entries": LightEntryList}}
    json.dump(root, j, indent=2)

import os
import tkinter as tk
from tkinter import filedialog


def menu():
    print("1. Convert X/XHD LIT file to JSON")

    user_choice = input()
    if user_choice == "1":

        file_path = filedialog.askopenfilename(filetypes=[("X/XHD LIT Container", "*.lit")])
        ext = os.path.splitext(file_path)
        with open(file_path, 'rb') as f:
            with open(f'{ext[0]}.json', 'w') as j:
                litReaderX(f, j)
        main.clear()


