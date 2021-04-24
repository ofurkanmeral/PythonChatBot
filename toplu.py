from selenium import webdriver
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from selenium.webdriver.common.keys import Keys
import sys
import sqlite3


con=sqlite3.connect("Numaralar.db")
cursor=con.cursor()

logfile = open("log.txt", "a", encoding="utf-8")
logfile.write(str(datetime.datetime.now()))

def tabloustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Whatsapp(Numara TEXT,Durum TEXT)")
    con.commit()

def tikla():


    browser=webdriver.Firefox()
    file=open("numara.txt","r",encoding="utf-8")
    liste=file.readlines()


    tabloustur()
    sayaconay_ = 0
    sayacred_ = 0


    for iter in liste:
        try:

            browser.get("https://web.whatsapp.com/send?phone={0}".format(iter))
            time.sleep(5)
            mesajkutusu = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.CONTROL,"v")
            time.sleep(2)
            buton3=browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")
            buton3.click()



            print("{0} adlı kişiye mesaj gönderildi".format(iter))
            Durum = 'Gönderildi'

            logfile = open("log.txt", "a", encoding="utf-8")
            logfile.write("{0} Başarıyla Gönderildi\n".format(iter))
            logfile.close()
            sayaconay_ += 1
            sayaconay.setText(str(sayaconay_))
            listboxonay.addItem(iter)
        except:
            print("{0} Adlı Kullanıcı Yok".format(iter))
            Durum = "Gönderilmedi"
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]").clear()
            listboxred.addItem(iter)
            sayacred_ += 1
            sayacred.setText(str(sayacred_))

            logfile = open("log.txt", "a", encoding="utf-8")
            logfile.write("{0} Gönderilmedi\n".format(iter))
            logfile.close()
        cursor.execute("insert into Whatsapp values(?,?)", (iter, Durum))
        con.commit()

app=QApplication(sys.argv)
pencere=QWidget()

sayaconay=QLabel(pencere)
sayaconay.move(330,280)
sayaconay.setFont(QFont('Times font',18))

sayacred=QLabel(pencere)
sayacred.move(330,300)
sayacred.setFont(QFont('Times font',18))

yazi=QLabel(pencere)
yazi.setText("Whatsapp Chatbot.")
yazi.setFont(QFont('Times font',20))
yazi.move(150,30)

pencere.setWindowTitle("Whatsapp Chatbot")

resim=QLabel(pencere)
resim.setPixmap(QPixmap("sola.jpg"))

listboxonay=QListWidget(pencere)
listboxonay.resize(100,180)
listboxonay.move(320,300)

listboxred=QListWidget(pencere)
listboxred.resize(100,180)
listboxred.move(450,300)

pencere.setGeometry(100,100,560,500)

Uibuton=QPushButton(pencere)
Uibuton.setText("Gönder")
Uibuton.move(50,450)

label1=QLabel(pencere)
label1.setFont(QFont('Times font',10))
label1.setText("Gönderilecek Mesaj")
label1.move(50,265)

mesajbox=QLineEdit(pencere)
mesajbox.move(50,300)
mesajbox.resize(250,150)

numarabox=QLineEdit(pencere)
numarabox.move(50,100)
numarabox.resize(200,200)
"""listwidget = QListWidget(pencere)
rus=list()
for iter in range(0,100):
    rus.append("rus"+"{0}".format(iter))
rus.reverse()
"""
zaman=QLabel(pencere)
#now=QDate.currentDate()
gun 	  = datetime.datetime.now().strftime("%d");
ay 	      = datetime.datetime.now().strftime("%m");
yil 	  = datetime.datetime.now().strftime("%Y");
saat 	  = datetime.datetime.now().strftime("%H");
dakika	  = datetime.datetime.now().strftime("%M");
tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
zaman.setText(str(tarihsaat))
zaman.setFont(QFont('ariel',10))
zaman.move(350,25)

"""for iter in rus:
    listwidget.insertItem(1,iter)
listwidget.move(70,350)
"""
pencere.show()

Uibuton.clicked.connect(tikla)

sys.exit(app.exec_())
