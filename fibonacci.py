def fibo(batas):
    bil1 =1
    bil2 =2
    
    if bil1 > bil2:
        print(bil1, end='\t')
        print(bil1, end='\t')
    suku_baru = bil1 + bil2
    while suku_baru < batas:
        print(suku_baru, end='\t')
        
        bil1 = bil2
        bil2 = suku_baru
        suku_baru = bil1 + bil2
batas = int(input('Masukan batas dari deret fibonacci: '))
fibo(batas)