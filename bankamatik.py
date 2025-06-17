"""
deryaHesap={
    'isim':'Derya',
    'sifre':5901,
    'hesapNo':'1',
    'bakiye':3000,
    'birikimHesabı':7000,
    'krediLimit':5000,
    'krediBorc':0,
}

emreHesap={
    'isim':'Emre',
    'sifre':2013,
    'hesapNo':'2',
    'bakiye':5000,
    'birikimHesabı':7000,
    'krediLimit':2500,
    'krediBorc':0,
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
        yeniİslem(hesap)
    else:
        hesap['krediLimit']-=miktar
        krediBorc=(-1)*miktar
        hesap['krediBorc']=krediBorc
        print(f"Krediniz başarıyla çekilmiştir.Güncel borcunuz:{hesap['krediBorc']}TL.")
        yeniİslem(hesap)
def krediBorcOde(hesap,miktar):
        hesap['krediBorc']+=miktar
        print(f'Borc yatirildi kalan borc:{hesap['krediBorc']}')

def bankaMatik(hesap):
        yapilacakIslem=int(input(f"1-Bakiye Sorgulama\n2-Kredi Limit Sorgulama\n3-Para Çekme\n4-Para Yatırma\n5-Kredi Çekme \n6-Kredi borç ödeme \nHoş Geldiniz {hesap['isim']}.Lütfen yapmak istediğiniz işlemi tuşlayınız:"))
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
            miktar=int(input("Çekmek istediğiniz kredi miktarı:"))
            krediCek(hesap,miktar)
        elif yapilacakIslem==6:
            print(hesap['krediBorc'])
            miktar = int(input("Odemek istediğiniz kredi miktarini giriniz:"))
            if miktar*(-1)>hesap['krediBorc']:
                print('Fazla miktar girdiniz.')
                yeniİslem(hesap)
            else:
                krediBorcOde(hesap,miktar)
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

"""
deryaAccount = {
    'name': 'Derya',
    'password': 5901,
    'accountNo': '1',
    'balance': 3000,
    'savingsAccount': 7000,
    'creditLimit': 5000,
    'creditDebt': 0,
}

emreAccount = {
    'name': 'Emre',
    'password': 3013,
    'accountNo': '2',
    'balance': 5000,
    'savingsAccount': 7000,
    'creditLimit': 2500,
    'creditDebt': 0,
}

accounts = [emreAccount, deryaAccount]

def findAccount(name, password):
    for account in accounts:
        if account['name'] == name and account['password'] == password:
            return account
    else:
        return None

def withdrawMoney(account, amount):
    if account['balance'] >= amount:
        account['balance'] -= amount
        print("Your withdrawal transaction was successfully completed.")
        checkBalance(account)
        newTransaction(account)
    else:
        if account['balance'] + account['savingsAccount'] >= amount:
            savingsApproval = input("Insufficient balance in your account. Would you like to use your savings account?")
            if savingsApproval.lower() == "yes":
                savingsAmount = amount - account['balance']
                account['balance'] = 0
                account['savingsAccount'] -= savingsAmount
                print("Your withdrawal transaction was successfully completed.")
                checkBalance(account)
                newTransaction(account)
            elif savingsApproval.lower() == "no":
                print("Transaction is being terminated.")
            else:
                print("Invalid or incomplete entry.")
        else:
            if account['balance'] + account['savingsAccount'] + account['creditLimit'] >= amount:
                checkCreditLimit(account)
                creditUseApproval = input("Insufficient balance in your main and savings accounts. Would you like to use your credit for the remaining amount?")
                if creditUseApproval.lower() == "yes":
                    creditAmount = (amount - account['balance']) - account['savingsAccount']
                    account['balance'] = 0
                    account['savingsAccount'] = 0
                    account['creditLimit'] -= creditAmount
                    print(f"You successfully used your credit. Your current debt is { -1 * creditAmount}.")
                    newTransaction(account)
                else:
                    print("Transaction is being terminated.")
            else:
                print("Sorry, insufficient balance and credit limit.")

def depositMoney(account, amount):
    accountType = int(input("1-Main Account\n2-Savings Account\nPlease select the account you want to deposit money into:"))
    if accountType == 1:
        account['balance'] += amount
        print("Your deposit transaction was successfully completed.")
        checkBalance(account)
        newTransaction(account)
    elif accountType == 2:
        account['savingsAccount'] += amount
        print("Your deposit transaction was successfully completed.")
        checkBalance(account)
        newTransaction(account)
    else:
        print("Invalid or incomplete entry.")
        newTransaction(account)

def checkBalance(account):
    print(f"After the transactions, the balance of account number {account['accountNo']} is {account['balance']}TL. Your savings account balance is {account['savingsAccount']}TL.")

def checkCreditLimit(account):
    print(f"Your credit limit is {account['creditLimit']}TL.")

def withdrawCredit(account, amount):
    checkCreditLimit(account)
    if amount > account['creditLimit']:
        print("Limit exceeded.")
        newTransaction(account)
    else:
        account['creditLimit'] -= amount
        creditDebt = (-1) * amount
        account['creditDebt'] = creditDebt
        print(f"Your credit has been successfully withdrawn. Your current debt is {account['creditDebt']}TL.")
        newTransaction(account)

def payCreditDebt(account, amount):
    account['creditDebt'] += amount
    print(f'Debt payment successful. Remaining debt: {account["creditDebt"]}')

def atm(account):
    action = int(input(f"1-Balance Inquiry\n2-Credit Limit Inquiry\n3-Withdraw Money\n4-Deposit Money\n5-Withdraw Credit\n6-Pay Credit Debt\nWelcome {account['name']}. Please select the transaction you want to perform:"))
    if action == 1:
        checkBalance(account)
    elif action == 2:
        checkCreditLimit(account)
    elif action == 3:
        checkBalance(account)
        amount = int(input("Enter the amount you want to withdraw:"))
        withdrawMoney(account, amount)
    elif action == 4:
        amount = int(input("Enter the amount you want to deposit:"))
        depositMoney(account, amount)
    elif action == 5:
        checkCreditLimit(account)
        amount = int(input("Enter the amount of credit you want to withdraw:"))
        withdrawCredit(account, amount)
    elif action == 6:
        print(account['creditDebt'])
        amount = int(input("Enter the amount of credit debt you want to pay:"))
        if amount * (-1) > account['creditDebt']:
            print('You entered an excessive amount.')
            newTransaction(account)
        else:
            payCreditDebt(account, amount)
    else:
        print("Invalid or incomplete entry.")

def newTransaction(account):
    continueTransaction = input("Would you like to perform another transaction?")
    if continueTransaction.lower() == "yes":
        atm(account)
    elif continueTransaction.lower() == "no":
        print("Transaction is being terminated.")
    else:
        print("Invalid or incomplete entry. Transaction is being terminated.")

name = input("Please enter your account name:")
password = int(input("Please enter your 4-digit password (numbers only):"))
account = findAccount(name, password)

if account:
    atm(account)
else:
    print("Incorrect username or password.")


















