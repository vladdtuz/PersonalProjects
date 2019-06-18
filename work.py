import FinanceAI as fn 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  

data = pd.read_csv('A.csv')
Direction = fn.DirectionalMovement(fn.PosMov(data['High']),
                                    fn.NegMove(data['Low']))

AveTrueRange = fn.ATR(fn.TR(data['High'],
                            data['Low'],
                            data['Close']),14)

DI_positive = 100*np.array(Direction[0][13:]) /np.array(AveTrueRange)
DI_negative = 100*np.array(Direction[1][13:]) /np.array(AveTrueRange)


plt.plot(DI_negative,'r', label='Negative')
plt.plot(DI_positive,label= 'Positive')
plt.legend(loc='best')
