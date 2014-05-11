import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def U(Z,x,y):
    N=x.size
    A=np.ones_like(Z) 
    return A

def f(x,y):
    return x*y**2
#cnabfsd 1


a=0.
b=1.
N=30
delta = (b-a)/N
print delta
x = y = np.arange(a, b, delta)
X, Y = np.meshgrid(x, y)
print X
N=x.size
Z=np.zeros(X.size).reshape(N,N)
Z[0,0:]=100.
print Z
#Z=U(Z,x,y)
Z[0:,0:]=f(X[0:,0:],Y[0:,0:])


#-------------------------1----------------------------
im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
                origin='lower', extent=[a,b,a,b],
                vmax=abs(Z).max(), vmin=-abs(Z).max())
plt.title ("GEO line")
#------------------------2-----------------------------

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
plt.title ("3D")



plt.show()
