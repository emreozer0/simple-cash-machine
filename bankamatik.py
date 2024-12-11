deryaHesap={
    'isim':'Derya',
    'sifre':5901,
    'hesapNo':'1',
    'bakiye':3000,
    'birikimHesabı':7000,
    'krediLimit':5000,
}

emreHesap={
    'isim':'Emre',
    'sifre':3013,
    'hesapNo':'2',
    'bakiye':5000,
    'birikimHesabı':7000,
    'krediLimit':2500,
}

hesaplar=[emreHesap,deryaHesap]
def hesapBul(isim,sifre):
    for hesap in hesaplar:
        if hesap['isim']==isim and hesap['sifre']==sifre:
            return hesap
    else:
        return None


def paraCek(hesap,miktar):
    if hesap['bakiye']>=miktar:
        hesap['bakiye']-=miktar
        print("Başarıyla Para Çekme İşleminiz Tamamlanmıştır.")
        bakiyeSorgulama(hesap)
        yeniİslem(hesap)
    else:
        if hesap['bakiye']+hesap['birikimHesabı']>=miktar:
            birikimHesapOnayi=input("Hesabınızdaki bakiye yetersiz.Ek hesabı kullanmak ister misiniz?")
            if birikimHesapOnayi=="Evet" or birikimHesapOnayi=="EVET" or birikimHesapOnayi=="evet":
                birikimKullanilacakMiktar= miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['birikimHesabı']-=birikimKullanilacakMiktar
                print("Başarıyla Para Çekme İşleminiz Tamamlanmıştır.")
                bakiyeSorgulama(hesap)
                yeniİslem(hesap)
            elif birikimHesapOnayi=="Hayır" or birikimHesapOnayi=="HAYIR" or birikimHesapOnayi=="hayır":
                print("İşlem sonlandırılıyor.")
            else:
                print("Eksik veya hatalı giriş yaptınız.")
        else:
            if hesap['bakiye'] + hesap['birikimHesabı'] + hesap['krediLimit']>=miktar:
                krediLimitSorgula(hesap)
                krediKullanimi=input("Ana ve birikim hesabı bakiyesi yetersiz.Kalan kısmı kredi kullanmak ister misiniz?")
                if krediKullanimi=="Evet" or krediKullanimi=="EVET" or krediKullanimi=="evet":
                    krediMiktar=(miktar-hesap['bakiye']) - hesap['birikimHesabı']
                    hesap['bakiye'] = 0
                    hesap['birikimHesabı'] = 0
                    hesap['krediLimit']-=krediMiktar
                    print(f"Başarıyla kredinizi kullandınız.Güncel borcunuz { -1 *krediMiktar}")
                    yeniİslem(hesap)
                else:
                    print("İşlem sonlandırılıyor.")
            else:
                print("Üzgünüz yetersiz bakiye ve kredi limiti..")

def paraYatır(hesap,miktar):
    hesapSec=int(input("1-Ana Hesap \n2-Birikim Hesabı \n Lütfen işlem yapmak istediğiniz hesabı seçiniz:"))
    if hesapSec==1:
        hesap['bakiye']+=miktar
        print("Başarıyla Para Yatırma İşleminiz Tamamlandı.")
        bakiyeSorgulama(hesap)
        yeniİslem(hesap)
    elif hesapSec==2:
        hesap['birikimHesabı'] += miktar
        print("Başarıyla Para Yatırma İşleminiz Tamamlandı.")
        bakiyeSorgulama(hesap)
        yeniİslem(hesap)
    else:
        print("Hatalı veya eksik tuşlama yaptınız.")
        yeniİslem(hesap)

def bakiyeSorgulama(hesap):
    print(f"Yapılan işlemler sonucu {hesap['hesapNo']} No'lu hesap bakiyeniz:{hesap['bakiye']}TL.Birikim hesap bakiyeniz:{hesap['birikimHesabı']}TL.")

def krediLimitSorgula(hesap):
    print(f"Kredi limitiniz:{hesap['krediLimit']}TL.")

def krediLimitSorgulaMenu(hesap):
    print(f"Kredi limitiniz:{hesap['krediLimit']}TL.")
    yeniİslem(hesap)

def bakiyeSorgulamaMenu(hesap):
    print(f"Ana hesap bakiyeniz:{hesap['bakiye']}TL.\n Birikim hesap bakiyeniz:{hesap['birikimHesabı']}")
    yeniİslem(hesap)

def krediCek(hesap,miktar):
    krediLimitSorgula(hesap)
    if miktar>hesap['krediLimit']:
        print("Limit Yetersiz")
    else:
        hesap['krediLimit']-=miktar
        krediBorc=(-1)*miktar
        print(f"Krediniz başarıyla çekilmiştir.Güncel borcunuz:{krediBorc}TL.")
        yeniİslem(hesap)

def bankaMatik(hesap):
        yapilacakIslem=int(input(f"1-Bakiye Sorgulama\n2-Kredi Limit Sorgulama\n3-Para Çekme\n4-Para Yatırma\n5-Kredi Çekme\nHoş Geldiniz {hesap['isim']}.Lütfen yapmak istediğiniz işlemi tuşlayınız:"))
        if yapilacakIslem==1:
            bakiyeSorgulamaMenu(hesap)
        elif yapilacakIslem==2:
            krediLimitSorgulaMenu(hesap)
        elif yapilacakIslem==3:
            bakiyeSorgulama(hesap)
            miktar=int(input("Çekmek istediğiniz tutarı giriniz:"))
            paraCek(hesap,miktar)
        elif yapilacakIslem==4:
            miktar=int(input("Yatırmak istediğiniz tutarı giriniz:"))
            paraYatır(hesap,miktar)
        elif yapilacakIslem==5:
            krediLimitSorgula(hesap)
            miktar=int(input("Çekmek istediğiniz kredi miktarı."))
            krediCek(hesap,miktar)
        else:
            print("Eksik veya hatalı tuşlama girdiniz.")

def yeniİslem(hesap):
    devam=input("Başka bir işlem yapmak ister misiniz?")
    if devam=="evet" or devam=="Evet" or devam=="EVET":
        bankaMatik(hesap)
    elif devam=="Hayır" or devam=="hayır" or devam=="HAYIR":
        print("İşlem sonlandırılıyor.")
    else:
        print("Hatalı veya eksik giriş yaptınız.işlem sonlandırılıyor.")
isim=input("Lütfen hesap adınızı giriniz:")
sifre=int(input("Lütfen 4 haneli  şifrenizi giriniz(Sadece rakamlar kullanılmalıdır):"))
hesap=hesapBul(isim,sifre)

if hesap:
    bankaMatik(hesap)
else:
    print("Kullanıcı adı veya Şifre hatalı.")





















