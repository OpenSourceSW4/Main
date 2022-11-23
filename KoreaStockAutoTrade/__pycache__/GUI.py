import requests
import json
import datetime
import time
import yaml
from tkinter import *

window = Tk()
window.title('국내주식자동투자')


helloLabel = Label(window, text = '자동 투자 현황', font=20, pady = 20)
helloLabel.grid(row=0, column=0)
helloLabel = Label(window, text = '자동 투자 현황', font=20, pady = 20)
helloLabel.grid(row=0, column=1)

tradeBox=Text(window, width=80, height=20)
tradeBox.grid(row=1, column=0, padx=5, pady=5)
newsBox=Text(window, width=50, height=20)
newsBox.grid(row=1, column=1, padx=5, pady=5)


button  = Button(window, text = "자동 투자 시작", width=20, height=2)
recommandButton = Button(window, text = "추천 종목 확인", width=20, height=2)
button.grid(row=2,column=0)
recommandButton.grid(row=2,column=1)

window.mainloop()