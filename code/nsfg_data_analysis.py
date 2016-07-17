import numpy as np

import nsfg
import chap01ex as c1
import datsys as ds
import matplotlib.pyplot as plt

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


    #Take a look at the different columns and understand the data.
    #Look for inconsistencies and errors

#4  Plotting, analysing distributions, and summary statistics
    #see plot_test.py

##******DO EXCERCISE 2.2 and 2.4*******

#5  Probability mass functions
