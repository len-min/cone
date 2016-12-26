import matplotlib
matplotlib.use('qt5agg')

import matplotlib.pyplot as plt

import numpy as np

print "Hello"

k = 5
#k2 = 10
h = 5

def sec( k, k2, h ):
    alpha = np.arange( 0, 2 * np.pi, 0.01 )

    rads = [ h / (k- k2*np.cos(a)) for a in alpha ]

    rplane = [ r*np.sqrt(1+k*k) for r in rads ]
    alpha_plane = [ np.pi/2 - np.pi/k + a/k for a in alpha ]

    r_a_plane = zip( rplane, alpha_plane )
    xplane = [ r * np.cos( a ) for (r,a) in r_a_plane ]
    yplane = [ r * np.sin( a ) for (r,a) in r_a_plane ]

    return xplane, yplane

x1, y1 = sec( k, 0.5, h )
plt.plot(x1, y1)

x2, y2 = sec( k, 1, h )
plt.plot(x2, y2)

x3, y3 = sec( k, 0.0, h )
plt.plot(x3, y3)

x4, y4 = sec( k, np.sqrt(3), h )
plt.plot(x4, y4)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
#plt.savefig("~/test.png")
plt.show()