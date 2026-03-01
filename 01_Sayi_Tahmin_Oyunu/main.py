import random


def oyun_baslat():
    # 1 ile 100 arasında rastgele bir sayı seçiyoruz
    hedef_sayi = random.randint(1, 100)
    deneme_hakki = 7

    print("--- Sayı Tahmin Oyununa Hoş Geldin Patron ---")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

    while deneme_hakki > 0:
        try:
            tahmin = int(input(f"\nKalan Hakkın: {deneme_hakki} | Tahminin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı gir patron!")
            continue

        if tahmin == hedef_sayi:
            print(f"Tebrikler! {8 - deneme_hakki}. denemede bildin. 🎉")
            break
        elif tahmin < hedef_sayi:
            print("Daha YÜKSEK bir sayı söyle.")
        else:
            print("Daha DÜŞÜK bir sayı söyle.")

        deneme_hakki -= 1

    if deneme_hakki == 0:
        print(f"\nMaalesef hakların bitti patron. Sayı şuydu: {hedef_sayi}")


if __name__ == "__main__":
    oyun_baslat()