import random


def balikTut():
    # burada boş bulunmasının sebebi boş değeri gelince ıska olarak görüp balık yakalamadığınızı dönecek.
    a = {1: "Levrek",
         2: "Sardalya",
         3: "Hamsi",
         4: "Ton Balığı",
         5: "boş"
         }
    balik_miktari = 0
    cevap = input("Balık tutmak ister misiniz? : ")
    if cevap == "evet" or cevap == "Evet" or cevap == "EVET" or cevap == "eVET":
        print("Olta atılıyor...")
        # Rastgele 1-5 arası sayıları çekiyorum. 5 değeri boş çekmeyi temsil ediyor.
        # Gelen değerler hangi balığın tutulduğunu gösteriyor.
        b = random.randint(1, 5)
        if b == int(b):
            # get fonksiyonu ile veride 1 2 3 4 5 şeklinde etiketlenen değerleri çekiyorum.
            c = a.get(b)
            if c == "boş":
                print("Maalesef oltadaki yem ile balıkları beslediniz.")
                print("Balık Miktarı: ", balik_miktari)
            else:
                balik_miktari += 1
                print("Tebrikler! Balık yakaladınız. Yakaladığınız balık: ", c)
                print("Balık Miktarı: ", balik_miktari)

    elif cevap == 'Hayır' or cevap == 'hayır' or cevap == 'hAYIR' or cevap == 'HAYIR':
        print("Bugün balık tutmak istemiyorsunuz. Teşekkürler. İyi günler")

    else:
        print("Hatalı değer girişi yaptınız. Lütfen evet/hayır cevabı verin.")


balik = balikTut()
balik


