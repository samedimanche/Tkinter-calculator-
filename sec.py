from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import math
import urllib3
import chardet
import idna
from bs4 import BeautifulSoup
import requests

URL = "https://myfin.by/currency/cb-rf/eur"
URL2 = "https://myfin.by/currency/cb-rf/cny"
headers = {"User-Agent": 'Mozilla/5.0'}
rGet = requests.get(URL, headers=headers)
soup = BeautifulSoup(rGet.content, 'html.parser')
div = ((soup.find('div', {'class': 'cur-rate__value'})).find('div', {'class': 'h1'})).text
textNum = (str(div)).replace(',', '.')
rGet2 = requests.get(URL2, headers=headers)
soup2 = BeautifulSoup(rGet2.content, 'html.parser')
div2 = ((soup2.find('div', {'class': 'cur-rate__value'})).find('div', {'class': 'h1'})).text
textNum2 = (str(div2)).replace(',', '.')
currency = float(textNum)
currency2 = float(textNum2)
ff = float(1000)
gg = float(31)
class Demo(App):
    def press(self, instance):
        t1 = float((self.solution.text).replace(',', '.'))
        t2 = float((self.solution1.text).replace(',', '.'))
        t3 = float((self.solution2.text).replace(',', '.'))
        dil = float((self.solution3.text).replace(',', '.'))
        t4 = currency
        t5 = currency2
        if (self.solution.text):
            try:
                if (((float(t3 * (t5 + 0.3))) < (ff * (t4 - 0.2))) and t1 < gg):
                    sum = math.ceil(float(t1 * dil + t2 * t3))
                    self.label.text = str(str(sum) + f"    ₽  from China to Blg\nDelivery to Blg: {dil}₽/1kg")
                else:
                    sum = math.ceil(float(t1 * dil + t2 * t3))
                    taxKG2 = math.ceil((t1 - gg) * 2)
                    tax2 = (math.ceil(((((t3 * (t5 + 0.3)) / (t4 - 0.2)) - ff) * 0.15) + float(5)))
                    if (t1 > gg and ((float(t3 * (t5 + 0.3))) > (ff * (t4 - 0.2)))):
                        if tax2 > taxKG2:
                            taxRub22 = math.ceil(float(tax2 * (math.ceil(t4))))
                            sum2 = math.ceil(float(sum + taxRub22))
                            self.label.text = str(f"{sum2} ₽\n" + str(
                                sum) + "  ₽  from China to Blg" + f"\n+ tax ≈{tax2} € ≈ ({taxRub22}₽)\nEur currency: {t4}\nDelivery to Blg: {dil}₽/1kg")
                        else:
                            taxRubKG = math.ceil(float(taxKG2 * (math.ceil(t4))))
                            sum3 = math.ceil(float(sum + taxRubKG))
                            self.label.text = str(((f"{sum3} ₽\n" + str(
                                sum) + "  ₽  from China to Blg" + f"\n+ tax ≈{taxKG2} € ≈ ({taxRubKG}₽)\nEur currency: {t4}\nDelivery to Blg: {dil}₽/1kg")))
                    elif (t1 > gg):
                        taxRubKG = math.ceil(float(taxKG2 * (math.ceil(t4))))
                        sum3 = math.ceil(float(sum + taxRubKG))
                        self.label.text = str(((f"{sum3} ₽\n" + str(
                            sum) + "    ₽  from China to Blg" + f"\n+ tax ≈{taxKG2} € ≈ ({taxRubKG}₽)\nEur currency: {t4}\nDelivery to Blg: {dil}₽/1kg")))
                    else:
                        taxRub = math.ceil(float(tax2 * (math.ceil(t4))))
                        sum2 = math.ceil(float(sum + taxRub))
                        self.label.text = str(((f"{sum2} ₽\n" + str(
                            sum) + "    ₽  from China to Blg" + f"\n+ tax ≈{tax2} € ≈ ({taxRub}₽)\nEur currency: {t4}\nDelivery to Blg: {dil}₽/1kg")))
            except:
                self.label.text = "Error"

    def build(self, **kwargs):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        label0 = Label(text=f"Enter Kilo", font_size=30,size_hint=(1, 0.1))
        main_layout.add_widget(label0)
        self.solution = TextInput(multiline=False, readonly=False, halign="center", font_size=45,size_hint=(1, 0.5))
        main_layout.add_widget(self.solution)
        label1 = Label(text=f"Enter Currency  ¥", font_size=30,size_hint=(1, 0.1))
        main_layout.add_widget(label1)
        self.solution1 = TextInput(multiline=False, readonly=False,halign="center", font_size=45,size_hint=(1, 0.5))
        main_layout.add_widget(self.solution1)
        label2 = Label(text=f"Enter Price of a thing ¥", font_size=30,size_hint=(1, 0.1))
        main_layout.add_widget(label2)
        self.solution2 = TextInput(multiline=False, readonly=False,halign="center", font_size=45,size_hint=(1, 0.5))
        main_layout.add_widget(self.solution2)
        label3 = Label(text=f"Enter cost delivery ₽ per 1kg", font_size=30,size_hint=(1, 0.1))
        main_layout.add_widget(label3)
        self.solution3 = TextInput(multiline=False, readonly=False,halign="center", font_size=45,size_hint=(1, 0.5))
        main_layout.add_widget(self.solution3)

        btn1 = Button(text="Calculate", font_size=40, background_color="#19FF6D",size_hint=(1, 0.5))
        btn1.bind(on_press=self.press)
        main_layout.add_widget(btn1)

        self.label=Label(text=f"",font_size=50, bold=True, color="#FF5100")
        main_layout.add_widget(self.label)

        return main_layout

if __name__ == '__main__':
    Demo().run()
