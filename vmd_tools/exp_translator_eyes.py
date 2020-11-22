from sys import argv

def TranslateEyes(input, dir):
    path = dir + '_eyes_translate.tmp'
    with open(dir + '_eyes_translate.tmp', 'w', encoding='Shift-JIS') as output:
        for line in input:
            data = line.split(',')
            if len(data) == 3: #which it always is
                expression = int(data[0])
                if expression == 3: #which it always is
                    data[0] = 'まばたき'
                    output.write(f'{data[0]},{data[1]},{data[2]}')
    return path