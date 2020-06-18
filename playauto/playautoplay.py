from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys,os,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

def bun():
     import playauto11bundorothy385
def bunsale():
     import playauto11bundorothy385sale
def auction():
     import playautoauctiondorothy385
def auctionsale():
     import playautoauctiondorothy385sale
def gmarket():
     import playautogmarketdorothy385
def gmarketsale():
     import playautogmarketdorothy385sale
def interpark():
     import playautointerparkdorothy385
def interparksale():
     import playautointerparkdorothy385sale
def naver():
     import playautosmartstoredorothy385
def naversale():
     import playautosmartstoredorothy385sale
def aesmsale():
     import auctionesmsale
def aesmstop():
     import auctionesmstop
def gesmsale():
     import gmarketesmsale
def gesmstop():
     import gmarketesmstop
def bunsteady():
     import playauto11bundorothy385steady
def auctionsteady():
     import playautoauctiondorothy385steady
def gmarketsteady():
     import playautogmarketdorothy385steady
def interparksteady():
     import playautointerparkdorothy385steady
def naversteady():
     import playautosmartstoredorothy385steady
def bun2():
     import playauto11bunsalefi
def bunsale2():
     import playauto11bunsalefisale
def auction2():
     import playautoauctionsalefi
def auctionsale2():
     import playautoauctionsalefisale
def gmarket2():
     import playautogmarketsalefi
def gmarketsale2():
     import playautogmarketsalefisale
def interpark2():
     import playautointerparkyoome
def interparksale2():
     import playautointerparkyoomesale
def naver2():
     import playautosmartstorebalmain
def naversale2():
     import playautosmartstorebalmainsale
def bunsteady2():
     import playauto11bunsalefisteady
def auctionsteady2():
     import playautoauctionsalefisteady
def gmarketsteady2():
     import playautogmarketsalefisteady
def interparksteady2():
     import playautointerparkbalmainsteady
def naversteady2():
     import playautosmartstorebalmainsteady
def nh():
     import playautonhmarketdorothy385
def nhsale():
     import playautonhmarketdorothy385sale
def nhsteady():
     import playautonhmarkeydorothy385steady
def nhstop():
     import playautonhmarketdorothy385stop
def nh2():
     import playautonhmarketyoome123
def nhsale2():
     import playautonhmarketyoome123sale
def nhsteady2():
     import playautonhmarkeyyoome123steady
def nhstop2():
     import playautonhmarkettoome123stop
def steady():
     import playautosteady
     

