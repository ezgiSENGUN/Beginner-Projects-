#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def toplama(sayi1, sayi2):
    return sayi1 + sayi2

def cikarma(sayi1, sayi2):
    return sayi1 - sayi2

def bolme(sayi1, sayi2):
    return sayi1 / sayi2

def carpma(sayi1, sayi2):
    return sayi1 * sayi2

print("İşlemi Seçiniz \n",
      "1. Toplama \n",
      "2. Çıkarma \n",
      "3. Bölme \n",
      "4. Çarpma")

islem_secimi = int(input("Yapacağınız işlemi 1, 2, 3, 4 şeklinde giriniz: "))

if islem_secimi >= 5 or islem_secimi < 1:
    print("Hata!")

else:
    sayi1 = int(input("İlk Sayıyı Giriniz: "))

    sayi2 = int(input("İkinci Sayıyı Giriniz: "))


    

if islem_secimi ==1:
    print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
    
    
elif islem_secimi ==2:
    print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
    
    
elif islem_secimi ==3:
    print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
    


elif islem_secimi ==4:
    print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
    
    

