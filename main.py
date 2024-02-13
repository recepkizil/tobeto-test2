print("Merhaba Tobeto Test Ekibi")

##degiskenler
##herhangi bir metinsel ifade olabilir. metinsel, numerik, obje. bunda değişiklik yapınca her yerde değişmiş oluyor

text="Hello " ##değisken
kullaniciAdi="Irem" #degisken
print(text+kullaniciAdi) 
print(text+ " " + kullaniciAdi) #boşluğu bu şekilde de ekleyebiliriz
totalText= text+ " "+ kullaniciAdi # böyle de yapılabilir
print(totalText)

totalText = " {message} Sayın {name} " . format ( message = "Hello" , name = kullaniciAdi )



#f-string
totalText = f"Hoşgeldiniz {kullaniciAdi}" 
print(totalText)
print(type(totalText))
# üsttekiler de dahil bu yaptıklarımıza string interpolation - metin birleştirme de denir

#kodlar yukardan aşağı okunduğu için değişken yukarda olmalı. 

studentCount= "45" #string
studentCount1= 5 #integer => tam sayi

print(studentCount +"5") #sonuc 455 oldu

studentCount = 5 #integer
print(studentCount + 5)

#her zaman tam sayı tutmak istemeyiz

averagePoint = 25.5 #double - decimal- float => ondalıklı sayı
print(averagePoint + 5)

isVerified = True # boolean #son veritipimiz budur. 
print(isVerified)

#tanımladığımız değişkenlerin tipini görmek için bu komutu kullanırız
print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))


#operatörler
#matematiksel operatörler
number = 10 
print(10 + 10)
print(number+ number) #toplama işlemi #iksi aynı anlama geliyor, aynı sonucu veriyor
print(number - 5) 
print(number / 2)
print(number * 3) 

print(number % 3) #mod operatörüdür. sol taraftaki değerin sağ taraftaki değere bölümünden kalan sonuç  

#mantıksal operatörler -- diğer adıyla karlıaştırma operatörler
print(number == 10) #number 10a eşit mi? cevap true oldu
print (number == 11) #cevap false

print(number != 10) #eşit olmama durumunu sorguluyoruz cevap false
print(number != 11) #cevap true 

print(number > 10) #false sayı 10dan büyük değil
print(number >= 10) #true sayı 10a eşit veya daha büyük

print(number < 10) #false
print(number <= 10) #true


#değişkenleri tek tek tanımlamak yerine listeleyebiliriz. diğer dosyada devam

