#ik itemel döngü var. while ve for

#for döngüsü

#for i in range(1,11):
    #print(i)

#start: döngü kaç sayısından başlasın demek. default olarak 0.
#stop: döngü kaç kere tekrar etsin. bunu vermek  durumundayız   
#step: döngü kaç kaç arttırılsın. bunda default 1.
#bunları parantez içine yazıcaz. (1,10.2) gibi. ilk parametreyi vermezsek sonu da görmüyor

    
#kullanıcının vereceği üst limit ile alt limitten 
#bu üst limite kadar olan tüm çift sayıları ekrana yazdıralım
#forRangeMin = int(input("Döngünün alt limitini belirleyiniz"))
#forRangeMax = int(input("Döngünün üst limitini veriniz"))

#for i in range(forRangeMin, forRangeMax+1):
    #if i % 2 ==0:
        #print(i)

#2ye bölümünden kalan sıfır olanlar çift sayıdır. 
#sonuna artı 1 yazarsak yazdığımız max min'i de dahil eder. 


#kullanıcının girdiği sayılar arasındaki en büyüğü bulan program yazınız
#önce kullanıcıdan 5 sayı alalım
""" biggestValue = 0
for i in range(5):
    sayi = int(input(f"{i+1}. sayiyi giriniz"))
    if sayi > biggestValue:
        biggestValue = sayi

print(f"Girdiğiniz sayilar arasinda en büyük olani: {biggestValue}") """

#bunu dizilerle yapmak isteseydik

""" sayilar =[]
for i in range(5):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz"))) 

sayilar.sort(reverse=True) #desc oldu. defauletu küçükten büyüğe çünkü.
print(min(sayilar))
print(max(sayilar)) """


#başka örnek

students = ["Ahmet", "Tuba", "Abdullah", "Onur", "Dilara"]
#lengt=uzunluk
print(len(students)) #dizenin içindeki eleman sayısını bulduk

""" for i in range(len(students)):
    if i>3:
        break
    print(f"{i+1}. Öğrenci: {students[i]}")   """

#+1 koyunca 0.öğrenci değil birinci öğrenci olarak yazdı. güzelleştirmek için yaptık.
#break: ilgili döngünün o anda kırılmasını sağlar
""" 
for i in students:
    print(f"Öğrenci: {i}")  """#bu farklı şekilde döndürdü

#continue: iterasyondaki current değeri atla bir sonraki değer ile devam et

""" for i in students:
    if i == "Tuba":
        continue

print(f"Öğrenci:{i}") """


##WHILE DONGUSU

i=0
while i<10:
    print("Merhaba")
    i+=2 

#fonksiyonlar ve class yapılarına çalış haftaya için    