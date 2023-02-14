sayi = float(input("Sayi 1 giriniz: "))
sayi2 = float(input("Sayi 2 giriniz: "))
print("""
----------
1-TOPLAMA
2-ÇIKARMA
3-ÇARPMA
4-BÖLME      
-----------      
""")
seçenek = float(input("Seçenek giriniz: "))
if (seçenek ==1):
    print("Toplama: ", sayi + sayi2)
elif (seçenek==2):
    print("Çikarma: ", sayi - sayi2)
elif (seçenek==3):
    print("Çarpma: ", sayi * sayi2)
elif (seçenek==4):
    print("Bölme: ", sayi / sayi2)
else:
    print("Böyle Bir seçenek yok")


