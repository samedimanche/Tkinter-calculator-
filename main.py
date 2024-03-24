from tkinter import *
import math
import requests
from bs4 import BeautifulSoup
# URL = "https://myfin.by/currency/cb-rf/eur"
# URL2 = "https://myfin.by/currency/cb-rf/cny"
URL="https://finance.rambler.ru/calculators/converter/1-EUR-RUB/"
URL3='https://finance.rambler.ru/calculators/converter/1-EUR-CNY/'
headers = {"User-Agent" : 'Mozilla/5.0'}
#EUR
# rGet = requests.get(URL, headers=headers)
# soup = BeautifulSoup(rGet.content, 'html.parser')
# div=((soup.find('div', {'class':'cur-rate__value'})).find('div', {'class':'h1'})).text
# textNum=(str(div)).replace(',','.')
# #CNY
# rGet2 = requests.get(URL2, headers=headers)
# soup2 = BeautifulSoup(rGet2.content, 'html.parser')
# div2 = ((soup2.find('div', {'class':'cur-rate__value'})).find('div', {'class':'h1'})).text
# textNum2=(str(div2)).replace(',','.')

#EUR
rGet1 = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(rGet1.content, 'html.parser')
div11 = ((soup1.find('div', {'class':'converter-change-table__row'})).find('div', {'class':'converter-change-table__rate'})).text
textNum11=(str(div11).replace('\n',''))
#CNY/EUR
rGet3 = requests.get(URL3, headers=headers)
soup3 = BeautifulSoup(rGet3.content, 'html.parser')
div33 = ((soup3.find('div', {'class':'converter-change-table__row'})).find('div', {'class':'converter-change-table__rate'})).text
textNum33=(str(div33).replace('\n',''))
# Create an instance of tkinter frame or window
win=Tk()
win.title('Calc')
win.configure(background='grey')
x=520
y=170
win.wm_geometry("+%d+%d" % (x, y))
currency=float(textNum11) #Eur
# currency2=float(textNum2) #CNY
currency3=float(textNum33)#CNYEUR
# Set the size of the tkinter window
win.geometry("700x780")
def cal_sum():
   with open("deliveri.txt",'r',encoding = 'utf-8') as f: #Delivery count
      dil=math.ceil(float(f.read()))
      t1 = float((a.get()).replace(',', '.'))
      t2 = float((b.get()).replace(',', '.'))
      t3 = float((c.get()).replace(',', '.'))
      t4 = currency
      # t5= currency2
      t6=currency3
      # t4 = float((z.get()).replace(',','.'))
      ff = float(1000)
      gg=float(31)
      if (((float(math.ceil(t3 / (t6-0.1)))) < (ff)) and t1<=gg):
         dil22=float(t1*dil)
         sum = math.ceil(float(dil22 + t2 * t3))
         label.config(text=(str('{:,}'.format(sum).replace(',', ' ')) + f"    ₽  from China to Blg"
                                                                        f"\nDelivery: {'{:,}'.format(dil22).replace(',', ' ')} ₽\nDelivery to Blg: {dil}₽/1kg"))
      else:
         dil22 = float(t1 * dil)
         sum = math.ceil(float(dil22 + t2 * t3))
         taxKG2 = math.ceil(((t1 - gg) * 2))
         tax2 = ((math.ceil(((((t3 / (t6 - 0.1)) ) - ff) * 0.15))))
         if (t1>gg and (float(math.ceil(t3 / (t6 - 0.1)) > (ff)))):
            if tax2>taxKG2:
               taxRub22 = math.ceil(float(tax2 * (math.ceil(t4)))+float(tax2 * (math.ceil(t4)))*0.07+float(500))
               sum2 = math.ceil(float(sum + taxRub22))
               label.config(text=(f"{'{:,}'.format(sum2).replace(',', ' ')} ₽\n" + str('{:,}'.format(sum).replace(',', ' ')) +
                                  " ₽  from China to Blg" + f"\n+ tax ≈{'{:,}'.format(tax2).replace(',', ' ')} € ≈ ({'{:,}'.format(taxRub22).replace(',', ' ')}₽)"
                                                            f"\nEur currency: {t4}\nDelivery: {'{:,}'.format(dil22).replace(',', ' ')} ₽\nDelivery to Blg: {'{:,}'.format(dil).replace(',', ' ')}₽/1kg"))
            else:
               taxRubKG = math.ceil(float(taxKG2 * (math.ceil(t4)))+ float(taxKG2 * (math.ceil(t4)))*0.07+float(500))
               sum3 = math.ceil(float(sum + taxRubKG))
               label.config(text=(f"{'{:,}'.format(sum3).replace(',', ' ')} ₽\n" + str('{:,}'.format(sum).replace(',',' ')) +
                                  " ₽  from China to Blg" + f"\n+ tax ≈{'{:,}'.format(taxKG2).replace(',', ' ')} € ≈ ({'{:,}'.format(taxRubKG).replace(',', ' ')}₽)"
                                                            f"\nEur currency: {t4}\nDelivery: {'{:,}'.format(dil22).replace(',', ' ')} ₽\nDelivery to Blg: {'{:,}'.format(dil).replace(',', ' ')}₽/1kg"))

         elif (t1>gg):
            taxRubKG = math.ceil(float(taxKG2 * (math.ceil(t4)))+ float(taxKG2 * (math.ceil(t4)))*0.07+float(500))
            sum3 = math.ceil(float(sum + taxRubKG))
            label.config(text=(f"{'{:,}'.format(sum3).replace(',', ' ')} ₽\n" + str('{:,}'.format(sum).replace(',',' ')) +
                               " ₽  from China to Blg" + f"\n+ tax ≈{'{:,}'.format(taxKG2).replace(',', ' ')} € ≈ ({'{:,}'.format(taxRubKG).replace(',', ' ')}₽)"
                                                         f"\nEur currency: {t4}\nDelivery: {'{:,}'.format(dil22).replace(',', ' ')} ₽\nDelivery to Blg: {'{:,}'.format(dil).replace(',', ' ')}₽/1kg"))

         else:
            taxRub = math.ceil(float(tax2 * (math.ceil(t4)))+float(tax2 * (math.ceil(t4)))*0.07+float(500))
            sum2 = math.ceil(float(sum + taxRub))
            label.config(text=(f"{'{:,}'.format(sum2).replace(',', ' ')} ₽\n" + str('{:,}'.format(sum).replace(',',' ')) +
                               " ₽  from China to Blg" + f"\n+ tax ≈{'{:,}'.format(tax2).replace(',', ' ')} € ≈ ({'{:,}'.format(taxRub).replace(',', ' ')}₽)"
                                                         f"\nEur currency: {t4}\nDelivery: {'{:,}'.format(dil22).replace(',', ' ')} ₽\nDelivery to Blg: {'{:,}'.format(dil).replace(',', ' ')}₽/1kg"))

   # Create an Entry widget
Label(win, text="Enter Kilo", font=('Impact 20')).pack()
a=Entry(win, width=35, font=(' Impact 25'))
a.pack()
Label(win, text="Enter Currency  ¥: ", font=('Impact 20')).pack()
b=Entry(win, width=35 , font=(' Impact 25'))
b.pack()
Label(win, text="Enter Price of a thing", font=('Impact 20')).pack()
c=Entry(win, width=35 , font=(' Impact 25'))
c.pack()

label=Label(win, text="Total Sum : ", font=('Impact 35'), fg='#f00')
label.pack(pady=35)
Button(win, text="Calculate Sum", command=cal_sum, font=('Impact 25') ).pack()

win.mainloop()
