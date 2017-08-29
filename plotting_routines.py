
# coding: utf-8

# In[ ]:

# import needed modules
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sb

# plot with errorbar
def plot_tc(tc,tce,col,coll,**kwargs):
    """ Plot given tuning curve with shaded errorbars.
    
    Arguments:
    
      *tc*:
        Vector containing tuning curve
      *tce*:
        Vector containing tuning curve error
      *col*:
        Color of tc error shade (rgb triplet)
      *coll*:
        Color of tc line (rgb triplet)
        
    Keyword arguments:
    
      *osi*:
        osi index value
      *dsi*:
        dsi index value
        
    """    
    dirs=np.arange(0,360,30)
    xpo=200
    ypo=max(tc+tce)
    plt.plot(dirs,tc,linewidth=3,color=coll)
    plt.fill_between(dirs,tc-tce,tc+tce,alpha=0.5,edgecolor=col,facecolor=col)
    if bool(kwargs) and len(kwargs)==2:
        s1='DSI = '+ "%.2f" % kwargs['dsi']
        s2='OSI = '+ "%.2f" % kwargs['osi']
        plt.text(1*xpo, 0.9*ypo, s1, fontsize=15, fontweight='bold')
        plt.text(1*xpo, 0.8*ypo, s2, fontsize=15, fontweight='bold')
    elif bool(kwargs) and len(kwargs)==1:
        print('WARNING: Two optional arguments needed!')
        
    return []

