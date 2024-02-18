sayilar = [100, 200, 300,"Merhaba",True, 15.5]

print(sayilar[1]) #sayılar kısmında birinci değeri yaz demek
#sonuc 200 çıkıyor çünkü programcılar saymaya 0'dan başlıyor
print(sayilar[0]) #sonuc 100 çıkar

print(sayilar) 

sayilar.append(400) #append yazdığımız şeyi listenin sonuna ekler
print(sayilar) 

sayilar.remove("Merhaba") #değere göre silme işlemi
print(sayilar) 

sayilar.pop() #verdiğimiz indexe göre siliyor. vermezsek varsayılan olarak sonuncuyu siliyor
print(sayilar) 
sayilar.pop(2) #2.değeri siler yani 300'ü
print(sayilar) 


add=[700,800,900]
sayilar.extend(add) #ekleme yapar
print(sayilar)

sayilar.extend(700,800,900) #bu da çalışır  
print(sayilar)


sayilar.clear() #listedeki tüm elemanları siler
print(sayilar)







