import random


def get_number():
    while True:
        try:
            sayi = int(input("Sayı tahminini gir: "))
            if(sayi < 1 or sayi > 100):
                print("Lütfen 1 - 100 arasında gir")
            else:
                return sayi
        except ValueError:
            print("Lütfen geçerli bir sayı girin")


def game():
    random_sayi = random.randint(1, 100)

    kalan_hak = 10
    deneme_sayisi = 0
    bilinebildi_mi = False

    while kalan_hak > 0 and bilinebildi_mi == False:
        tahmin = get_number()
        deneme_sayisi +=1
        kalan_hak -=1

        if tahmin > random_sayi:
            print("Random sayı tahmininden daha küçük.")
            print(f"{kalan_hak} hakkın kaldı.")
        elif tahmin == random_sayi:
            print("Sayıyı bildin!")
            bilinebildi_mi = True
        else:
            print("Random sayı tahmininden daha büyük.")
            print(f"{kalan_hak} hakkın kaldı.")

        print("--------------")

    if bilinebildi_mi == False:
        print(f"Hakkın bitmesine rağmen sayıyı bilemedin. Gerçek sayı = {random_sayi}")


while True:
    print("Oyun başladı.")

    game()


    tekrar = input("Tekrar oynamak ister misin? (E/H): ").upper()

    if tekrar != "E":
        break