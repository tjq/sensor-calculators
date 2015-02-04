import math
import sys
 
h = 1000
vFOV = 41.25
zoom1 = input("Detection zoom: ")
zoom2 = input("Confirmation zoom: ")
vFOVz1 = (vFOV/zoom1)
vFOVz2 = (vFOV/zoom2)
a1 = input("Angle of inclination: ")
a2 = ((vFOVz1 - vFOVz2)/2) + a1
print "Angle of confirmation incl: %s" %a2
y1 = 90 - (vFOVz1 + a1)
y2 = 90 - (vFOVz2 + a2)
maxFOV = input("Contraints on FOV (from Vertical): ")
d1 = h * math.tan(math.radians(a1))
d2 = h * math.tan(math.radians(a2))


#Calculate width of detection and confirmation footprints
z1 = (h/math.tan(math.radians(y1))) - d1
print "Width of detection FOV = %s ft" %z1
z2 = h/math.tan(math.radians(y2)) - d2
print "Width of confirmation FOV = %s ft" %z2

#Finding maximum detection velocity
v1fps = (2.0 * h * math.tan(math.radians(vFOVz1/2)))/(0.5)
v1 = v1fps * (3600.0/5280.0)
print "Max velocity during detection = %s mph" %v1

dist1 = v1/2 

#Finding maximum confirmation velocity
v2fps = (z2+(1000*math.tan(math.radians(maxFOV))))/5
v2 = v2fps * (3600.0/5280.0)
print "Max velocity during confirmation = %s mph" %v2

#Setting detection, confirmation, and maximum FOV 
dFOV = math.fabs(vFOVz1 + a1)
cFOV = math.fabs(vFOVz2 + a2)
mFOV = 2 * maxFOV
         
#If Statements re: field of view being too large.
if dFOV > mFOV or cFOV > mFOV:
	print '*** FOV is too great for this zone! *** '
if dFOV >  mFOV:
	print 'Detection field of view = %s, max is %s deg' %(dFOV, mFOV)
if cFOV > mFOV:
	print 'Confirmation field of view = %s, max is %s deg' %(cFOV, mFOV)
else:
	sys.exit()