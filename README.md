# Algorithm Visualiser

A simple tool built step by step visualisation for path finding, maze creating and sorting algorithms 

![Example](Fonts/Example.png "Example")

### Included algorithms:

Path Finding:
1) [A* Path finding algorithm](Algorithms/astar.py)
1) [Dijkstra algorithm](Algorithms/dijkstra.py)

Maze:
1) [Prim's algorithm](Algorithms/prims.py)
1) [Kruskal's algorithm](Algorithms/kruskal.py)
1) [Sidewinder algorithm](Algorithms/sidewinder.py)
1) [Eller's algorithm](Algorithms/ellers.py)
1) [Recursive backtracking algorithm](Algorithms/recursive_backtracking.py)
1) [Aldous Broder algorithm (Modified)](Algorithms/aldous_broder.py)
1) [Wilson's algorithm](Algorithms/wilson.py)
1) [Hunt and Kill algorithm](Algorithms/hunt_and_kill.py) (Modified)
1) [Growing Tree algorithm](Algorithms/growing_tree.py) (newest and random choices combined)
1) [Binary Tree algorithm](Algorithms/binary_tree.py)
1) [Recursive division algorithm](Algorithms/recursive_division.py)

Sorting:
1) [Bead / Gravity Sort](Sorts/bead.py)
1) [Bitonic Sort](Sorts/bitonic.py)
1) [Bogo / Stupid Sort](Sorts/Bogo.py)
1) [Bubble Sort](Sorts/bubble.py)
1) [Bucket / Bin Sort](Sorts/bucket.py)
1) [Cocktail Shaker / Bidirectional Bubble / Ripple / Shuttle Sort](Sorts/cocktail.py)
1) [Comb Sort](Sorts/comb.py)
1) [Counting Sort](Sorts/counting.py)
1) [Cycle Sort](Sorts/cycle.py)
1) [Double Sort](Sorts/double.py)
1) [Gnome / Dubbed Stupid Sort](Sorts/gnome.py)
1) [Heap Sort](Sorts/heap.py)
1) [Insertion Sort](Sorts/insertion.py)
1) [Merge Sort](Sorts/iterativemerge.py) (Iterative method)
1) [Merge Sort](Sorts/recursivemerge.py) (Recursive method)
1) [Odd Even / Brick Sort](Sorts/oddeven.py)
1) [Pancake Sort](Sorts/pancake.py)
1) [Pigeonhole Sort](Sorts/pigeon.py)
1) [Quick Sort](Sorts/quick.py)
1) [Radix Sort](Sorts/radix.py)
1) [Shell Sort](Sorts/shell.py)
1) [Selection Sort](Sorts/selection.py)
1) [Sleep Sort](Sorts/sleepsort.py)
1) [Wiggle Sort](Sorts/wiggle.py)

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
|  o 	|  Pigeonhole Sort	|
|  p 	|  Quick Sort	|
|  a 	|  Radix Sort	|
|  s 	|  Selection Sort	|
|  d 	|  Shell Sort	|
|  f 	|  Sleep Sort	|
|   j	|  	Wiggle Sort|
|   	|  	|

#### Note:
1) Maze algorithms don't work if start and end nodes are mentioned already.
2) Path finding algorithms work only if start and end nodes are mentioned.
3) Sort algorithms work only when lines are shuffled 