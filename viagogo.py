
import random

class Point():
	''' This class represents points '''

	def __init__(self, x, y):
		self._x = x
		self._y = y


	def setEvent(self, e):
		self._event = e


	def getEvent(self):
		return self._event


	def setX(self, x):
		self._x = x


	def getX(self):
		return self._x


	def setY(self, y):
		self._y = y


	def getY(self):
		return self._y


	def distanceFromPoint(self, point):
		''' calculates the Manhattan distance between this 
		and another point '''

		return abs(self.getX() - point.getX()) + \
			abs(self.getY() - point.getY())


class Event():
	''' This class represents events '''

	_ID = 0

	def __init__(self, point):
		self._id = Event._ID
		Event._ID += 1
		self._tickets = []
		self._point = point


	def getID(self):
		return self._id


	def setPoint(self, point):
		self._point = point


	def getPoint(self):
		return self._point


	def setTicketsList(self, ticketList):
		for t in ticketList:
			if self.isTicketPricePositive(t.getPrice()):
				self._tickets = ticketList


	def addSingleTicket(self, ticket):
		if self.isTicketPricePositive(ticket.getPrice()):
			self._tickets.append(ticket)


	def addTicketList(self, ticketList):
		for t in ticketList:
			if self.isTicketPricePositive(t.getPrice()):
				self._tickets += ticketList


	def getTickets(self):
		return self._tickets


	def isTicketPricePositive(self, price):
		if price <= 0:
			print "Ticket price cannot be <= 0 "
		return price > 0


	def hasTickets(self):
		''' True if the event has tickets left '''

		return len(self.getTickets()) > 0


	def getCheapestTicket(self):
		''' Returns the cheapest ticket '''

		if self.hasTickets():
			return self.getTickets()[0]
		else:
			return -1


	def sortTicketPricesAscending(self):
		self._tickets.sort(key=lambda x: float(x.getPrice()), reverse=False)


	def sortTicketPricesDescending(self):
		self._tickets.sort(key=lambda x: float(x.getPrice()), reverse=True)


	def toString(self, distance):
		print "Event %.3d - $%.2f, Distance %d" % \
			(self.getID(), self.getCheapestTicket().getPrice(), distance)


	def createTicketsRandomly(self):
		''' Creates a random number of tickets between 0-100 with
		random prices ranging from 0.1 - 400.00 '''

		tickets = [Ticket(round(random.uniform(0.1, 400),2)) \
				for _ in xrange(random.randint(0, 100))]

		return tickets


class Ticket():
	''' This class represents a ticket '''

	def __init__(self, price):
		self._price = price


	def setPrice(self, price):
		self._price = price


	def getPrice(self):
		return self._price


class PointCollection():
	''' This class is responsible for creating and 
	manipulating instances of the Point class '''

	def __init__(self):
		self._limitX = [-10, 10]
		self._limitY = [-10, 10]
		self._points = []


	def createPoint(self):
		''' Creates a new point within the desired limits 
		and adds it to the list'''

		xCoord = random.randint(self._limitX[0], self._limitX[1])
		yCoord = random.randint(self._limitY[0], self._limitY[1])
		p = Point(xCoord, yCoord)

		# make sure we create a new point that does not already exist
		while self.pointExists(p):
			xCoord = random.randint(self._limitX[0], self._limitX[1])
			yCoord = random.randint(self._limitY[0], self._limitY[1])
			p = Point(xCoord, yCoord)

		self.addPoint(p)
		return p


	def pointExists(self, point):

		for p in self._points:
			if p.getX() == point.getX() and p.getY() == point.getY():
				return True
		return False


	def setLimitX(self, limitX):
		self._limitX = limitX


	def getLimitX(self):
		return self._limitX


	def setLimitY(self, limitY):
		self._limitY = limitY


	def getLimitY(self):
		return self._limitY


	def addPoint(self, point):
		''' Adds a point in the list, given that it is 
		within the limits '''

		if not self.isPointWithinLimits(point):
			print "Point(%d, %d) is not within limits" % (point.getX(), point.getY())
			return 
		self._points.append(point)


	def getPoints(self):
		''' Returns a list of all the points '''

		return self._points


	def isPointWithinLimits(self, point):
		''' Checks whether a point is within the 
		desired boundaries '''

		return (self._limitX[0] <= point.getX() <= self._limitX[1]) \
			and (self._limitY[0] <= point.getY() <= self._limitY[1])


	def createEventsForPoints(self):
		''' Create a random number of tickets and assign an
		event to each point '''

		for p in self._points:
			self.createEventAtPoint(p)


	def createEventAtPoint(self, point):
		''' Given a point creates a new event for it '''

		e = Event(point)
		tickets = e.createTicketsRandomly()
		e.setTicketsList(tickets)
		e.sortTicketPricesAscending()
		point.setEvent(e)


