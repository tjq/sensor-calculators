import math

h = input('Height: ')
vFOV = input("Vertical FOV: ")
zoom1 = input("Detection zoom: ")
zoom2 = input("Confirmation zoom: ")
vFOVz1 = (vFOV/zoom1)
vFOVz2 = (vFOV/zoom2)
a1 = input('Angle of Inclination: ')
a2 = ((-vFOVz1-vFOVz2)/2)
y1 = 90 - (vFOVz1 + a1)
y2 = 90 - (vFOVz2 + a2)
maxFOV = input("Contraints on FOV (from Vertical): ")
d1 = h * math.tan(math.radians(a1))
d2 = h * math.tan(math.radians(a2))

#Calculate width of trapezoid
z1 = (h/math.tan(math.radians(y1))) - d1
print "Width of detection FOV = %s ft" %z1

z2 = h/math.tan(math.radians(y2)) - d2
print "Width of confirmation FOV = %s ft" %z2

v1fps = (2.0 * h * math.tan(math.radians(vFOVz1/2)))/(0.5)
v1 = v1fps * (3600.0/5280.0)
print "Max velocity during detection = %s mph" %v1

dist1 = v1/2 

a2pan = math.atan(math.radians(((z1/2) - dist1)/1000)) - vFOVz2
print "Angle of pan, just after detection = %s degrees" %a2pan
d2pan = h * math.tan(math.radians(a2pan))
y2pan = 90 - (vFOVz2 + a2pan)
z2pan = h/math.tan(math.radians(y2pan)) - d2pan
print "Width of panned confirmation FOV = %s ft" %z2pan 

v2fps = (z2pan + (1000 * math.tan(math.radians(a2pan)))+(1000*math.tan(math.radians(maxFOV))))/5
v2 = v2fps * (3600.0/5280.0)
print "Max velocity during confirmation = %s mph" %v2