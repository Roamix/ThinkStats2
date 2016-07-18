"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(dct_f="2002FemResp.dct", dat_f="2002FemResp.dat.gz"):
    dct = thinkstats2.ReadStataDct(dct_f)
    df = dct.ReadFixedWidth(dat_f, compression="gzip")
    #CleanFemPreg(df)
    return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)

#    df = ReadFemResp()




if __name__ == '__main__':
    main(*sys.argv)
