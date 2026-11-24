def sum(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def division(a, b):
    if b == 0:
        print("Bir sayı 0'a bölünemez.")
        return None
    else:
        return a/b

def number_format(num):
    if isinstance(num, float):
        if num.is_integer():
            return str(num)
        return f"{num:.2f}"
    return str(num)

def get_number(variable):
    while True:
        try:
            return float(input(f"{variable} = "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin")


process_log = []

exit = 0
while exit < 1:
    print("Hesap makinesi")
    print("""
    1. Topla
    2. Çıkar
    3. Çarp
    4. Böl
    5. Loglar
    6. Çıkış
    """)

    log = None
    process = int(input("Yapmak istediğiniz işlemi seçin (1-6): "))

    if process == 1:
        a = get_number("A")
        b = get_number("B")
        sonuc = sum(a, b)

        log = f"{a} + {b} = {number_format(sonuc)}"
        print(log)
    elif process == 2:
        a = get_number("A")
        b = get_number("B")
        sonuc = sub(a, b)

        log = f"{a} - {b} = {number_format(sonuc)}"
        print(log)

    elif process == 3:
        a = get_number("A")
        b = get_number("B")
        sonuc = mult(a, b)

        log = f"{a} x {b} = {number_format(sonuc)}"
        print(log)

    elif process == 4:
        a = get_number("A")
        b = get_number("B")
        sonuc = division(a, b)

        log = f"{a} / {b} = {number_format(sonuc) if sonuc is not None else 'Tanımsız'}"
        print(log)

    elif process == 5:
        print(f"İşlem kayıtları - {len(process_log)} adet ")
        print("-----------")
        for log in process_log:
            print(log)
            
        print("-----------")

    elif process == 6:
        print("Çıkış işlemi alındı.")
        exit = 1
        break
    else:
        print("Geçersiz işlem numarası")

    if log != None:
        process_log.append(log)
