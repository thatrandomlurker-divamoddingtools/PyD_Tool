import struct, diva_tools.dex, json, misc.ulsr

class VMD_Morph(object):
    def VMD_Morph(self):
        self.Name = b''
        self.Frame = int()
        self.Value = int()


def Read_Main_Morphs_to_EXP(dex_main_f, dex_eyes_f, json_file):
    # I hate this code, and i know everyone else will hate this code
    # But i need some way to load all the possible expressions into their own lists
    # And to do that i need to make the lists
    # If i knew how to do this on the fly i would, but i don't
    kanashii_frames = []
    warai_frames = []
    pikkuri_frames = []
    kantan_frames = []
    eyesmile_frames = []
    mabushii_frames = []
    tsuyoi_frames = []
    meikakunisuru_frames = []
    yasashii_frames = []
    nagashi_frames = []
    kiri_frames = []
    utsuro_frames = []
    kangaeru_frames = []
    setsuna_frames = []
    genki_frames = []
    yaru_frames = []
    mabataki_frames = []
    cool_frames = []
    kumon_frames = []
    kutsuu_frames = []
    naki_frames = []
    nayami_frames = []
    pikkuri2_frames = []
    wink2_frames = []
    wink2r_frames = []
    wink_frames = []
    winkr_frames = []
    diva_frames = []

    file_version = dex_main_f.read(30).decode("Shift-JIS")
    model_name = dex_main_f.read(20).decode("Shift-JIS")
    bone_keyframes = struct.unpack("I", dex_main_f.read(4))[0]
    # Won't bother to write bone reading code yet
    face_keyframes = struct.unpack("I", dex_main_f.read(4))[0]

    for i in range(0, face_keyframes):
        morph = VMD_Morph()
        try:
            name = dex_main_f.read(15).decode('Shift-JIS').split('\x00')[0]
        except UnicodeDecodeError:
            print('Ok, this is weird... this should not happen... oh well')
            name = "broken"
            pass
        morph.Name = str(name)
        morph.Frame = struct.unpack("I", dex_main_f.read(4))[0]
        morph.Value = struct.unpack("f", dex_main_f.read(4))[0]
        if morph.Name == "悲しい":
            kanashii_frames.append(morph.__dict__)
        elif morph.Name == "笑い":
            warai_frames.append(morph.__dict__)
        elif morph.Name == "ぴっくり":
            pikkuri_frames.append(morph.__dict__)
        elif morph.Name == "感嘆":
            kantan_frames.append(morph.__dict__)
        elif morph.Name == "アイスマイル":
            eyesmile_frames.append(morph.__dict__)
        elif morph.Name == "眩しい":
            mabushii_frames.append(morph.__dict__)
        elif morph.Name == "強い":
            tsuyoi_frames.append(morph.__dict__)
        elif morph.Name == "明確にする":
            meikakunisuru_frames.append(morph.__dict__)
        elif morph.Name == "優しい":
            yasashii_frames.append(morph.__dict__)
        elif morph.Name == "ながし":
            nagashi_frames.append(morph.__dict__)
        elif morph.Name == "キリッ":
            kiri_frames.append(morph.__dict__)
        elif morph.Name == "ウツロ":
            utsuro_frames.append(morph.__dict__)
        elif morph.Name == "考える":
            kangaeru_frames.append(morph.__dict__)
        elif morph.Name == "せつな":
            setsuna_frames.append(morph.__dict__)
        elif morph.Name == "元気":
            genki_frames.append(morph.__dict__)
        elif morph.Name == "ヤル":
            yaru_frames.append(morph.__dict__)
        elif morph.Name == "まばたき":
            mabataki_frames.append(morph.__dict__)
        elif morph.Name == "クール":
            cool_frames.append(morph.__dict__)
        elif morph.Name == "くもん":
            kumon_frames.append(morph.__dict__)
        elif morph.Name == "くつう":
            kutsuu_frames.append(morph.__dict__)
        elif morph.Name == "なき":
            naki_frames.append(morph.__dict__)
        elif morph.Name == "なやみ":
            nayami_frames.append(morph.__dict__)
        elif morph.Name == "ぴっくり２":
            pikkuri2_frames.append(morph.__dict__)
        elif morph.Name == "ウィンク２":
            wink2_frames.append(morph.__dict__)
        elif morph.Name == "ｳｨﾝｸ２右":
            wink2r_frames.append(morph.__dict__)
        elif morph.Name == "ウィンク":
            wink_frames.append(morph.__dict__)
        elif morph.Name == "ウィンク右":
            winkr_frames.append(morph.__dict__)

    # Lets begin adding
    # SAD
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kanashii_frames):
            break
        src1 = kanashii_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 0
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kanashii_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 0
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # LAUGH
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(warai_frames):
            break
        src1 = warai_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 1
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = warai_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 1
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # pikkuri
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(pikkuri_frames):
            break
        src1 = pikkuri_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 3
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = pikkuri_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 3
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # ADMIRATION
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kantan_frames):
            break
        src1 = kantan_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 5
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kantan_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 5
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # eyesmile
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(eyesmile_frames):
            break
        src1 = eyesmile_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 6
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = eyesmile_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 6
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # mabushii
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(mabushii_frames):
            break
        src1 = mabushii_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 8
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = mabushii_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 8
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # tsuyoi
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(tsuyoi_frames):
            break
        src1 = tsuyoi_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 10
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = tsuyoi_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 10
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # meikakunisuru
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(meikakunisuru_frames):
            break
        src1 = meikakunisuru_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 11
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = meikakunisuru_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 11
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # yasashii
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(yasashii_frames):
            break
        src1 = yasashii_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 12
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = yasashii_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 12
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # nagashi
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(nagashi_frames):
            break
        src1 = nagashi_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 13
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = nagashi_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 13
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # kiri
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kiri_frames):
            break
        src1 = kiri_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 15
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kiri_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 15
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # utsuro
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(utsuro_frames):
            break
        src1 = utsuro_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 16
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = utsuro_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 16
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # kangaeru
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kangaeru_frames):
            break
        src1 = kangaeru_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 17
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kangaeru_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 17
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # setsuna
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(setsuna_frames):
            break
        src1 = setsuna_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 18
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = setsuna_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 18
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # genki
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(genki_frames):
            break
        src1 = genki_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 19
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = genki_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 19
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # yaru
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(yaru_frames):
            break
        src1 = yaru_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 20
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = yaru_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 20
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # mabataki
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(mabataki_frames):
            break
        src1 = mabataki_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 22
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = mabataki_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 22
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # cool
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(cool_frames):
            break
        src1 = cool_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 34
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = cool_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 34
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # kumon
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kumon_frames):
            break
        src1 = kumon_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 36
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kumon_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 36
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # kutsuu
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(kutsuu_frames):
            break
        src1 = kutsuu_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 37
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = kutsuu_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 37
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # naki
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(naki_frames):
            break
        src1 = naki_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 38
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = naki_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 38
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # nayami
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(nayami_frames):
            break
        src1 = nayami_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 39
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = nayami_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 39
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # pikkuri2
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(pikkuri2_frames):
            break
        src1 = pikkuri2_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 40
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = pikkuri2_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 40
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # wink2
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(wink2_frames):
            break
        src1 = wink2_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 42
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = wink2_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 42
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # wink2r
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(wink2r_frames):
            break
        src1 = wink2r_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 43
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = wink2r_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 43
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # wink
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(wink_frames):
            break
        src1 = wink_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 44
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = wink_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 44
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # winkr
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(winkr_frames):
            break
        src1 = winkr_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 45
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = winkr_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 0
            df.I = 45
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        diva_frames.append(df.__dict__)

    # diva_frames sorting code
    frame_sorter = []
    while True:
        if len(diva_frames) == 0:
            break
        highest = int(0)
        highest_index = int(0)
        for frame in diva_frames:
            if frame["F"] == highest:
                frame_sorter.pop(-1)
                frame_sorter.append(frame)
            elif frame["F"] > highest:
                highest = frame["F"]
                highest_index = int(diva_frames.index(frame))
        frame_sorter.append(diva_frames[highest_index])
        diva_frames.pop(highest_index)

    # and last but not least, let's reverse the list
    frames = []
    finish_tracker = int(len(frame_sorter) - 1)
    while True:
        if finish_tracker < 0:
            break
        frame = frame_sorter[finish_tracker]
        finish_tracker -= 1
        frames.append(frame)

    # Now to perform operations on the eyes section
    blink_frames = []
    eyes_frames = []

    file_version = dex_eyes_f.read(30).decode("Shift-JIS")
    model_name = dex_eyes_f.read(20).decode("Shift-JIS")
    bone_keyframes = struct.unpack("I", dex_eyes_f.read(4))[0]
    # Won't bother to write bone reading code yet
    face_keyframes = struct.unpack("I", dex_eyes_f.read(4))[0]

    for i in range(0, face_keyframes):
        morph = VMD_Morph()
        try:
            name = dex_eyes_f.read(15).decode('Shift-JIS').split('\x00')[0]
        except UnicodeDecodeError:
            print('Ok, this is weird... this should not happen... oh well')
            name = "broken"
            pass
        morph.Name = str(name)
        morph.Frame = struct.unpack("I", dex_eyes_f.read(4))[0]
        morph.Value = struct.unpack("f", dex_eyes_f.read(4))[0]
        if morph.Name == "まばたき":
            blink_frames.append(morph.__dict__)
    # blinks
    internal_tracker = int(0)
    while True:
        if internal_tracker >= len(blink_frames):
            break
        src1 = blink_frames[internal_tracker]
        internal_tracker += 1
        if src1["Frame"] == 0 and src1["Value"] == 0:
            continue
        elif src1["Frame"] == 0 and src1["Value"] == 1:
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 1
            df.I = 3
            df.V = src1["Value"]
            df.T = 0
        else:
            src2 = blink_frames[internal_tracker]
            internal_tracker += 1
            df = diva_tools.dex.EXPFrame()
            df.F = src1["Frame"]
            df.B = 1
            df.I = 3
            df.V = src2["Value"]
            df.T = int(src2["Frame"] - src1["Frame"])
        eyes_frames.append(df.__dict__)

    # diva_frames sorting code
    eye_frame_sorter = []
    while True:
        if len(eyes_frames) == 0:
            break
        highest = int(0)
        highest_index = int(0)
        for frame in eyes_frames:
            if frame["F"] > highest:
                highest = frame["F"]
                highest_index = int(eyes_frames.index(frame))
        eye_frame_sorter.append(eyes_frames[highest_index])
        eyes_frames.pop(highest_index)

    # and last but not least, let's reverse the list
    eyeframes = []
    finish_tracker = int(len(eye_frame_sorter) - 1)
    while True:
        if finish_tracker < 0:
            break
        frame = eye_frame_sorter[finish_tracker]
        finish_tracker -= 1
        eyeframes.append(frame)

    # Finally, let's write the file
    dex_main = {"Dex": []}
    meta = {"Name": f"{file_version}", "Main": frames, "Eyes": eyeframes}
    dex_main["Dex"].append(meta)

    json.dump(dex_main, json_file, indent=2)

