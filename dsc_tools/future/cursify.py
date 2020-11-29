import struct
from dsc_tools.future.ft_db import cmd_len

def cursify(f):
    filesize = len(f.read())
    f.seek(0)
    while True:
        if int(f.tell()) >= filesize:
            break
        command = struct.unpack('I', f.read(4))[0]
        if command > 128:
            print('Likely Header Value')
            print(f.tell())
            continue
        else:
            lentoseek = cmd_len[command]
            print(command, lentoseek)
            if command != 6:
                for i in range(0, lentoseek):
                    f.seek(4, 1)
            elif command == 6:
                f.seek(16, 1)
                f.write(b'\x00\x00\x00\x00')
                f.seek(8, 1)