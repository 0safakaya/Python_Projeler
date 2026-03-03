import json
import os
import hashlib
import base64

DOSYA_ADI = "vault.json"


# -------------------- Yardımcı Fonksiyonlar --------------------

def sifre_hashle(sifre):
    """Şifreyi SHA256 ile hashler."""
    return hashlib.sha256(sifre.encode()).hexdigest()


def veri_yukle():
    """Vault dosyasını yükler."""
    if not os.path.exists(DOSYA_ADI):
        return None
    with open(DOSYA_ADI, "r", encoding="utf-8") as f:
        return json.load(f)


def veri_kaydet(veri):
    """Vault dosyasına veriyi kaydeder."""
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=4)


def metin_sifrele(metin):
    """Metni base64 ile şifreler."""
    return base64.b64encode(metin.encode()).decode()


def metin_coz(sifreli_metin):
    """Şifreli metni çözer."""
    return base64.b64decode(sifreli_metin.encode()).decode()


# -------------------- İlk Kurulum --------------------

def ilk_kurulum():
    print("🔐 İlk kullanım - Ana şifre oluşturun")
    sifre = input("Yeni ana şifre belirleyin: ")
    sifre_tekrar = input("Şifreyi tekrar girin: ")

    if sifre != sifre_tekrar:
        print("Şifreler uyuşmuyor!")
        return False

    veri = {
        "password": sifre_hashle(sifre),
        "notes": []
    }

    veri_kaydet(veri)
    print("✔️ Vault oluşturuldu!")
    return True


# -------------------- Giriş Kontrol --------------------

def giris_yap():
    veri = veri_yukle()
    if not veri:
        return False

    sifre = input("Ana şifreyi girin: ")
    if sifre_hashle(sifre) == veri["password"]:
        print("✔️ Giriş başarılı!")
        return True
    else:
        print("❌ Hatalı şifre!")
        return False


# -------------------- Not İşlemleri --------------------

def not_ekle():
    veri = veri_yukle()
    baslik = input("Not başlığı: ")
    icerik = input("Not içeriği: ")

    sifreli_icerik = metin_sifrele(icerik)

    veri["notes"].append({
        "title": baslik,
        "content": sifreli_icerik
    })

    veri_kaydet(veri)
    print("✔️ Not kaydedildi!")


def notlari_listele():
    veri = veri_yukle()

    if not veri["notes"]:
        print("Henüz kayıtlı not yok.")
        return

    print("\n📂 Kayıtlı Notlar:\n")

    for i, not_item in enumerate(veri["notes"], 1):
        cozulmus = metin_coz(not_item["content"])
        print(f"{i}. {not_item['title']}")
        print(f"   İçerik: {cozulmus}\n")


# -------------------- Menü --------------------

def menu():
    while True:
        print("\n===== ŞİFRELİ NOT KASASI =====")
        print("1 - Not Ekle")
        print("2 - Notları Listele")
        print("3 - Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_listele()
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")


# -------------------- Ana Çalışma --------------------

if __name__ == "__main__":
    if not os.path.exists(DOSYA_ADI):
        if ilk_kurulum():
            if giris_yap():
                menu()
    else:
        if giris_yap():
            menu()