def hitung_ips(jumlah_mata_kuliah):
    total_sks = jumlah_mata_kuliah * 3
    total_bobot = 0

    for i in range(1, jumlah_mata_kuliah + 1):
        nilai = input(f'Nilai MK {i} : ')

        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print('Nilai tidak valid. Mohon input A, B, C, atau D.')
            return

        total_bobot += bobot * 3

    ips = total_bobot / total_sks
    return ips

jumlah_mata_kuliah = int(input('Berapa jumlah mata kuliah? '))

hasil_ips = hitung_ips(jumlah_mata_kuliah)

print(f'Nilai IPS Anda semester ini: {hasil_ips:.2f}')
