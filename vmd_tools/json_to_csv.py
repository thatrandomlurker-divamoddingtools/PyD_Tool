import json
import os


def JsonToCSVMain(data, dir, index):
    frame_count = int(0)
    prev_exists_count = 0
    
    prev_EXP = int(0)
    prev_VALUE = float(0)
    prev_FRAME = int(0)
    vmd_str = """"""

    for i in data['Dex'][index]['Main']:
        Frame = i['F']
        ID = i['I']
        Value = i['V']
        Trans = i['T']

        if prev_exists_count == 0:
            vmd_str += f'{ID},{Frame},{float(Value)}\n'
            prev_EXP = int(ID)
            prev_VALUE = int(Value)
            prev_FRAME = int(Frame)
            prev_exists_count = 1
            frame_count += 1

        elif prev_exists_count == 1:
            if ID == prev_EXP:
                vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                vmd_str += f'{prev_EXP},{Frame + Trans},{Value}\n'
                frame_count += 2
            elif ID != prev_EXP:
                vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                vmd_str += f'{prev_EXP},{Frame + Trans},0.0\n'
                vmd_str += f'{ID},{Frame},{float(0)}\n'
                vmd_str += f'{ID},{Frame + Trans},{float(Value)}\n'

                frame_count += 4

            prev_EXP = ID
            prev_VALUE = Value
            prev_FRAME = Frame

    output_path_main = f'{dir}_{data["Dex"][index]["Name"][6:]}_main.tmp'
        
    with open(output_path_main, 'w') as output:
        output.write(vmd_str)

    return output_path_main, frame_count


def JsonToCSVEyes(data, dir, index):
    frame_count = int(0)
    prev_exists_count = 0

    prev_EXP = int(0)
    prev_VALUE = float(0)
    prev_FRAME = int(0)
    vmd_str = """"""

    for i in data['Dex'][index]['Eyes']:
        Frame = i['F']
        ID = i['I']
        Value = i['V']
        Trans = i['T']

        if prev_exists_count == 0:
            vmd_str += f'{ID},{Frame},{float(Value)}\n'
            prev_EXP = int(ID)
            prev_VALUE = int(Value)
            prev_FRAME = int(Frame)
            prev_exists_count = 1

            frame_count += 1

        elif prev_exists_count == 1:
            if ID == prev_EXP:
                vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                vmd_str += f'{prev_EXP},{Frame + Trans},{Value}\n'

                frame_count += 2
            elif ID != prev_EXP:
                vmd_str += f'{prev_EXP},{Frame},{prev_VALUE}\n'
                vmd_str += f'{prev_EXP},{Frame + Trans},0.0\n'
                vmd_str += f'{ID},{Frame},{float(0)}\n'
                vmd_str += f'{ID},{Frame + Trans},{float(Value)}\n'

                frame_count += 4

            prev_EXP = ID
            prev_VALUE = Value
            prev_FRAME = Frame

    output_path_main = f'{dir}_{data["Dex"][index]["Name"][6:]}_eyes.tmp'

    with open(output_path_main, 'w') as output:
        output.write(vmd_str)

    return output_path_main, frame_count
