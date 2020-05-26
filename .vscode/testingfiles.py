import matplotlib.pyplot as mplt  
import numpy as np
fig = mplt.figure()  
ax = fig.add_subplot(111) 
ax.plot([1,2,3,5],[1,2,1,3])  
plotlim = mplt.xlim() + mplt.ylim()  
test = np.array( [[0,0],[4,1]]).T
ax.imshow(test, cmap=mplt.cm.Greens, interpolation='bicubic', extent=plotlim)  
mplt.draw()  
mplt.show()