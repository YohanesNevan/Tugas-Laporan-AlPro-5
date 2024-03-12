def avarage():
    total = 0
    count = 0
    while True:
        input_user = int(input('Masukan nilai (nol atau negatif untuk berhenti): '))
        if input_user < 1 :
            break
        else:
            total = total + input_user
            count = count + 1
    if count > 0:
        return total / count
    else:
        return 0
    
hasil = avarage()
print('Rata-rata: ', hasil)