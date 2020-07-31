# Algorithm Visualiser

A simple tool built step by step visualisation for path finding, maze creating and sorting algorithms. 

Over 35 algorithms visualised step by step! 

---

> Maze and Path Finding

![Example](Fonts/Example1.png "Maze and Path Finding")

>Sorting

![Example](Fonts/Example2.png "Sorting")

---

## Supported Algorithms:

>Path Finding:
1) [A* Path finding algorithm](Algorithms/astar.py)
1) [Dijkstra algorithm](Algorithms/dijkstra.py)

>Maze:
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

>Sorting:
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
1) [Merge Sort](Sorts/iterativemerge.py)
1) [Odd Even / Brick Sort](Sorts/oddeven.py)
1) [Pancake Sort](Sorts/pancake.py)
1) [Pigeonhole Sort](Sorts/pigeon.py)
1) [Quick Sort](Sorts/quick.py)
1) [Radix Sort](Sorts/radix.py)
1) [Shell Sort](Sorts/shell.py)
1) [Selection Sort](Sorts/selection.py)
1) [Sleep Sort](Sorts/sleep.py)
1) [Stooge Sort](Sorts/stooge.py)
1) [Wiggle Sort](Sorts/wiggle.py)

---
## To run the application:

Install modules
```bash
pip install pygame
```

Run to get started right away!:
```bash
python app.py
```

---
## To use the tool:
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
| Backspace  	|  Clear Screen (Maze)\Increase execution Speed (Both) 	|
|   Tab	|  Switch off or on grid (Both) 	|
|   Mouse Right Click	|   Clear node or obstacle (Maze)	|
|   Mouse Left Click	|   Add Node or obstacle (Maze)	|
|   Space	|  Shuffle (Sort)	|
|   R_Shift	| Invert (Sort) 	|
|   Escape	|  Return to previous page	|
|   h	|  Help	|

> Maze Generation:

|   Key	|   Function	|
|---	|---	|
| 1  	|   Prim's algorithm	|
|  2 	|   Kruskal's algorithm	|
|  3	|   Sidewinder algorithm	|
|  4 	|   Recursive backtracking algorithm	|
|  5 	|   Aldous Broder algorithm	|
|  6 	|   Hunt and Kill algorithm	|
|   7	|   Growing Tree algorithm	|
|   8	|   Binary Tree algorithm	|
|   9	|   Recursive Division algorithm	|
|  0	|  	 Wilson's algorithm|
|  q 	|  	 Eller's algorithm|

> Path Finding:

|   Key	|   Function	|
|---	|---	|
| z  	|   A* algorithm	|
| x  	|   Dijkstra algorithm	|
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
| r  	|  Merge Sort	|
| t  	|   Odd Even Sort	|
|  y 	|  Pancake Sort	|
|  u 	|  Pigeonhole Sort	|
|  i 	|  Quick Sort	|
|  o 	|  Radix Sort	|
|  p 	|  Selection Sort	|
|  a 	|  Shell Sort	|
|  s 	|  Sleep Sort	|
|  d 	|  Stooge Sort	|
|   f	|  	Wiggle Sort|

#### Note:
1) Maze algorithms don't work if start and end nodes are mentioned already.
2) Path finding algorithms work only if start and end nodes are mentioned.
3) Sort algorithms work only when lines are shuffled 