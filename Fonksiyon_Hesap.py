def topla(x,y):
    return x+y
def çikar(x,y):
    return x-y
def çarpma(x,y):
    return x*y
def bol(x,y):
    return x/y

print("Yapilacak İşlemi Seçin.")
print("============")
print("1.Toplama")
print("2.Çikarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("Seçiminiz giriniz: ")

sayi1= int(input("Sayi 1 Giriniz: "))
sayi2= int(input("Sayi 2 Giriniz: "))

if secim == '1':
    print(sayi1,"+",sayi2,"=", topla(sayi1,sayi2))
elif secim == '2':
    print(sayi1,"-",sayi2,"=", çikar(sayi1,sayi2))
elif secim == '3':
    print(sayi1,"*",sayi2,"=", çarpma(sayi1,sayi2))
elif secim == '4':
    print(sayi1,"/",sayi2,"=", bol(sayi1,sayi2))
else:
    print("Hatali seçim yaptiniz.")
    

    
    