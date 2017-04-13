from bs4 import BeautifulSoup
import requests
import time
import os
from slacker import Slacker

slack = Slacker('xoxb-168765462614-AF2fvGqqzsTorz0BTvzXaEYu')

try: 
    while True:
        s = requests.Session()
        response = s.get("https://www.pmbull.com/gold-price/")



        soup = BeautifulSoup(response.text, "html.parser")

        goldprice = soup.findAll("div",{"id":"gold_spot_3"})
        ya = soup.find('b')
        final = ya.text
        semi = final.split()
        goldprice = semi[0]
        percent1 = semi[2]
        semipercent = (percent1[:-1]) #makes percent just a number : 0.01 etc....
        percent = (semipercent[1:])

        print goldprice
        quit = raw_input("Press q to quit")
        if float(percent) > 0.99:
            print percent
            slack.chat.post_message('#goldpriceforpapa', 'Current Price Per Ounce: ' + goldprice + '\n' + "RECORD HIGH PERCENT!!" + ' ' + '--->' + ' ' + '+' + percent + '%') 
            time.sleep(10)
        else:
            time.sleep(10)
        if quit == "q":
            break
except KeyboardInterrupt:
    pass
    
  
