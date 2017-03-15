import math
c = float(input()) #side AB - casting it to float as python 2 will force cast everything to int and very small values get casted to 0
a = float(input()) #side BC
# calcualting denominator part of arcsine calculation
u = (((pow((pow(a,2)+pow(c,2)),0.5))/2)*math.sin(math.radians(math.degrees(math.atan(float(c/a))))))
# calcualting numerator part of arcsine calculation
l = pow((pow(a,2)+pow(((pow((pow(a,2)+pow(c,2)),0.5))/2),2) - 2*a*((pow((pow(a,2)+pow(c,2)),0.5))/2)*math.cos(math.radians(math.degrees(math.atan(c/a))))),0.5)
MBC = float(math.degrees(math.asin(u/l)))
print str(int(round(MBC,0)))+u'\u00b0'