def generatePoints():
	''' Generates a random number of points > 5 and their 
	equivalent events '''

	pc = PointCollection()
	totalPoints = 20

	for _ in xrange(totalPoints):
		pc.createPoint()

	pc.createEventsForPoints()
	return pc


def findClosestEvents(point, pointCollection, numberOfEvents):
	''' Given a point and a collection of points returns a 
	sorted list containing 'numberOfEvents' closest events '''

	closestEvents = []

	for p in pointCollection.getPoints():
		dist = point.distanceFromPoint(p)
		e = p.getEvent()
		if e.hasTickets():
			closestEvents.append([e, dist])

	# sort based on distance
	closestEvents.sort(key=lambda x: int(x[1]), reverse=False)
	return closestEvents[:numberOfEvents]


def getPointFromUser(pc):
	''' Gets the input point from a user and returns a 
	point instance '''

	validInput = False
	while validInput == False:

		inp = input("Input coords:> ")
		if type(inp) == type((1,2)) and len(inp) == 2:
			p = Point(inp[0], inp[1])
			if not pc.isPointWithinLimits(p):
				print "Please enter a valid point"
			else:
				validInput = True
		else:
			print "Please enter a valid point"

	return p


def PointTest():
	''' Ensures that the Point class behaves as it should '''

	p = Point(0,0)
	assert p.getX() == 0
	assert p.getY() == 0
	p.setX(5)
	p.setY(8)
	assert p.getX() == 5
	assert p.getY() == 8
	assert p.distanceFromPoint(Point(0,0)) == 13


def EventTest():
	''' Ensures that the Event class behaves as it should '''

	p = Point(3,4)
	e = Event(p)
	assert e.getPoint() == p
	tickets = e.createTicketsRandomly()
	e.setTicketsList(tickets)
	e.sortTicketPricesAscending()

	# make sure tickets have been sorted by price in asc. order
	for i in range(1, len(e.getTickets())):
		prev = e.getTickets()[i-1].getPrice()
		cur = e.getTickets()[i].getPrice()
		assert prev < cur


def PointCollectionTest():
	''' Ensures that the PointCollection class behaves as it should '''

	pc = PointCollection()

	# create points (-3,-3), (-2,-2), ... , (7,7)
	for i in range(-3, 8):
		p = Point(i, i)
		pc.addPoint(p)

	pc.createEventsForPoints()

	p = Point(0,0)
	closestEvents = findClosestEvents(p, pc, 5)
	assert len(closestEvents) == 5
	assert closestEvents[0][1] == 0
	assert closestEvents[1][1] == 2
	assert closestEvents[2][1] == 2
	assert closestEvents[3][1] == 4
	assert closestEvents[4][1] == 4


def unitTests():

	PointTest()
	EventTest()
	PointCollectionTest()


def main():

	pointCollection = generatePoints()
	p = getPointFromUser(pointCollection)
	if p == -1:
		return

	closestEvents = findClosestEvents(p, pointCollection, 5)
	print "Closest Events to (%d, %d):" % (p.getX(), p.getY())
	for ce in closestEvents:
		ce[0].toString(ce[1])


if __name__ == '__main__':

	# Do the unit tests first.
	unitTests()

	main()

