import struct
import random
from dsc_tools.future.ft_db import cmd_len

def MaxRandomizer(f):  # Random target types (for non slides), Random entry angles, random amplitude (within a range of 200 - 2000)
    filesize = len(f.read())
    f.seek(0)
    print(f.tell())
    while True:
        print('hallo')
        if int(f.tell()) >= filesize:
            break
        command = struct.unpack('I', f.read(4))[0]
        if command > 128:
            print('Likely Header Value')
            print(f.tell())
        else:
            lentoseek = cmd_len[command]
            print(command, lentoseek)
            if command != 6:
                for i in range(0, lentoseek):
                    f.seek(4, 1)
            elif command == 6:
                target_type = struct.unpack('I', f.read(4))[0]
                f.seek(-4, 1)
                if target_type == 0 or 1 or 2 or 3:
                    f.write(struct.pack('I', int(random.choice(range(0, 4)))))
                elif target_type == 4 or 5 or 6 or 7:
                    f.write(struct.pack('I', int(random.choice(range(4, 8)))))
                f.seek(8, 1)
                f.write(struct.pack('i', int(random.choice(range(-360, 361)) * 1000)))
                f.write(struct.pack('i', int(random.choice(range(500, 2001)) * 250)))
                f.write(struct.pack('i', int(random.choice(range(150, 2001)))))
                f.write(struct.pack('i', int(random.choice(range(-5, 6)))))
