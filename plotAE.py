#!/usr/bin/env python
from matplotlib.pyplot import show
#
from aeindex import readae,plotae
"""
./plotAE.py data/WWW_aeasy00007552.dat -t 2013-05-01T07:00 2013-05-01T11:00
"""

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('fn',help='data filename')
    p.add_argument('-t','--tlim',help='min max time',nargs=2)
    p = p.parse_args()
    
    dat = readae(p.fn, p.tlim)
    plotae(dat,p.tlim)
    
    show()
    