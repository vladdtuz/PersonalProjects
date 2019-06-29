import FinanceAI as fn 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  

high = np.random.randint(0,high=1000,size=500)
low = np.random.randint(1,high=1000,size=500)
close = np.random.randint(0,high=1000,size=500)

a = fn.DirectionalMovement(
            fn.PosMov(high),fn.NegMove(low))

b = fn.ATR(fn.TR(high,low,close),14)

DMPositive_smooth = fn.SMMA(a[0],14)
DMNegavtive_smooth = fn.SMMA(a[1],14) 

c = fn.DiPos(DMPositive_smooth,DMNegavtive_smooth,b,14)