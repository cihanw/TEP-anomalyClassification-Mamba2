import pandas as pd
import pyreadr
import os
import glob
from pathlib import Path

# Klasör yollarını tanımlayın
dosya_yolu = Path(r"C:\Users\Bilge\pyTorch\datas\rdata")
cikti_klasoru = Path(r"C:\Users\Bilge\pyTorch\datas\csv")

# Çıktı klasörü yoksa oluşturun (Hata almamak için önemli)
cikti_klasoru.mkdir(parents=True, exist_ok=True)


def rdata_to_csv_converter(klasor_yolu, hedef_klasor):
    arama_deseni = str(klasor_yolu / "*.RData")
    rdata_dosyalari = glob.glob(arama_deseni)

    if not rdata_dosyalari:
        print(f"Hata: Belirtilen yolda dosya bulunamadı: {klasor_yolu}")
        return

    print(f"Bulunan .RData dosya sayısı: {len(rdata_dosyalari)}")

    for rdata_tam_yol in rdata_dosyalari:
        try:
            # 1. Dosyayı oku
            data_dict = pyreadr.read_r(rdata_tam_yol)

            if not data_dict:
                continue

            ilk_nesne_adi = list(data_dict.keys())[0]
            veri_cercevesi = data_dict[ilk_nesne_adi]

            if not isinstance(veri_cercevesi, pd.DataFrame):
                continue

            # --- DÜZELTME BURADA ---
            # Orijinal dosya adını al (örn: TEP_FaultFree_Testing)
            dosya_adi_yalin = Path(rdata_tam_yol).stem

            # Yeni CSV yolunu oluştur (hedef_klasor + dosya_adi + .csv)
            csv_tam_yol = hedef_klasor / f"{dosya_adi_yalin}.csv"
            # -----------------------

            # CSV olarak kaydet
            veri_cercevesi.to_csv(csv_tam_yol, index=False, encoding="utf-8")

            print(f"Başarılı: {os.path.basename(rdata_tam_yol)} -> {csv_tam_yol.name}")

        except Exception as e:
            print(f"Hata: {os.path.basename(rdata_tam_yol)} atlanıyor. Hata: {e}")

    print("\nTüm işlemler tamamlandı.")


# Çalıştır
rdata_to_csv_converter(dosya_yolu, cikti_klasoru)
