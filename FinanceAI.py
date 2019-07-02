def PosMov(high):
    '''
    Function to return today's high - yesterday's high
    Input: 
        list of size n
    Output: 
        list of size n-1
    What is means:
        If positive, means today's high is larger than yesterday. 
        Trending updward
    '''
    a = [high[i] - high[i-1] for i in range(1,len(high))]
    return a 

def NegMove(low):
    '''
    Function to return yesterday's low - today's low
    Input:
        list of size n
    Output:
        list of size n-1
    What it means:
        If positive, means yesterday's low is bigger than today's
        The price is varying up. 
    '''
    a = [low[i-1] -low[i] for i in range(1,len(low))]
    return a 
    
def DirectionalMovement(Up,Down):
    '''
    Function to compare the directional movement
    Input:
        Two lists, size n
    Output:
        Two lists, size n
    What it means:
        Whichever list has more zeros, it means it has the
        lower values
    '''
    DmPos = []
    DmNeg = []
    for i in range(0,len(Up)):
        if Up[i] > Down[i] and Up[i] >0:
            DmPos.append(Up[i])
        else:
            DmPos.append(0)
    for m in range(0,len(Down)):
        if Down[m] >Up[m] and Down[m] >0:
            DmNeg.append(Down[m])
        else:
            DmNeg.append(0)
    return DmPos,DmNeg

def TR(high, low, close):
    '''
    Function to determine true range. This is a relationship
    between high, low and previous close values
    Input:
        three lists, size n
    Output:
        one list, size n-1
    What does it mean:
        Compares the differences between high, low and previous
        close and chooses the highest one. Meaning, highest
        volitality
    '''
    case_a = [high[i] - low[i] for i in range(1,len(high))]
    case_b = [high[i] - close[i-1] for i in range(1,len(close))]
    case_c = [low[i] - close[i-1] for i in range(1,len(low))]
    TR = []
    for i in range(0,len(case_a)):
        TR.append(max(case_a[i],abs(case_b[i]),abs(case_c[i])))
    return TR

def ATR(trueRange, periods):
    '''
    Function to calculate the average true range for a given
    period
    Input:
        list of true values
        float - interval to calculate the averages on
    Output:
        list containing the average true values
    '''
    first = [sum(trueRange[:periods])/len(trueRange[:periods])]
    Ave= first 
    for i in range(periods,len(trueRange)):
        Ave.append((Ave[i-periods]*(periods-1)+trueRange[i])/periods)
    return Ave

def SMMA(Close,periods):
    '''
    Function to for smoothed moving average. Function takes a list
    and a period and uses it to calculate a smooter line
    Input:
        list of size n
        periods as integer
    Output:
        list of SMMA, smoothed moving averages of size n-1
    '''
    WeightedSum = [0]
    WeightedCount =[0]
    SMMA = []
    alpha = 1/periods
    for i in range(1,len(Close)):
        WeightedSum.append(Close[i] + (1-alpha)*WeightedSum[i-1])
        WeightedCount.append(1 + (1-alpha)*WeightedCount[i-1])
        SMMA.append(WeightedSum[i]/WeightedCount[i])
    return SMMA

# def DiPos(DMPlus,DMVe,ATR,periods):
#     DiPos = []
#     DiVe = []
#     for i in range(0,len(ATR)):
#         DiPos.append(100 * DMPlus[i+periods-2] /ATR[i])
#         DiVe.append(100*DMVe[i+periods-2]/ATR[i])
    
#     return DiPos,DiVe

def DI(DMPos,DMVe,ATR,periods):
    '''
    Function to find the Directional movement of the signals.

    Input:
        Positive movement; size n
        Negative movement; size n
        average true range size n-periods
        periods over which the ATR was calculated; periods
    Output:
        two lists. one for the DI+ and one for DI-
        sized n-periods
    '''

    from numpy import array
    from FinanceAI import SMMA
    DMPos= array(DMPos)
    DMVe = array(DMVe)
    ATR = array(ATR)
    bb = DMPos[periods-1:]/ATR
    cc = DMVe[periods-1:]/ATR
# 
    return 100*array(SMMA(bb,periods)),100*array(SMMA(cc,periods))

def ADX(high,low,close,periods):
    import FinanceAI as fn
    import numpy as np 
    aa = fn.DirectionalMovement(fn.PosMov(high),fn.NegMove(low))
    bb = fn.ATR(fn.TR(high,low,close),periods)
    cc = fn.DI(aa[0],aa[1],bb,periods)
    # 
    return 100*((np.abs(cc[0])-np.abs(cc[1]))/(np.abs(cc[0])+np.abs(cc[1])))

