import random

class Person:
    def __init__(self, name, age, tckn):
        self.name = name
        self.age = age
        self.__tckn = tckn

        
    def goster_kisi(self):
        print(f"{self.name} - {self.age} - {self.__tckn}")

    def check_tckn(self, givenTckn):
        if self.__tckn == givenTckn:
            return self
        else:
            return None

class BankAccount:
    def __init__(self, person: Person, account_no, cash):
        self.person = person
        self.account_no = account_no
        self.cash = cash
        self.__logs = []

    def yatir_para(self, yatirilacakMiktar):
        self.cash += yatirilacakMiktar
        self.save_log("deposit", yatirilacakMiktar, self.cash)
    
    def cek_para(self, cekilecekMiktar):
        if self.cash >= cekilecekMiktar:
            self.cash -= cekilecekMiktar
            self.save_log("withdrawal", cekilecekMiktar, self.cash)
        else:
            print("Yeterli bakiye yok, çekim iptal")
        
    def goster_para(self):
        print(f"{self.account_no} - {self.cash:.3f} TL")

    def transfer(self, type, transferMiktarı, aliciID):
        if(type == "sender"):
            if self.account_no == aliciID:
                print("Aynı hesaba transfer yapılamaz.")
                return False
            if transferMiktarı <= 0:
                print("Transfer tutarı 0'dan büyük olmalı.")
                return False
            if self.cash < miktar:
                print("Yeterli bakiye yok, transfer iptal.")
                return False
            
            self.cash -= transferMiktarı
        elif(type == "receiver"):
            self.cash += transferMiktarı
        else:
            print("Bilinmeyen transfer tipi.")
            return False


    def save_log(self, type, amount, balance):
        self.__logs.append({"process_type": type, "amount" : amount, "after_transaction_balance": balance})

    def show_logs(self):
        if len(self.__logs) != 0:
            for log in self.__logs:
                print(f"[{log["process_type"]}], {log["amount"]}, {log["after_transaction_balance"]} ")

        else:
            print("Log kaydı bulunamadı.")


exit = 0

persons = []
accounts = []

def hesap_arama(specialText=None):
    if not accounts:
        print("HATA: Hic hesap yok.")
        return None
    acc_no = int(input(specialText if specialText is not None else "Hesap No: "))
    acc = find_account(acc_no)
    if acc is None:
        print("HATA: Hesap bulunamadı")
        return None

    return acc

def find_account(account_no):
    for acc in accounts:
        if acc.account_no == account_no:
            return acc
    return None

def find_person_by_tckn(tckn):
    for person in persons:
        check = person.check_tckn(tckn)
        if check != None:
            return person
    return None

def generate_unique_id():
    mevcut_acc_nos = {acc.account_no for acc in accounts}
    #Aslında random yerine uuid ile yapılır ama program anlaşılırlığı ve kullanımı kolay olsun diye random yaptım.
    while True:
        new_no = random.randint(1000, 9999)
        if new_no not in mevcut_acc_nos:
            return new_no



while exit < 1:
    print("Banka sistemine hoş geldiniz.")
    print("""
    1. Hesap Aç
    2. Para Yatır
    3. Para Çek
    4. Bakiye Göster
    5. Kişi Bilgi Göster
    6. Log Kaydı Göster
    7. EFT Transferi
    8. Çıkış
    """)
    process = int(input("Yapmak istediğiniz işlemi seçin (1-6): "))

    if process == 1:
        print("Ad, Yaş ve TCKN gir")
        name = input("AD: ").strip()
        if not name:
            print("HATA: Ad boş olamaz")
            continue
        age = input("YAS: ").strip()
        if not age.isdigit() or int(age) <= 0:
            print("HATA: Yaş pozitif bir tam sayı olmalı")
            continue
        tckn = input("TCKN: ").strip()
        if not tckn.isdigit() or len(tckn) != 11:
            print("HATA: TCKN 11 haneli olmalı")
            continue

        kisi = Person(name, int(age), tckn)
        uuid = generate_unique_id()
        persons.append(kisi)
        accounts.append(BankAccount(kisi, uuid, 0))

        print(f"Hesap başarıyla oluşturuldu. HESAP NO: {uuid}")

    elif process == 2:
        acc = hesap_arama()
        if acc == None:
            continue
        
        try:
            miktar = float(input("Miktar: "))
        except ValueError:
            print("HATA: Geçerli bir sayı girin")
            continue
        acc.yatir_para(miktar)

    elif process == 3:
        acc = hesap_arama()
        if acc == None:
            continue

        print("Çekilecek Para")
        miktar = int(input("Miktar: "))
        acc.cek_para(miktar)

    elif process == 4:
        acc = hesap_arama()
        if acc == None:
            continue

        print("Bakiye Göster")
        acc.goster_para()

    elif process == 5:
        if persons == None:
            print("HATA: Önce kişi oluşturmalısınız")
            continue

        tckn = input("TCKN: ").strip()
        if not tckn.isdigit() or len(tckn) != 11:
            print("HATA: TCKN 11 haneli olmalı")
            continue
        person = find_person_by_tckn(tckn)
        if person != None:
            person.goster_kisi()
        else: 
            print("TCKN'ye göre kisi bulunamadı.")

    elif process == 6:
        acc = hesap_arama()
        if acc == None:
            continue
        
        print("Log Kaydı Göster")
        acc.show_logs()

    elif process == 7:
        sender_acc = hesap_arama("EFT Gönderici Hesap No: ")
        if sender_acc == None:
            continue
        
        receiver_acc = hesap_arama("EFT Alıcı Hesap No: ")
        if receiver_acc == None:
            continue

        miktar = int(input("Transfer Miktar: "))

        sender_acc.transfer("sender", miktar, receiver_acc.account_no)
        receiver_acc.transfer("receiver", miktar, None)

        print("EFT İşlemi gerçekleştirildi.")

    elif process == 8:
        print("Çıkış alındı. Hoşça kalın")
        exit = 1
        break
    else:
        print("HATA: Geçersiz işlem numarası")