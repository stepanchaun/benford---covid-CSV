import csv #na citanie tych csv suborov
import math

CESTA = r"C:\Users\stepa\Downloads\data.csv"

pocty = [0] * 10

with open(CESTA, encoding="utf-8-sig") as f: #to with same zatvori, namiesto subor.close(), to s utf je potrebne na neviditelny znak BOM v exceli
    for riadok in csv.DictReader(f): # dictreader cita CSV tak, ze prvy riadok bere ako nazvy 
        try:
            v = int(float(riadok["weekly_count"])) 
        except (ValueError, KeyError): #keby sa nieco stane tak program nepadne, ale preskoci riadok.
            continue
        if v >= 1: #ignoruj 0 a zaporne cisla
            pocty[int(str(v)[0])] += 1

n = sum(pocty)
print("n =", n)
for d in range(1, 10):
    skut = pocty[d] / n * 100
    oca = math.log10(1 + 1 / d) * 100 #benfordov vzorec, koli nemu je potrebny import math
    print(d, f"{skut:5.1f} %", f"{oca:5.1f} %", "#" * round(skut)) #ked mi nesiel kod, agent ho upravil a pridal graf z #, je to celkom cool.