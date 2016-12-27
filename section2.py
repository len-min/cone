import matplotlib
matplotlib.use('qt5agg')

import matplotlib.pyplot as plt

import numpy as np

print "Hello"

k = 10000
#k2 = 10
h = 10000

def from_rad_to_xy( rad, alpha ):
    r_a = zip(rad, alpha)
    xplane = [r * np.cos(a) for (r, a) in r_a]
    yplane = [r * np.sin(a) for (r, a) in r_a]
    return xplane, yplane

def sec( k, k2, h ):
    alpha = np.arange( 0, 2 * np.pi, 0.01 )

    rads = [ h / (k- k2*np.cos(a)) for a in alpha ]

    rplane = [ r*np.sqrt(1+k*k) for r in rads ]
    alpha_plane = [ np.pi/2 - np.pi/k + a/k for a in alpha ]

    return from_rad_to_xy( rplane, alpha_plane )

def hor_bounds( k, h ):
    alpha = np.arange(0, 2 * np.pi, 0.01)
    alpha_plane = [np.pi / 2 - np.pi / k + a / k for a in alpha]

    rplane = [ h ] * len( alpha_plane )

    return from_rad_to_xy(rplane, alpha_plane)

#def bounds( h0, h1 ):
#    x =

x1, y1 = sec( k, 0.5, h )
plt.plot(x1, y1)

x2, y2 = sec( k, 1, h )
plt.plot(x2, y2)

x3, y3 = sec( k, 0.0, h )
plt.plot(x3, y3)

x4, y4 = sec( k, np.sqrt(3), h )
plt.plot(x4, y4)

hor_x_0, hor_y_0 = hor_bounds( k, h - 2 )
plt.plot(hor_x_0, hor_y_0)

hor_x_1, hor_y_1 = hor_bounds( k, h + 2 )
plt.plot(hor_x_1, hor_y_1)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.ylim( [h - 3, h+ 3] )
plt.savefig("G:\\test.png")
plt.show()