
# This program creates columns of live Bitcoin prices every minute in a csv file. The program also outputs the data in order to see the containt of the it in real time.

import csv
import time
import requests

from datetime import datetime


# Getting data from 'Crypto Compare' :

url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'

def get_price(coin, currency):
    
    try:
        
        response = requests.get(url.format(coin, currency)).json()
        
        return response
        
    except requests.ConnectionError:
        
        error_statement = "Error: Problem Getting To The Link. Make sure you are connected to the internet.)
        
        print(error_statement)


# Using the data to creat a CSV file :

fieldnames = ["time", "current price(₹)"]


with open('Live Bitcoin Price Today.csv', 'w') as csv_file:
    
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
       
     
while True:
    
    today = datetime.now()
    date_time = today.strftime('%H:%M')
    current_price = get_price('BTC', 'INR')
  
    
    with open('Live Bitcoin Price Today.csv', 'a') as csv_file:
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        try:
         info = {
         "time": date_time,
         "current price(₹)": current_price['INR']
         }   
            
         csv_writer.writerow(info)
         print('At', date_time,'Price of 1 Bitcoin is Rs.', current_price['INR'])

         time.sleep(60)
         
        except (TypeError, NameError): 
         break
