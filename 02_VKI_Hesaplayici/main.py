# 02_VKI_Hesaplayici/main.py

def vki_hesapla():
    boy = float(input("Boyunuzu metre cinsinden girin (Örn: 1.75): "))
    kilo = float(input("Kilonuzu kilogram cinsinden girin (Örn: 75): "))

    vki = kilo / (boy ** 2)
    print(f"\nSonuç: VKİ Değeriniz {vki:.2f}")

    # Basit bir veri sınıflandırması
    if vki < 18.5:
        durum = "Zayıf"
    elif 18.5 <= vki < 25:
        durum = "Normal"
    elif 25 <= vki < 30:
        durum = "Fazla Kilolu"
    else:
        durum = "Obez"

    print(f"Kategori: {durum}")


if __name__ == "__main__":
    vki_hesapla()