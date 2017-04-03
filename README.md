README

# How to run the program
python viagogo.py


# Example Run
Input coords:> 8,9
Closest Events to (8, 9):
Event 023 - $0.35, Distance 2
Event 014 - $9.29, Distance 5
Event 012 - $12.58, Distance 7
Event 026 - $8.05, Distance 9
Event 013 - $23.60, Distance 15


# Analysis
I chose Python to complete this task. I have created 4 classes, and here I describe the gist of their functionality:

1) Point class
The Point class represents a point in the desired range (i.e. from -10 to +10 in both axis). Each point holds its x,y coordinates, one event, and can calculate the Manhattan distance to another point.

2) Event class
The Event class represents an event. Each event has a unique id, holds a point (the location where this event takes place), and a list of tickets.

3) Ticket class
The Ticket class represents a ticket.

4) PointCollection class
The PointCollection class is responsible for creating and manipulating point instances. Among others it maintains a list of all points, and it can create points, as well as events for points. 


# Tests
Unit tests are executed before the main function, so if there is something wrong in the code it will signal before execution has started.


# Assumptions Made
1) Ticket price <= 400.00 (I just chose a number >0)
2) Number of tickets <= 100 (rather small number to save some time while creating tickets)
3) Closest events have available tickets.
4) Total number of points (and thus events) are 20. (I just chose a number > 5)


# Changes to support multiple events at the same location
The Point class would be altered to maintain a list of events rather than one event. Assuming we have a list of events for each point, then for each of the points that are close to a location given by the user we can go through all of the events and present them to the user.


# Changes to work with a much larger world size
1) I wouldn’t be able to store everything in memory so I would use a database like SQLite. This presumably would make querying both easier and more efficient. Moreover, it would allow me to query for a variety of things that now I cannot.
2) I would group points into larger areas that I would names for. For instance, 100 events might have different coordinates, but all could be in ‘London’. 
3) I would optimise for speed. e.g. in function findClosestEvents() I know that the total number of events I am creating are 20 (see assumptions made) so I know everything can be stored in memory and have fast results. If events were more I would not keep a list of all events and then sort it based on distance, but rather have a list of only 5 elements and add/remove events more efficiently.
4) I would use different data structures such as a hashSet to store points with the coordinates as key. This would give me O(1) search/insertion/deletion (assuming no collisions), rather than the current O(n) search/deletion where I iterate a list.

