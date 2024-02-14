#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Lütfen boyunuzu girin:"))
kilo = float(input("Lütfen kilonuzu girin:"))

vki = kilo / (boy ** 2)

print("Vücut kitle endeksiniz:", "{:.2f}".format(vki))

if vki < 18.5:
    print("Zayıf")
elif 18.5<= vki <24.9:
    print("Normal")
elif 24.9<= vki <29.9:
    print("Kilolu")
else:
    print("Obez")


##2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("Lütfen maaşınızı girin:"))
zam_orani = float(input("Lütfen zam oranını girin:"))

zamli_maas = maas + (maas * zam_orani/100)

print("Xamlı maaşınız:", zamli_maas)


##3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = float(input("Lütfen birinci sayıyı girin: "))
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))
sayi3 = float(input("Lütfen üçüncü sayıyı girin: "))
en_buyuk_sayi = max(sayi1, sayi2, sayi3)
print("En büyük sayı:", en_buyuk_sayi)

##4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

import math
yaricap = float(input("Lütfen dairenin yarıçapını girin"))

alan = math.pi * yaricap**2

cevre = 2 * math.pi * yaricap

print("Dairenin alanı: {:.2f}".format(alan))
print("Dairenin çeversi: {:.2f}".format(cevre))

##5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Lürfen bir sayı girin:")

ters_sayi = sayi[::-1]

if sayi == ters_sayi:
    print("Bu sayı bir palindromdur")
else:
    print("Bu sayı bir palindrom değildir")