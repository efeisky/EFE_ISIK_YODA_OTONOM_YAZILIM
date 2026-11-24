DATA_FILE="surus_verisi.csv"
OUTPUT_FILE="sonuc.txt"

def read_file():
    datas = []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = lines[1:]
    missing_count = 0
    for line in lines:
        zones = line.strip().split(",")

        if zones[1] == "":
            missing_count+=1
            continue

        zaman_s = int(zones[0])
        hiz_kmh = float(zones[1])

        datas.append(dict({
            "zaman" : zaman_s,
            "hiz" : hiz_kmh
        }))

    return datas, missing_count

data, missing_count = read_file()
data_count = len(data)

print(f"""
Toplam Ölçüm Sayısı: {data_count + missing_count}
Eksik Ölçüm Sayısı: {missing_count}
Uygun Ölçüm Sayısı: {data_count} 
--------------------------------
""")

def calc_ort_hiz(data, data_len):
    return sum(d["hiz"] for d in data) / data_len

def calc_max_hiz(data):
    return max(data, key=lambda d: d["hiz"])

ort_hiz = calc_ort_hiz(data, data_count)

max_data = calc_max_hiz(data)
max_hiz = max_data["hiz"]
max_hiz_sn = max_data["zaman"]

print(f"""
Ortalama Hız: {ort_hiz:.3f}
Max Hız: {max_hiz}
Max Hızın Yapıldığı Saniye: {max_hiz_sn} 
--------------------------------
""")


def calc_stop_second(data):
    durma_suresi = 0
    for d in data:
        if d["hiz"] == 0.0:
            durma_suresi +=1
    return durma_suresi

def calc_limit_second(data):
    limit_asim_suresi = 0
    for d in data:
        if d["hiz"] > 30.0:
            limit_asim_suresi +=1
    return limit_asim_suresi

stop_second = calc_stop_second(data)
limit_second = calc_limit_second(data)

print(f"""
Durma Süresi: {stop_second}
Limit Aşım Süresi: {limit_second}
--------------------------------
""")

def calc_mesafe(data):
    mesafe = 0
    for d in data:
        mesafe += d["hiz"] / 3.6
    return mesafe

mesafe = calc_mesafe(data)
print(f"""
Aldığı Mesafe: {mesafe:.3f} metre
--------------------------------
""")

def save_results(total_count, missing_count, valid_count, ort_hiz, max_hiz, max_hiz_sn, stop_second, limit_second, mesafe):
    rapor = f"""Toplam Ölçüm Sayısı: {total_count}
Eksik Ölçüm Sayısı: {missing_count}
Uygun Ölçüm Sayısı: {valid_count}
--------------------------------
Ortalama Hız: {ort_hiz:.3f}
Max Hız: {max_hiz}
Max Hızın Yapıldığı Saniye: {max_hiz_sn}
--------------------------------
Durma Süresi: {stop_second}
Limit Aşım Süresi: {limit_second}
--------------------------------
Aldığı Mesafe: {mesafe:.3f} metre
--------------------------------"""
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(rapor)

save_results(data_count + missing_count, missing_count, data_count, ort_hiz, max_hiz, max_hiz_sn, stop_second, limit_second, mesafe)