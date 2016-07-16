import numpy as np

import nsfg

#data import
df = nsfg.ReadFemPreg()
pregordr = df['pregordr'] #pregordr = df.pregordr
#Take a look at the different columns and understand the data.
#Look for inconsistencies and errors

#data cleaning
nsfg.CleanFemPreg(df)
#Clean data however it has to be done
