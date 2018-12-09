import time

print('Basit Not Hesaplama Programı')
print('Not: vize notunu %30 final notunu %70'"\n")

print('Lütfen isminizi giriniz:'"\n")
myName = input()
print('Merhaha , ' + myName)
print("\n")

vize = float(input(' Lütfen vize notunuzu giriniz : '))
final = float(input('Lütfen final notunuzu giriniz : '))

print("\n")
ortalama=(float(vize)*0.3)+(float(final)*0.7)

if final>=50:
    if(ortalama>=85 and final>=50):
        print("Harf Notunuz AA GEÇTİNİZ  " +myName)
    elif ortalama>=75 and ortalama<85 :
        print("Harf Notunuz BA GEÇTİNİZ  " +myName)
    elif ortalama>= 70 and ortalama < 75:
        print("Harf Notunuz BB GEÇTİNİZ " +myName)
    elif ortalama >= 65 and ortalama < 70:
        print("Harf Notunuz CB GEÇTİNİZ  " +myName)
    elif ortalama >= 60 and ortalama < 65:
        print("Harf Notunuz CC GEÇTİNİZ  " +myName)
    elif ortalama >= 55 and ortalama < 60:
        print("Harf Notunuz DC KOŞULLU GEÇTİNİZ  " +myName)
    elif ortalama >= 50 and ortalama < 55:
        print("Harf Notunuz DD KOŞULLU GEÇTİNİZ " +myName)	
    
else:
    print("Harf notunuz FF KALDINIZ " +myName )
	

print("Ortalama :{0} ".format(ortalama))
print("\n")




time.sleep(7)
