sayi = int(input("Lütfen asal çarpanlarına ayırmak istediğiniz sayıyı giriniz: "))
asal_carpanlar = []
i = 2
while sayi > 1:
     while sayi % i == 0:
          asal_carpanlar.append(i)
          sayi //= i
i += 1
