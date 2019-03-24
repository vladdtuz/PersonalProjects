import pandas as pd
import numpy as np

odds =[[1.83,3.40,1],
      [1.,3.5,4.4],
      [ 1.89,1,4.10]]
odds2 = [[13,10,1],
      [1.1,2,3],
      [1.5,1.1,1.5]]

def TrueProb (OddsData):
    """ 
    Function to identify true odds 
    of the outcome. Makes the average from 
    all betting websites
    Each game should be in a seprate list with their respective odds
    
    Input :
       OddsData : requires input in the format of 3 numbers. 
       Team A Odds
       Team B odds
       Draw Odds
    Output:
        Averaged Odds for each outcome
    """
    prob =1/np.array(OddsData) 
    true_prob = np.average(np.transpose(prob),axis=-1)
    return true_prob

def TrueOdds (TrueProbability):
    """
    Functions to define True and fair  odds based on true probability. 
    Odds on which to bet on. 
    Analysis is calculated on a 'per element basis'.
    If x elements are given, x odds will be calculated
    Input:
       True probability
    Output:
       Favourable odds 
    """
    true_odds = 1/(np.array(TrueProbability) - 0.05)
    return true_odds

def ToBuy (OfferedOdds, TrueOddsArray):
    """"
    Function to identify which site and which game to buy odds from
    Input:
        OfferedOdds : site offered odds
        TrueOdds:     caluclated true odds
    Output:
     Game and website to buy odds from.
     Provides 3 outputs. best buying site when buying A, or B or Draw
     """
    offeredOdds = pd.DataFrame(odds, columns =['TeamA','Draw','TeamB'],index=['SiteA','SiteB','SiteC'])
    TobuyDf = pd.DataFrame()
    TobuyDf['FavourableOnA'] = offeredOdds['TeamA'].where(offeredOdds['TeamA'] > TrueOddsArray[0])
    TobuyDf['FavourableOnDraw'] = offeredOdds['Draw'].where(offeredOdds['Draw'] > TrueOddsArray[1])
    TobuyDf['FavourableOnB'] = offeredOdds['TeamB'].where(offeredOdds['TeamB'] > TrueOddsArray[2])
    winA = TobuyDf.sort_values(by=['FavourableOnA'],ascending=False)
    winB = TobuyDf.sort_values(by=['FavourableOnB'],ascending=False)
    draw = TobuyDf.sort_values(by=['FavourableOnDraw'],ascending=False)
    return winA,winB,draw

