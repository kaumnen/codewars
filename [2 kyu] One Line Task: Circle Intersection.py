from numpy import*;circleIntersection=lambda a,b,r:r*r*(lambda h:h<1and arccos(h)-h*(1-h*h)**.5)(hypot(*subtract(b,a))/r/2)//.5
