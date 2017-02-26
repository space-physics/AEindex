from datetime import datetime,timedelta
from dateutil.parser import parse
from pytz import UTC
from pandas import read_fwf, DataFrame
from matplotlib.pyplot import figure
import seaborn as sns
sns.set_style('whitegrid')
#
from sciencedates import forceutc

def readae(fn,tlim):
    if tlim is not None:
        tlim[0] = forceutc(parse(tlim[0]))
        tlim[1] = forceutc(parse(tlim[1]))
    
    C = [(a,b) for a,b in zip(range(34,389,6),range(40,395,6))]
    cols = [(12,14),(14,16),(16,18),(19,21),(21,24)] + C
    
    # names=['year','month','day',hour','var']
    D = read_fwf(fn,cols,header=None)
    #%% one iteration per hour
    dat = DataFrame(columns=['AE','AU','AL','AO'])
    for i,d in D.iterrows():
        t0 = datetime(2000+d[0], d[1], d[2], d[3], tzinfo=UTC)
        
        if tlim and (t0 + timedelta(hours=1) < tlim[0] or t0 > tlim[1]):
            continue
            
        for j in range(60):
            t = t0 + timedelta(minutes=j)
            dat.loc[t, d[4]] = d[5+j]
    
    # below two lines don't work unless preassigned time
        #t = [t0 + timedelta(minutes=k) for k in range(60)]
        #dat.loc[t,d[4]] = d[5:65]
        
    return dat

def plotae(dat,tlim):
    ax = figure().gca()
    dat.plot(ax=ax)
    ax.set_xlabel('time [UTC]')
    ax.set_ylabel('index value')
    ax.set_title('Auroral Electrojet Indices')
    ax.set_xlim(tlim)
