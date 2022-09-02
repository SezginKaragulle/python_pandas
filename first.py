import numpy as np
import pandas as pd

benimSozlugum = {"Atil":50,"Zeynep":40,"Mehmet":30}

mySeries = pd.Series(benimSozlugum)
print("SERİES: ",mySeries)

benimYaslarim = [50,40,30]
benimIsimlerim = ["Atil","Zeynep","Mehmet"]

def pandas_1():
    mySeries2 = pd.Series(benimYaslarim,benimIsimlerim)
    print("SERİES2: ",mySeries2)

def pandas_2():
    # yeni bir series oluşturuyoruz.
    print(pd.Series(["Atil","Atlas","Osman"],[1,2,3]))

def pandas_3():
    yarismaSonucu1 = pd.Series([10,5,1],["Atil","Atlas","Osman"])
    yarismaSonucu2 = pd.Series([20,10,8],["Atil","Atlas","Osman"])
    sonSonuc = yarismaSonucu1 + yarismaSonucu2
    print(sonSonuc)

def pandas_4():
    data = np.random.rand(4,3)
    print(data)
    print("")
    dataFrame = pd.DataFrame(data)
    print(dataFrame)

def pandas_5():
    data = np.random.rand(4,3)
    yeniDataFrame = pd.DataFrame(data,index=["Atil","Zeynep","Atlas","Mehmet"],columns=["Maaş","Yaş","Çalışma Saati"])
    print(yeniDataFrame)
    print("")
    yeniDataFrame["Emeklilik Yasi"] = yeniDataFrame["Maaş"] + yeniDataFrame["Maaş"]
    print(yeniDataFrame)
    # print("")
    # print("")
    # print(yeniDataFrame.drop("Emeklilik Yasi",axis=1))
    yeniDataFrame.drop("Emeklilik Yasi",axis=1,inplace=True)
    print(yeniDataFrame)

def pandas_6():
    sozlukVerisi = {"Istanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"Izmir":[40,39,38]}
    havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
    print(havaDurumuDataFrame)
    print("")
    havaDurumuDataFrame = havaDurumuDataFrame.fillna(20)
    print(havaDurumuDataFrame)

def pandas_7():
    maasSozlugu = {"Departman":["Yazılım","Satış","Pazarlama","Finans","İnsan Kaynakları","Hukuk"],
    "Calisan İsmi":["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
    "Maas": [100,150,200,300,400,500]}
    maasDataFrame = pd.DataFrame(maasSozlugu)
    print(maasDataFrame)
    print("")
    grupObjesi = maasDataFrame.groupby("Departman")
    print(grupObjesi)
    print("")
    print(grupObjesi.count())
    print("")
    print(grupObjesi.max())
    print("")
    print(grupObjesi.describe())

def pandas_8():
    dataFrame = pd.read_excel("C:\\python\\PANDAS\\maas.xlsx")
    print(dataFrame)
    print("")
    doluDegerlerDataFrame = dataFrame.dropna()
    print(dataFrame.dropna())
    print("")
    doluDegerlerDataFrame.to_excel("yenimaas.xlsx")
    



