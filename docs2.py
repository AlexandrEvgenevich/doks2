import os.path

texts = {}
res_file = []


def reader(file, mode, encoding):
    opb = os.path.basename(file)
    opnfil = open(file, mode=mode, encoding=encoding)
    filrl = opnfil.readlines()
    opnfil2 = open(file, mode=mode, encoding=encoding)
    lines = 0
    for z in filrl:
        lines += 1
    return texts.update({lines: [opb, opnfil2.read()]})


def worker(data):
    b = []
    for a in data.keys():
        b.append(a)
    b.sort()

    for c in b:
        if c in data.keys():
            x = data[c]

            res_file.append(x[0])
            res_file.append(c)
            res_file.append((x[1]))


def writer(data):
    for x in data:
        y = str(x)
        with open('text.txt', 'a') as file:
            file.write(f"{y}\n")


reader('txts/txt1.txt', 'r', 'utf-8')
reader('txts/txt2.txt', 'r', 'utf-8')
reader('txts/txt3.txt', 'r', 'utf-8')

worker(texts)
writer(res_file)
