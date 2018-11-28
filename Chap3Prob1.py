from math import sin, cos, radians

LatOfAtl, LongOfAtl = 33.7524500,-84.3920200
LatOfOrl, LongOfOrl = 28.4115300,-81.5250400
LatOfSav, LongOfSav = 32.1672300,-81.1998900
LatOfChar, LongOfChar = 35.2072400,-80.9567600

def distanceBetweenCities(x1,y1,x2,y2):
    d = 6371.01 * cos(sin(radians(x1))* sin(radians(x2)) + cos(radians(x1))* cos(radians(x2))* cos((radians(y1)) - (radians(y2))) )
    return d
    
disBetCharSav = distanceBetweenCities(LatOfChar, LongOfChar,LatOfChar, LongOfChar)
disBetSavOrl = distanceBetweenCities(LatOfSav, LongOfSav, LatOfSav, LongOfSav)
disBetOrlAtl = distanceBetweenCities(LatOfOrl, LongOfOrl, LatOfAtl, LongOfAtl)
disBetAtlChar = distanceBetweenCities(LatOfAtl, LongOfAtl, LatOfChar, LongOfChar)
disBetCharOrl = distanceBetweenCities(LatOfChar, LongOfChar, LatOfOrl, LongOfOrl)

def areaOfTriange(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    return area
    
AreaCoveredByCities = areaOfTriange(disBetCharSav, disBetSavOrl, disBetCharOrl)+ areaOfTriange(disBetCharOrl, disBetAtlChar, disBetOrlAtl)
print("Area enclosed by Atlanta, Orlando, Savannah and Charlotte is  ", AreaCoveredByCities, "km*km")
