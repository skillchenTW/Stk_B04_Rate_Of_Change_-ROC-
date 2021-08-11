import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

#Compute Roc
def ROC(data,n):
    N=data['Close'].diff(n)
    D=data['Close'].shift(n)
    try:
        ROC = pd.Series(N/D, name="Rate Of Change")
        data = data.join(ROC)
        return data
    except Exception as e:
        print(e)

data = web.DataReader("2330.TW", data_source='yahoo', start='1/1/2020', end='8/10/2021')    
data = pd.DataFrame(data)

n=5
ROC_Nifty=ROC(data,n)
ROC = ROC_Nifty['Rate Of Change']

# represent them in chart
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(2,1,1)
ax.set_xticklabels([])
plt.plot(data['Close'], lw=1)
plt.title("2330.TW Price Chart")
plt.ylabel('Close Price')
plt.grid(True)
bx = fig.add_subplot(2,1,2)
plt.plot(ROC, 'k', lw=0.75, linestyle='-', label='ROC')
plt.legend(loc=2,prop={'size':9})
plt.ylabel('ROC Values')
plt.grid(True)
plt.setp(plt.gca().get_xticklabels(), rotation=45)
plt.show()