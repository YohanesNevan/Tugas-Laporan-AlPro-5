def konvergen(start):
    suku = start
    while suku != 1:
        print(suku)
        if suku % 2 == 0:
            suku = suku // 2
        else:
            suku = suku * 3 + 1
start = int(input('Masukan suku pertama dari deret konvergen: '))
konvergen(start)