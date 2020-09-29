import struct
from misc.ulsr import *
import json


class AET_DB_Entry(object):
    def AET_DB_Entry(self):
        self.AETSet_Name_Offset = 0
        self.SPRSet_Name_Offset = 0
        self.AET_File_Name_Offset = 0
        self.AETSet_Name = ''
        self.SPRSet_Name = ''
        self.AET_File_Name = ''


class SPR_DB_Entry(object):
    def SPR_DB_Entry(self):
        self.SPRSet_Name_Offset = 0
        self.SPR_File_Name_Offset = 0
        self.SPRSet_Name = ''
        self.SPR_File_Name = ''


class DB_Header(object):
    def DB_Header(self):
        self.Count = 0
        self.EntryPointer = 0
        self.Entries = {}


def Read_AETDB_To_Json(f, j):
    entries = []
    aetdb_root = {}
    aetdb_root["AETDB"] = {}
    header = DB_Header()
    header.Count = struct.unpack('I', f.read(4))[0]
    header.EntryPointer = struct.unpack('I', f.read(4))[0]
    f.seek(header.EntryPointer)
    for i in range(0, header.Count):
        entry = AET_DB_Entry()
        entry.AETSet_Name_Offset = struct.unpack('I', f.read(4))[0]
        entry.SPRSet_Name_Offset = struct.unpack('I', f.read(4))[0]
        entry.AET_File_Name_Offset = struct.unpack('I', f.read(4))[0]
        entry.AETSet_Name = Str_Read_At_Offset(entry.AETSet_Name_Offset, f)
        entry.SPRSet_Name = Str_Read_At_Offset(entry.SPRSet_Name_Offset, f)
        entry.AET_File_Name = Str_Read_At_Offset(entry.AET_File_Name_Offset, f)

        entry.__dict__.pop('AETSet_Name_Offset', None)
        entry.__dict__.pop('SPRSet_Name_Offset', None)
        entry.__dict__.pop('AET_File_Name_Offset', None)

        entries.append(entry.__dict__)

    aetdb_root["AETDB"]["Entries"] = entries

    json.dump(aetdb_root, j, indent=2)


def Read_SPRDB_To_Json(f, j):
    entries = []
    sprdb_root = {}
    sprdb_root["SPRDB"] = {}
    header = DB_Header()
    header.Count = struct.unpack('I', f.read(4))[0]
    header.EntryPointer = struct.unpack('I', f.read(4))[0]
    f.seek(header.EntryPointer)
    for i in range(0, header.Count):
        entry = SPR_DB_Entry()
        entry.SPRSet_Name_Offset = struct.unpack('I', f.read(4))[0]
        entry.SPR_File_Name_Offset = struct.unpack('I', f.read(4))[0]
        entry.SPRSet_Name = Str_Read_At_Offset(entry.SPRSet_Name_Offset, f)
        entry.SPR_File_Name = Str_Read_At_Offset(entry.SPR_File_Name_Offset, f)

        entry.__dict__.pop('SPRSet_Name_Offset', None)
        entry.__dict__.pop('SPR_File_Name_Offset', None)

        entries.append(entry.__dict__)

    sprdb_root["SPRDB"]["Entries"] = entries

    json.dump(sprdb_root, j, indent=2)


def Write_SPRDB_To_Bin(j, f):
    data = json.load(j)
    entries = data["SPRDB"]["Entries"]
    offsets_table = []
    # minor prep work
    f.write(struct.pack('I', len(entries)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    # i could just use bytes, but this is easier, and safer
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))

    # ok, now to write the strings

    for entry in entries:
        offsets_table.append(f.tell())
        f.write(entry["SPRSet_Name"].encode('UTF-8'))
        f.write(b'\x00')
        offsets_table.append(f.tell())
        f.write(entry["SPR_File_Name"].encode('UTF-8'))
        f.write(b'\x00')

    entry_offset = f.tell()
    # now to loop around

    for offset in offsets_table:
        f.write(struct.pack('I', offset))

    # finally, we return and write the offset
    f.seek(4)
    f.write(struct.pack('I', entry_offset))


def Write_AETDB_To_Bin(j, f):
    data = json.load(j)
    entries = data["AETDB"]["Entries"]
    offsets_table = []
    # minor prep work
    f.write(struct.pack('I', len(entries)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    # i could just use bytes, but this is easier, and safer
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))
    f.write(struct.pack('I', int(0)))

    # ok, now to write the strings

    for entry in entries:
        offsets_table.append(f.tell())
        f.write(entry["AETSet_Name"].encode('UTF-8'))
        f.write(b'\x00')
        offsets_table.append(f.tell())
        f.write(entry["SPRSet_Name"].encode('UTF-8'))
        f.write(b'\x00')
        offsets_table.append(f.tell())
        f.write(entry["AET_File_Name"].encode('UTF-8'))
        f.write(b'\x00')

    entry_offset = f.tell()
    # now to loop around

    for offset in offsets_table:
        f.write(struct.pack('I', offset))

    # finally, we return and write the offset
    f.seek(4)
    f.write(struct.pack('I', entry_offset))
