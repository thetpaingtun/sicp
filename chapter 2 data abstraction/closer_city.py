from math import sqrt

def closer_city(lat,lon,city1,city2):
	current_point = point(lat,lon)
	distance_from_city1 = distance(current_point,getPoint(city1))
	distance_from_city2 = distance(current_point,getPoint(city2))
	print(getName(city1) if distance_from_city1 < distance_from_city2 else getName(city2))







#Return the distance of two points 
def distance(point1,point2):
	return sqrt(square(getX(point2)-getX(point1))+square(getY(point2)-getY(point1)))


#city constructor and selector

def city(name,point):
	return {"name":name,"point":point}


def getName(city):
	return city['name']

def getPoint(city):
	return city['point']


#point constructor and selector 

def point(x,y):
	return [x,y]


def getX(point):
	return point[0]


def getY(point):
	return point[1]


#helpers
def square(n):
	return n*n






##test ####
city1 = city("Berkeley",point(2,3))
city2 = city("New York",point(3,4))

closer_city(1,4,city1,city2)
closer_city(3,5,city1,city2)





