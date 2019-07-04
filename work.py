import FinanceAI as fn 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  

data = pd.read_csv('A.csv')
aa= fn.ADX(data['High'],data['Low'],data['Close'],14)
plt.plot(aa)