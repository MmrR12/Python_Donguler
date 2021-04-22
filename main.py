sayilar = [1,2,3,4,5,6] # Normalde böyle bir listenin her karakterini tek tek yazdırmak istesek şunu yapardık
                        # print(sayilar[0])
                        # print(sayilar[1]) ... diye devam eder ancak for döngüsüyle bunu daha kolay yapabiliriz.
for sayi_yaz in sayilar:
    print(sayi_yaz)   # Burada yaptığımız şey şu: for yazarak döngüyü başlatıyoruz daha sonra herhangi bir değişken tanımlıyoruz
                      # burada sayi_yaz diye bir değişken tanımladık (farklı bir değişkende tanımlayabilirsin) daha sonra in yazdık
                      # yani içine koy demek neyi içine koyacak sayilar listesinden aldığı değeri sayi_yaz değişkenine koyacak
                      # daha sonra print(sayi_yaz) ile bunu yazdıracak.Bu her defasında gerçekleşecek taki sayilar listesindeki eleman
                      # bitene kadar
for yazdir in sayilar:
    print("Merhaba") # Burada yaptığımız şey ise şu: yazdir değişkenine her defasında sayilar bir değer tanımlanıyor
                     # daha sonra Merhaba yazdırılıyor.Bu sayilar listesindeki değerler bitene kadar devam eder.

harf = ["n","m","r"]
for y_yazdir in harf: # Gördüğün gibi burada yaptığımız şey yukarıdakiyle aynı anlatmak istediğim şey şu y_yazdir değikenine harf
    print("Maraba")   # listesinden değer atanıyor daha sonra Maraba yazdırılıyor yukarıdakiyle aynı işlemi yapıyor ama fark ettiysen
                      # harf listesinde harfler var sayılar değil yani döngüde bir Maraba ifadesinin yazdırılması için bir sayı değerine
                      # gerek yok harf değerleri her y_yazdir ın içerisine atıldığında Maraba yazdırılıyor.

isimler = ["Muhammed","Resul","Ayşe"]       # Şimdi burada fark ettiysen her isimler listesindeki değer tanis değişkenine atandı
for tanis in isimler:                       # daha sonra aşağıdaki print ifadesiyle her defasında yazdırıldı ve tanis a atanan değişken
    print(f"Merhaba benim adım {tanis}")    # ismi yazdırıldı.

isim = "Muhammed Özden"
for parcala in isim:  # Gördüğün gibi burada isim değişkenindeki string ifadeyi aldı her karakterine parçaladı ve parcala değikenine
    print(parcala)    # atayıp daha sonra yazdırdı.

tuple = [(1,2), (4,5), (7,8)]
for l_deger in tuple: # Gördüğün gibi burada tuple listesindeki her değeri aldı l_deger değişkenine atadı ve daha sonra yazdırdı
    print(l_deger)

for s_d, i_d in tuple:  # sıfırıncı değer = s_d   # ilk_değer = i_d
    print("Sıfırıncı değerleri :",s_d)   # Burada tuple listesinin içerisindeki değişkenleri aldık ve s_d i_d diye ikiye ayırdık
    print("İlk değerleri : ",i_d)       # her ayırdığımız değeri yazdırdık.


sozluk = {"anahtar1" : "L", "anahtar2" : "K", "anahtar3" : "M"} # Burada sozluk tanımlayıp içerisine anahtar:değer (key:value) ikilileri tanımladım

for anahtar_satin_al in sozluk: # Fark ettiysen kodun çıktısında sadece sozluk değişkenindeki anahtar(key) geldi eşitlediğimiz değer(value) bilgisi gelmedi
    print(anahtar_satin_al)     # oysa ki tuple adlı listemizden değerleri çektiğimizde her ikili de gelmişti ama sözlük yapılarında bu işe yaramıyor
                                # başka yöntem kullanmamız lazım

for anahtar_satin_al in sozluk.items():
    print(anahtar_satin_al) # Eveet bu kodu yazarak yukarıdaki koddan farklı olarak anahtar:değer (key:value) ikililerini de aynı anda getirdik
                            # burada sozluk.items() parametresini kullanarak anahtarlar(keylerin) değerlerine(valuelerine) de ulaştık ve
                            # her zaman olduğu gibi anahtar_satin_al değişkenine tek tek atıp yani tanımlayıp hepsini tek tek yazdırdık.