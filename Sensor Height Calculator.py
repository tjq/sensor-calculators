import math

hfov = 55
vfov = 41.25
hres = 640.0
wp = 4
PD = input('Pixels detected: ')
a = input('Angle of Inclination: ')
zoom = 1.51
maxzoom = 10

print '------------------------------------------'

while zoom <= maxzoom:
	hFOVz = hfov / zoom
	vFOVz = vfov / zoom
	diam = (hFOVz)/(hres)
	diamreq = diam * PD #where diamreq = diamper
	D = wp/(2*math.tan(math.radians(diamreq/2)))
	h = D * math.cos(math.radians(vFOVz + a))
	print '%s              %s' %(h,zoom)
	zoom = zoom + .01
	
	
	
	


	
	
	

