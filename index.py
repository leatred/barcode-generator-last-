# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:45:07 2020

@author: Mustafa KAÇAR
"""

from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import barcode
import random
from barkodui import Ui_MainWindow

#generator,_=loadUiType('barcode.ui')

class AnaProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Hangisi)
    def Hangisi(self):
        barcodetype=self.comboBox.currentText()
        if barcodetype=="CODE128":
            self.Generate_CODE128()
        elif barcodetype=="ISBN13":
            self.Generate_ISBN13()
        elif barcodetype=="CODE39":
            self.Generate_CODE39()
        elif barcodetype=="EAN13":
            self.Generate_EAN13()
        else:
            self.Generate_EAN14()

            
    def Generate_ISBN13(self):
        if self.lineEdit.text()!="":
            barkod_sayisi=int(self.lineEdit.text())
        if barkod_sayisi!="":
            i=int(0)
            while(i<barkod_sayisi):
                random2=random.randint(100000000,999999999)
                barkod_adi= str(978) + str(random2) 
                name = barcode.generate('ISBN13', barkod_adi, output="output/"+barkod_adi)
                i+=1
            self.statusBar().showMessage("Barcode is generated to 'OUTPUT' file")
        else:
            self.statusBar().showMessage("Barcode number is empty!")

    
    def Generate_CODE39(self):
        barcodestart= self.lineEdit_2.text()
        if self.lineEdit.text()!="":
            barkod_sayisi=int(self.lineEdit.text())
        if barcodestart!="" and barkod_sayisi!="":


            i=int(0)
            while(i<barkod_sayisi):
                random2=random.randint(11111111111,99999999999999999)
                barkod_adi= barcodestart+str(random2) 
                name = barcode.generate('CODE39', barkod_adi, output="output/"+barkod_adi)
                i+=1
            self.statusBar().showMessage("Barcode is generated to 'OUTPUT' file")
        else:
            self.statusBar().showMessage("Barcode start or barcode number is empty!")





    def Generate_EAN13(self):
        if self.lineEdit.text()!="":
            barkod_sayisi=int(self.lineEdit.text())
        if barkod_sayisi!="":

            i=int(0)
            while(i<barkod_sayisi):
                random2=random.randint(1000001011000,999999999999999)
                barkod_adi= str(random2)
                name = barcode.generate('EAN13', barkod_adi, output="output/"+barkod_adi)
                i+=1
            self.statusBar().showMessage("Barcode is generated to 'OUTPUT' file")
        else:
            self.statusBar().showMessage("Barcode number is empty!")

   
    
    
    def Generate_CODE128(self):
        if self.lineEdit.text()!="":
            barkod_sayisi=int(self.lineEdit.text())
        barcodestart= self.lineEdit_2.text()

        if barcodestart!="" and barkod_sayisi!="":

            i=int(0)
            while(i<barkod_sayisi):
                random2=random.randint(11111111111,99999999999999999)
                barkod_adi= barcodestart+str(random2) 
                name = barcode.generate('CODE128', barkod_adi, output="output/"+barkod_adi)
                i+=1
            self.statusBar().showMessage("Barcode is generated to 'OUTPUT' file")
        else:
            self.statusBar().showMessage("Barcode start or barcode number is empty!")
    
    
    
    def Generate_EAN14(self):
        if self.lineEdit.text()!="":
            barkod_sayisi=int(self.lineEdit.text())
        if barkod_sayisi!="":
            i=int(0)
            while(i<barkod_sayisi):
                random2=random.randint(1000001111000,9999999999999)
                barkod_adi= str(random2)
                name = barcode.generate('EAN14', barkod_adi, output="output/"+barkod_adi)
                i+=1
            self.statusBar().showMessage("Barcode is generated to 'OUTPUT' file")
        else:
            self.statusBar().showMessage("Barcode number is empty!")
    
                
def main():
    app=QApplication(sys.argv)
    window=AnaProgram()
    window.show()
    app.exec_()
    
    
if __name__ =='__main__':
    main()
        
