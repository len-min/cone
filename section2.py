import matplotlib
matplotlib.use('qt5agg')

import matplotlib.pyplot as plt

import numpy as np

print "Hello"

pole_per = 5.6
pole_rad = pole_per / np.pi / 2

#k2 = 10
h = 10000
k = h / pole_rad

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

ysize = pole_per
sm_to_inches = 1/2.54
my_dpi = 100
plt.figure( figsize=(pole_per * sm_to_inches, ysize * sm_to_inches), dpi=my_dpi)

def add_sec( plt, h, angle, col, w ):
    x1, y1 = sec( k, np.tan( angle / 180.0 * np.pi), h )
    lines = plt.plot(x1, y1)
    plt.setp(lines, color=col, linewidth=w)

step = 0.5
off = 1.2
add_sec( plt, h+off       , 24, '#156526', 1)
add_sec( plt, h+off-step*1, 30, '#F96161', 2)
add_sec( plt, h+off-step*2, 34, '#FF7400', 1)
add_sec( plt, h+off-step*3, 38, 'r', 1)
add_sec( plt, h+off-step*4, 42, 'b', 1)

hor_x_0, hor_y_0 = hor_bounds( k, h - 2 )
plt.plot(hor_x_0, hor_y_0)

hor_x_1, hor_y_1 = hor_bounds( k, h + 2 )
plt.plot(hor_x_1, hor_y_1)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
#plt.grid(True)

plt.ylim( [h - ysize/2, h+ ysize/2] )
plt.xlim( [ - pole_per/2, pole_per/2 ] )

plt.savefig("G:\\test.png", dpi=600)
plt.show()