
import numpy as np
import pandas as pd
import nsfg
#import chap01ex as c1
import datsys as ds
import matplotlib.pyplot as plt
import thinkstats2 as ts2
import thinkplot as tp
import scipy.stats as ss

def ReadFemResp(dct_f="2002FemResp.dct", dat_f="2002FemResp.dat.gz"):
    dct = ts2.ReadStataDct(dct_f)
    df = dct.ReadFixedWidth(dat_f, compression="gzip")
    #CleanFemPreg(df)
    return df

def ReadBabyBoom(dat_f="babyboom.dat"):
    var_info = [
        ('time', 1, 8, int),
        ('sex', 9, 16, int),
        ('weight_g', 17, 24, int),
        ('minutes', 25, 32, int),
    ]
    columns = ['name', 'start', 'end', 'type']
    variables = pd.DataFrame(var_info, columns=columns)
    variables.end += 1
    dct = ts2.FixedWidthVariables(variables, index_base=1)

    df = dct.ReadFixedWidth(dat_f, skiprows=59)
    return df


#1  data import
dfp = nsfg.ReadFemPreg()
#dfr = c1.ReadFemResp()
dfr = ReadFemResp()

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
"""
# PMF is done manually with
pmfpl2 = [dictpl.values[x]/float(len(firsts.prglngth)) for x in range(0,len(dictpl))]
***Make it a dict instead with dictpl.keys() as keys***
"""
n1, bins1, typ1 = plt.hist(firsts.prglngth, bins=range(0, int(max(firsts.prglngth))+1), normed=True)
n2, bins2, typ2 = plt.hist(laters.prglngth, bins=range(0, int(max(laters.prglngth))+1), normed=True)
#or firsts.prglngth.hist(bins=range(0, int(max(firsts.prglngth))+1), normed=True)

#Calculating and plotting probabiltiy differences between two groups
plt.clf()
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

    ***numpy
    bins = 200
    n4, bin_edges, rec4 = plt.hist(diffs.dropna(), bins=bins, normed=True)
    cdf = np.cumsum(n4)
    plt.plot(bin_edges[1:], cdf)

"""


#7 Modeling distributions
dfb = ReadBabyBoom()
#Exponential distribution - used for modeling distribution of time intervals between events
"""
diffs = dfb.minutes.diff()
bins = 200
n4, bin_edges = plt.hist(diffs.dropna(), bins=bins, normed=True)
cdf = np.cumsum(n4)
plt.plot(bin_edges[1:], cdf)
#complementary (ccdf)
ccdf = 1 - df
plt.plot(bin_edges[1:], np.log(ccdf))
"""

#Normal distribution
"""
scipy.stats.norm()
"""
#Normal probability plot
"""
x = firsts.birthwgt_lb.dropna().sort_values()
gauss=np.random.normal(0, 1, len(x))
plt.plot(sort(gauss), x.values)

Alternatively:
ts2.NormalProbabilityPlot(x)
ss.probplot(firsts.birthwgt_lb.dropna(), plot=plt)
"""

