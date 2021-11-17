import csv
with open('test2.csv', newline='', encoding='ISO-8859-9') as f:
    reader = csv.reader(f)
    count = 0
    toplam_not = []
    toplam_kredi = []
    rCount = 0
    for row in reader:
        row = [i.split(";") for i in row]

        if len(row) >1:
            temp = row
            row = []
            for i in temp:
                for j in i:
                    row.append(str(j))
        else: row = row[0]
        if count >= 2:
            row[3] = row[3].replace(",",".")
            print(row[3])
            rCount +=1
            rowD = {"ders_kodu" : row[0],
                    "ders_adı" : row[1],
                    "kategori" : row[2],
                    "sınav_puanı":float(row[3]),
                    "notu" : row[4],
                    "kredi" : int(row[5]),
                    "last": row[-1]
                    }
            print("SATIR",rCount,"---",rowD)
            toplam_not.append((rowD["sınav_puanı"]*rowD["kredi"]))
            toplam_kredi.append(rowD["kredi"])

        count += 1
    print("\n------------\n1) Yüzeysel\n2) Detaylı \n\n")
    a = input("Seçiminiz : ")
    if "2" in a:
        while True:
            kredi = input("kredi: ")
            puan = input("puan: ")
            if len(kredi) == 0 or  len(puan) == 0:
                break
            toplam_kredi.append(float(kredi))
            toplam_not.append((float(kredi)*float(puan)))

    toplam_kredi = sum(toplam_kredi)
    toplam_not = sum(toplam_not)
    print(toplam_kredi) 
    print(toplam_not/toplam_kredi)
 
