     
# This program fetch data from a CSV file and produces an animated line chart that changes in a minute and is good to display live data.  

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


# Getting and assigning the data :

def animate(i):
    
    data = pd.read_csv('Live Bitcoin Price Today.csv')
    time = data['time']
    current_date = data['current price(₹)']

# Plotting :
    
    plt.cla()

    plt.plot(time, current_date)
    

# Labeling the data :
       
    plt.title('Bitcoin Price Today :', fontsize = 12, fontweight = 'bold')
    
    plt.xlabel('\n Time (hrs & mins) >>>', fontsize = 12)
    
    plt.ylabel('Price (₹) >>> \n', fontsize = 12)
    
    plt.tight_layout()


# Animating the line chart :

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.show()


''' Sourin Das '''