class Ogrenci():
    def __init__(self,no,ad,soyad,tez_adi):
        self.no=no
        self.ad=ad
        self.soyad=soyad
        self.tez_adi=tez_adi
        def __tez_ad(self,yeni_tez_adi):
            self.tez_adi=yeni_tez_adi

Tuna=Ogrenci("29","tuna","şenol","python")

print(Tuna.tez_adi)
