# Algorithm Visualiser

A simple tool built step by step visualisation for path finding and maze creating algorithms 

### Included algorithms:

Path Finding:
* A* Path finding algorithm
* Dijkstra algorithm

Maze:
* Prim's algorithm
* Kruskal's algorithm
* Sidewinder algorithm
* Recursive backtracking algorithm
* Aldous Broder algorithm
* Wilson's algorithm

---
#### To run the application:

Install pygame
```bash
pip install pygame
pip install argparse
```

Run command for more information:
```
python app.py -h
```
or
```
python app.py --help
```
---
#### To use the tool:
Different coloured squares represents the following:

|  Color 	|   Representation	|  
|---	|---	|
|   White	|  Empty Square 	|
|   Black	| Barrier  	|
|   Red	|   Visited	|
|   Green	|  To be visited 	|
|   Orange	|   Start Node	|
|   Teal	|   End Node	|
|   Purple	|   Shortest Path	|

Keys:

|   Key	|   Function	|
|---	|---	|
| Backspace  	|  Clear Screen 	|
|   Tab	|  Switch off or on grid 	|
|   Mouse Right Click	|   Clear node or obstacle	|
|   Mouse Left Click	|   Add Node or obstacle	|
| p  	|  Draw maze using Prim's algorithm	|
|  k 	|  Draw maze using Kruskal's algorithm	|
|   s	|  Draw maze using Sidewinder algorithm	|
|  b 	|  Draw maze using Recursive backtracking algorithm	|
|  u 	|  Draw maze using Aldous Broder algorithm	|
|  w 	|  	Draw maze using Wilson's algorithm|
|  e 	|  	Draw maze using Eller's algorithm|
| a  	|  Run A* algorithm	|
| d  	|  Run Dijkstra algorithm	|
|   	|  	|

#### Note:
1) Maze algorithms don't work if start and end nodes are mentioned already.
2) Path finding algorithms work only if start and end nodes are mentioned.
