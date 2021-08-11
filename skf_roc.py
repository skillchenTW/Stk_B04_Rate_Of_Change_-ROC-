# 算法交易：Python 編程中的技術指標變化率 (ROC) 實現。

import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

def SKF_RateOfChange(symbol,start='1/1/2000',end='8/10/2021',ndays=5):    
    data = web.DataReader(f"{symbol}.TW", data_source='yahoo', start='1/1/2020', end='8/10/2021')    
    data = pd.DataFrame(data)
    #Compute Roc
    N=data['Close'].diff(ndays)
    D=data['Close'].shift(ndays)
    try:
        ROC = pd.Series(N/D, name="Rate Of Change")
        data = data.join(ROC)
        ROC_Nifty = data
        ROC = ROC_Nifty['Rate Of Change']
        # represent them in chart
        fig = plt.figure(figsize=(7,5))
        ax = fig.add_subplot(2,1,1)
        ax.set_xticklabels([])
        plt.plot(data['Close'], lw=1)
        plt.title(f"{symbol}.TW Price Chart")
        plt.ylabel('Close Price')
        plt.grid(True)
        bx = fig.add_subplot(2,1,2)
        plt.plot(ROC, 'k', lw=0.75, linestyle='-', label='ROC')
        plt.legend(loc=2,prop={'size':9})
        plt.ylabel('ROC Values')
        plt.grid(True)
        plt.setp(plt.gca().get_xticklabels(), rotation=45)
        plt.show()
    except Exception as e:
        print(e)

    
SKF_RateOfChange(symbol='0050',start='1/1/2001',end='8/10/2021',ndays=1)
#SKF_RateOfChange(symbol='2330',start='1/1/2015',end='8/10/2021',ndays=1)




    