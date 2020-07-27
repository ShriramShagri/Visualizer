# Algorithm Visualiser

A simple tool built step by step visualisation for path finding and maze creating algorithms 

[](https://github.com/ShriramShagri/Visualiser/blob/master/Fonts/Example.png)

### Included algorithms:

Path Finding:
* [A* Path finding algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/astar.py)
* [Dijkstra algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/dijkstra.py)

Maze:
* [Prim's algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/prims.py)
* [Kruskal's algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/kruskal.py)
* [Sidewinder algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/sidewinder.py)
* [Eller's algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/ellers.py)
* [Recursive backtracking algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/recursive_backtracking.py)
* [Aldous Broder algorithm (Modified)](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/aldous_broder.py)
* [Wilson's algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/wilson.py)
* [Hunt and Kill algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/hunt_and_kill.py) (Modified)
* [Growing Tree algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/growing_tree.py) (newest and random choices combined)
* [Binary Tree algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/binary_tree.py)
* [Recursive division algorithm](https://github.com/ShriramShagri/Visualiser/blob/master/Algorithms/recursive_division.py)

---
#### To run the application:

Install modules
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

Run to get started right away!:
```bash
python app.py
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
|  r 	|  Draw maze using Recursive backtracking algorithm	|
|  u 	|  Draw maze using Aldous Broder algorithm	|
|  h 	|  Draw maze using Hunt and Kill algorithm	|
|   g	|  Draw maze using Growing Tree algorithm	|
|   b	|  Draw maze using Binary Tree algorithm	|
|   q	|  Draw maze using Recursive Division algorithm	|
|  w 	|  	Draw maze using Wilson's algorithm|
|  e 	|  	Draw maze using Eller's algorithm|
| a  	|  Run A* algorithm	|
| d  	|  Run Dijkstra algorithm	|
|   	|  	|

#### Note:
1) Maze algorithms don't work if start and end nodes are mentioned already.
2) Path finding algorithms work only if start and end nodes are mentioned.
