for i in range(1, 101):
    print(i)
    
for _ in range(1, 101):
    print("Hello World")
    
for i in range(2, 101, 2):
    print(i)
    
for i in range(100, 1, -2):
    print(i)
    
bilangan = 0
genap = False
while genap == False:
    bilangan = int(input("Masukan bilangan genap= "))
    if bilangan % 2 == 0:
        genap = True
print(bilangan,"yang anda masukan adalah bilanagan genap")

for i in range(1, 11):
    if i == 5:
        break
    else:
        print(i)
print("Selesai")
    
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i)
print("Selesai")
    

    
