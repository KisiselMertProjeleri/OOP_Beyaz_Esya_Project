class Base:
    def __init__(self, urun_id = 0, ürün_ismi = ""):
        self.urun_id = urun_id
        self.ürün_ismi = ürün_ismi

    def urun_kaydet(self):
        # KUllanicidan ID ve isim bilgilerini alir ve sinifin özelliklerine atar
        self.urun_id = int(input('Ürün ID:'))
        self.ürün_ismi = input('Ürün Ismi: ')
class Urun(Base):
    def __init__(self, urun_id = 0, ürün_ismi = "", ürün_fiyati = 0):
        super().__init__(urun_id, ürün_ismi)
        self.ürün_fiyati = ürün_fiyati

    def urun_kaydet(self):
        super().urun_kaydet()
        self.ürün_fiyati = float(input('Ürün Fiyati: '))

    def ürün_silme(self, ürün_listesi):
        # Parametre olarak verilen ürün listesini siler
        for i in ürün_listesi:
            print(f"{i.urun_id} Idsi olan ismi {i.ürün_ismi}")
            
            # Silmesini istedigimiz ürünnlerin id'sini alalim
            id = int(input('Silenecek Id: '))
            # Liste üzerinden gezinerek silencek ürünü bulup kaldiralim
            for i in ürün_listesi:
                if i.urun_id == id:
                    ürün_listesi.remove(i)
    def Update(self, ürün_listesi):
        # Parametre olarak girilmis ürün listesini görelim
        for i in ürün_listesi:
            print(f"{i.urun_id} olan Id'li ürünün ismi {i.urun_ismi}")

            # Güncellemek istedigi ürün Id'sini soralim
            id = int(input('Güncellenecek ID: '))

            # Liste üzerinde gezinerek güncellenecek ürünün isim ve fiyatini kullanicidan alarak ürünü günceller
            for i in ürün_listesi:
                if i.urun_id == id:
                    i.ürün_ismi = input('Yeni ürün ismi')
                    i.ürün_fiyati = input('Güncel Fiyat: ')
                else:
                    print(f"Ürün Bulunamadi")

class Kategory(Base):
    def __init__(self, ürün_tanimi = ""):
        self.ürün_tanimi = ürün_tanimi

    def urun_kaydet(self):
        super().urun_kaydet()
        self.urun_tanimi = input('Ürün Aciklamasi: ')

class Marka(Base):
    def __init__(self, ürün_markasi = ""):
        self.ürün_markasi = ürün_markasi

    def urun_kaydet(self):
        super().urun_kaydet()
        self.urun_markasi = input('Ürün Markasi: ')

# Ürün, kategori ve marka listelerini olusturalim
ürünler = []
kategoriler =  []
markalar = []

# Örnek bir ürün olusturalim ve bilgilerini kullanicidan alalim
ürün = Urun()
ürün.urun_kaydet()
ürünler.append(ürün)
for i in ürünler:
    print(f"Ürün ID: {i.urun_id} \nÜrün Ismi: {i.urun_ismi}\nÜrün Fiyati: {i.ürün_fiyati}")

ürün.Update(ürünler)

for i in ürünler:
    print(f"Ürün ID: {i.urun_id} \nÜrün Ismi: {i.urun_ismi}\nÜrün Fiyati: {i.ürün_fiyati}")
