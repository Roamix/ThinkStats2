import thinkplot
import thinkstats2
import numpy as np
import chap01ex as c1
import nsfg
import matplotlib.pyplot as pp
import math

#th = thinkstats2.Hist([1,2,2,3,5])
#thinkplot.Hist(th)
#thinkplot.show(xlabel='value', ylabel='frequency')

dfr = c1.ReadFemResp()
dfp = nsfg.ReadFemPreg()

""" Not necessary
pn_hist = {}
wgt_hist = {}
for x in dfr.pregnum:
    pn_hist[x] = pn_hist.get(x, 0) + 1

for x in dfp.birthwgt_lb:
    if x >= 0:
        wgt_hist[x] = wgt_hist.get(x, 0) + 1

#pp.hist(histo.values())
#pp.bar(histo.keys(), histo.values(), 1, color="g")
"""

#matplotlib can take panda Series as argument if cleaned properly (no NaN etc.)
"""
pp.hist(dfr.pregnum, int(max(dfr.pregnum) + 1))
pp.title("Number of pregnancies")
pp.xlabel("value")
pp.ylabel("frequency")
pp.show()
"""

#panda Series has matplotlib methods as well.
#                               max data value + 1
#dfp.birthwgt_lb.hist(bins=int(max(dfp.birthwgt_lb) + 1))

#Looking for outliers and errors. Any unatural pregnancy lengths?
live = dfp[dfp.outcome==1]
pl=live.prglngth
pl_hist=pl.value_counts().sort_index()
#first 10 min values and 10 max values
mins = pl_hist.keys()[:10]
maxs = pl_hist.keys()[len(pl_hist):-10]

#Comparing pregnancy length distributions of live first borns and later borns
firsts = live[live.birthord==1]
laters = live[live.birthord > 1]

fpl_hist = firsts.prglngth.value_counts().sort_index()
lpl_hist = laters.prglngth.value_counts().sort_index()

#On same axis
fp=firsts.prglngth.hist(bins=max(firsts.prglngth)+1,width=0.7)
lp=laters.prglngth.hist(bins=max(laters.prglngth)+1, width=0.7, align="right")

#As Subplots
fig, axes = pp.subplots(1,2)
fp=firsts.prglngth.hist(bins=max(firsts.prglngth)+1,ax=axes[0])
lp=laters.prglngth.hist(bins=max(laters.prglngth)+1, ax=axes[1])

mf = firsts.prglngth.mean()
vf = firsts.prglngth.var()
ml = laters.prglngth.mean()
vl = laters.prglngth.var()

diff = mf-ml

nf, nl = len(firsts.prglngth), len(laters.prglngth)
pool_var = (nf * vf + nl * vl)/(nf + nl)
s = math.sqrt(pool_var)
d = diff/s