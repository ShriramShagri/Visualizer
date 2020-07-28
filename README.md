# Algorithm Visualiser

A simple tool built step by step visualisation for path finding, maze creating and sorting algorithms 

![Example](Fonts/Example.png "Example")

### Included algorithms:

Path Finding:
* [A* Path finding algorithm](Algorithms/astar.py)
* [Dijkstra algorithm](Algorithms/dijkstra.py)

Maze:
* [Prim's algorithm](Algorithms/prims.py)
* [Kruskal's algorithm](Algorithms/kruskal.py)
* [Sidewinder algorithm](Algorithms/sidewinder.py)
* [Eller's algorithm](Algorithms/ellers.py)
* [Recursive backtracking algorithm](Algorithms/recursive_backtracking.py)
* [Aldous Broder algorithm (Modified)](Algorithms/aldous_broder.py)
* [Wilson's algorithm](Algorithms/wilson.py)
* [Hunt and Kill algorithm](Algorithms/hunt_and_kill.py) (Modified)
* [Growing Tree algorithm](Algorithms/growing_tree.py) (newest and random choices combined)
* [Binary Tree algorithm](Algorithms/binary_tree.py)
* [Recursive division algorithm](Algorithms/recursive_division.py)

Sorting:
* [Bead / Gravity Sort](Sorts/bead.py)
* [Bitonic Sort](Sorts/bitonic.py)
* [Bogo / Stupid Sort](Sorts/Bogo.py)
* [Bubble Sort](Sorts/bubble.py)
* [Bucket / Bin Sort](Sorts/bucket.py)
* [Cocktail Shaker / Bidirectional Bubble / Ripple / Shuttle Sort](Sorts/cocktail.py)
* [Comb Sort](Sorts/comb.py)
* [Counting Sort](Sorts/counting.py)
* [Cycle Sort](Sorts/cycle.py)
* [Double Sort](Sorts/double.py)
* [Gnome / Dubbed Stupid Sort](Sorts/gnome.py)
* [Heap Sort](Sorts/heap.py)
* [Insertion Sort](Sorts/insertion.py)
* [Merge Sort](Sorts/iterativemerge.py) (Iterative method)
* [Merge Sort](Sorts/recursivemerge.py) (Recursive method)
* [Odd Even / Brick Sort](Sorts/oddeven.py)
* [Pancake Sort](Sorts/pancake.py)
* [Selection Sort](Sorts/selection.py)
* [Wiggle Sort](Sorts/wiggle.py)

---
#### To run the application:

Install modules
```bash
pip install pygame
pip install argparse
```

Run command for more information:
```bash
python app.py -h
or
python app.py --help
```

Run to get started right away!:
```bash
python app.py
```

---
#### To use the tool:
> Different coloured squares represents the following:

|  Color 	|   Representation	|  
|---	|---	|
|   White	|  Empty Square 	|
|   Black	| Barrier  	|
|   Red	|   Visited	|
|   Green	|  To be visited 	|
|   Orange	|   Start Node	|
|   Teal	|   End Node	|
|   Purple	|   Shortest Path	|

> Basic Keys:

|   Key	|   Function	|
|---	|---	|
| Backspace  	|  Clear Screen 	|
|   Tab	|  Switch off or on grid 	|
|   Mouse Right Click	|   Clear node or obstacle	|
|   Mouse Left Click	|   Add Node or obstacle	|

> Maze Generation:

|   Key	|   Function	|
|---	|---	|
| p  	|   Prim's algorithm	|
|  k 	|   Kruskal's algorithm	|
|   s	|   Sidewinder algorithm	|
|  r 	|   Recursive backtracking algorithm	|
|  u 	|   Aldous Broder algorithm	|
|  h 	|   Hunt and Kill algorithm	|
|   g	|   Growing Tree algorithm	|
|   b	|   Binary Tree algorithm	|
|   q	|   Recursive Division algorithm	|
|  w 	|  	 Wilson's algorithm|
|  e 	|  	 Eller's algorithm|

> Path Finding:

|   Key	|   Function	|
|---	|---	|
| a  	|   A* algorithm	|
| d  	|   Dijkstra algorithm	|
|   	|  	|

> Sorting:

|   Key	|   Function	|
|---	|---	|
|   Space	| Shuffle 	|
|  1 	|  Bead Sort	|
|  2 	|  Bitonic Sort	|
|  3 	|  Bolo Sort	|
| 4  	|   Bubble Sort	|
| 5  	|   Bucket Sort	|
| 6  	|   Cocktail Shaker Sort	|
| 7  	|   Comb Sort	|
| 8  	|   Counting Sort	|
| 9  	|   Cycle Sort	|
| 0  	|   Double Sort	|
| q  	|   Gnome Sort	|
| w  	|   Heap Sort	|
| e  	|   Insertion Sort	|
| r  	|  Merge Insertion Sort (iterative)	|
| t  	|  Merge Sort (Recursive)	|
| y  	|  Merge Sort (iterative)	|
| u  	|   Odd Even Sort	|
|  i 	|  Pancake Sort	|
|  h 	|  Selection Sort	|
|   j	|  	Wiggle Sort|
|   	|  	|

#### Note:
1) Maze algorithms don't work if start and end nodes are mentioned already.
2) Path finding algorithms work only if start and end nodes are mentioned.
3) Sort algorithms work only when lines are shuffled 