ortalamaNot = int(input("Lütfen ortalamanizi giriniz:"))

print(type(ortalamaNot))

if ortalamaNot >50:
    print("Başarili")
    if ortalamaNot >80:
        print("Bravoo!!!")
elif ortalamaNot >40:
    print("ortalama notunuz var")
else:
    print("Kaldiniz")

##print("if bloğundan bağimsiz bi kisim")
##iki seçenekten fazla koşul varsa elif kullanırız
#else bir tane yazılır, diğerleri birkaç tane yazılabilir 
    
if ortalamaNot >85 and ortalamaNot <100:
    print("Başarili")
    print("Bravoo!!!")
elif ortalamaNot >70 and ortalamaNot<85:
    print("ortalama notunuz var")
else:
    print("Kaldiniz")
 
 #and ile böyle yazılırdi
    
