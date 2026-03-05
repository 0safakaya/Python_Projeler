import requests


def ulke_bilgisi_getir(ulke):
    url = f"https://restcountries.com/v3.1/name/{ulke}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Ülke bulunamadı.")
            return

        data = response.json()[0]

        isim = data["name"]["common"]
        baskent = data.get("capital", ["Bilinmiyor"])[0]
        nufus = data.get("population", "Bilinmiyor")
        bolge = data.get("region", "Bilinmiyor")

        para = list(data.get("currencies", {}).values())[0]["name"] if data.get("currencies") else "Bilinmiyor"

        dil = list(data.get("languages", {}).values())[0] if data.get("languages") else "Bilinmiyor"

        print("\n🌍 Ülke Bilgisi\n")
        print(f"Ülke: {isim}")
        print(f"Başkent: {baskent}")
        print(f"Bölge: {bolge}")
        print(f"Nüfus: {nufus}")
        print(f"Para Birimi: {para}")
        print(f"Dil: {dil}")

    except Exception as e:
        print("Bir hata oluştu:", e)


def main():
    print("🌎 Ülke Bilgi Uygulaması")

    while True:
        ulke = input("\nBilgi almak istediğiniz ülke (çıkmak için q): ")

        if ulke.lower() == "q":
            print("Program kapatılıyor...")
            break

        ulke_bilgisi_getir(ulke)


if __name__ == "__main__":
    main()