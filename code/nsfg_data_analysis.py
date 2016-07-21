
import numpy as np
import pandas as pd
import nsfg
import chap01ex as c1
import datsys as ds
import matplotlib.pyplot as plt
import thinkstats2 as ts2
import thinkplot as tp

#1  data import
dfp = nsfg.ReadFemPreg()
dfr = c1.ReadFemResp()

#2  data cleaning
nsfg.CleanFemPreg(dfp) #Clean data however it has to be done
#CleanFemResp(dfr)

#3  looking at variables
#pregordr = dfp['pregordr'] #pregordr = df.pregordr
#dfr.pregnum
live = dfp[dfp.outcome==1]
firsts = live[live.birthord==1]
laters = live[live.birthord>1]


"""
    Take a look at the different columns and understand the data.
    Look for inconsistencies and errors
"""

#4  Plotting, analysing distributions, and summary statistics
"""
    see plot_test.py

******DO EXCERCISE 2.2 and 2.4*******
"""

#5  Probability mass functions/Probabilty distribution functions
n1, bins1, typ1 = plt.hist(firsts.prglngth, bins=range(0, int(max(firsts.prglngth))+1), normed=True)
n2, bins2, typ2 = plt.hist(laters.prglngth, bins=range(0, int(max(laters.prglngth))+1), normed=True)
#or firsts.prglngth.hist(bins=range(0, int(max(firsts.prglngth))+1), normed=True)

#Calculating and plotting probabiltiy differences between two groups
weeks = bins1[:-1]
diffs = [100*(n1[week]-n2[week]) for week in weeks]  #scalar 100 for bigger bars
plt.bar(weeks[35:47], diffs[35:47])
plt.show()

#******DO CHAPTER 3 EXCERCISES*******

#6  CDF (Cumulative Distribution Function)
"""
    n3, bins3, rec3 = plt.hist(pl,bins=range(0,max(pl)+1), normed=True,cumulative=True)
    firsts.totalwgt_lb.hist(bins=150, normed=True, cumulative=True)
    ts2.Cdf(pl)
"""