if __name__ == "__main__":
     if getattr(sys, 'frozen', False):
          Chrome_path = os.path.join(sys._MEIPASS, "ChromeDriver.exe")
          driver = webdriver.Chrome(Chrome_path)
     else:
          driver=webdriver.Chrome()
     
     window=Tk() 
     window.title("플레이오토2.0") 
     window.configure(background='#E6F3FE')
     radvar=IntVar()
    
     num1 = ttk.Button(window, text="K1D", command=bun)
     num1.grid(column=1, row=1, sticky=W)


     num2 = ttk.Button(window, text="K2D", command=bunsale) 
     num2.grid(column=2, row=1, sticky=W)

     num14 = ttk.Button(window, text="K3D", command=bunsteady) 
     num14.grid(column=3, row=1, sticky=W)

     num19 = ttk.Button(window, text="K1S", command=bun2)
     num19.grid(column=4, row=1, sticky=W)


     num20 = ttk.Button(window, text="K2S", command=bunsale2) 
     num20.grid(column=5, row=1, sticky=W)

     num21 = ttk.Button(window, text="K3S", command=bunsteady2) 
     num21.grid(column=6, row=1, sticky=W)


     num3 = ttk.Button(window, text="A1D", command=auction)
     num3.grid(column=1, row=2, sticky=W)

     num4 = ttk.Button(window, text="A2D", command=auctionsale) 
     num4.grid(column=2, row=2, sticky=W)
     

     num15 = ttk.Button(window, text="A3D", command=auctionsteady) 
     num15.grid(column=3, row=2, sticky=W)

     num22 = ttk.Button(window, text="A1S", command=auction2)
     num22.grid(column=4, row=2, sticky=W)

     num23 = ttk.Button(window, text="A2S", command=auctionsale2) 
     num23.grid(column=5, row=2, sticky=W)
     

     num24 = ttk.Button(window, text="A3S", command=auctionsteady2) 
     num24.grid(column=6, row=2, sticky=W)

     num11 = ttk.Button(window, text="옥션-ESM판매", command=aesmsale) 
     num11.grid(column=7, row=2, sticky=W)

     num34 = ttk.Button(window, text="옥션-ESM판매중지", command=aesmstop) 
     num34.grid(column=8, row=2, sticky=W)
    
     num5 = ttk.Button(window, text="G1D", command=gmarket)
     num5.grid(column=1, row=3, sticky=W)


     num6 = ttk.Button(window, text="G2D", command=gmarketsale) 
     num6.grid(column=2, row=3, sticky=W)

     num16 = ttk.Button(window, text="G3D", command=gmarketsteady) 
     num16.grid(column=3, row=3, sticky=W)

     num25 = ttk.Button(window, text="G1S", command=gmarket2)
     num25.grid(column=4, row=3, sticky=W)


     num26 = ttk.Button(window, text="G2S", command=gmarketsale2) 
     num26.grid(column=5, row=3, sticky=W)

     num27 = ttk.Button(window, text="G3S", command=gmarketsteady2) 
     num27.grid(column=6, row=3, sticky=W)

     num12 = ttk.Button(window, text="g마켓-ESM판매", command=gesmsale) 
     num12.grid(column=7, row=3, sticky=W)

     num13 = ttk.Button(window, text="g마켓-ESM판매중지", command=gesmstop) 
     num13.grid(column=8, row=3, sticky=W)


     num7 = ttk.Button(window, text="I1D", command=interpark)
     num7.grid(column=1, row=4, sticky=W)


     num8 = ttk.Button(window, text="I2D", command=interparksale) 
     num8.grid(column=2, row=4, sticky=W)

     num17 = ttk.Button(window, text="I3D", command=interparksteady) 
     num17.grid(column=3, row=4, sticky=W)

     num28 = ttk.Button(window, text="I1S", command=interpark2)
     num28.grid(column=4, row=4, sticky=W)


     num29 = ttk.Button(window, text="I2S", command=interparksale2) 
     num29.grid(column=5, row=4, sticky=W)

     num30 = ttk.Button(window, text="I3S", command=interparksteady2) 
     num30.grid(column=6, row=4, sticky=W) 


     num9 = ttk.Button(window, text="N1D", command=naver)
     num9.grid(column=1, row=5, sticky=W)


     num10 = ttk.Button(window, text="N2D", command=naversale) 
     num10.grid(column=2, row=5, sticky=W)

     num18 = ttk.Button(window, text="N3D", command=naversteady) 
     num18.grid(column=3, row=5, sticky=W)

     num31 = ttk.Button(window, text="N1S", command=naver2)
     num31.grid(column=4, row=5, sticky=W)


     num32 = ttk.Button(window, text="N2S", command=naversale2) 
     num32.grid(column=5, row=5, sticky=W)

     num33 = ttk.Button(window, text="N3S", command=naversteady2) 
     num33.grid(column=6, row=5, sticky=W)

     num35 = ttk.Button(window, text="H1D", command=nh) 
     num35.grid(column=1, row=6, sticky=W)

     num36 = ttk.Button(window, text="H2D", command=nhsale) 
     num36.grid(column=2, row=6, sticky=W)

     num37 = ttk.Button(window, text="H3D", command=nhsteady) 
     num37.grid(column=3, row=6, sticky=W)

     num38 = ttk.Button(window, text="H1S", command=nh2) 
     num38.grid(column=4, row=6, sticky=W)

     num39 = ttk.Button(window, text="H2S", command=nhsale2) 
     num39.grid(column=5, row=6, sticky=W)

     num40= ttk.Button(window, text="H3S", command=nhsteady2) 
     num40.grid(column=6, row=6, sticky=W)

     num41= ttk.Button(window, text="333", command=steady) 
     num41.grid(column=1, row=7, sticky=W)

     

     


     window.mainloop() 
