import math

h = input('Height: ')
vFOV = input('Vertical FOV: ')
hFOV = input('Horizontal FOV: ')
zoom = input('Zoom: ')
vFOVz = vFOV/zoom
hFOVz = hFOV/zoom
a = input("Angle of inclination: ")
y = 90 - (vFOV + a)


#Calculate dead space	
d = h * math.tan(math.radians(a))

#Calculate width of trapezoid
z = h/math.tan(math.radians(y)) - d
print "Width of trapezoid = %s ft" %z

#Calculate slant lengths
sf = h/math.cos(math.radians(vFOVz + a))
sb = h/math.cos(math.radians(a))

#Calculate front and back widths
wf = 2 * sf * math.atan(math.radians(.5 * hFOVz))
wb = 2 * sb * math.atan(math.radians(.5 * hFOVz))

print "Front width = %s ft; Back width = %s ft" %(wf, wb)

#Calculate area
Area = ((wf + wb)*z)/2
print "Area = %s ft^2" %Area
	