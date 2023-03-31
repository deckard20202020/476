To run the program you simply have to run hw4.py.  There are no arguments as I have no completed the extra credit.
When you run hw.4, all three methods, exploration without collision, exploration with collision, and path finding will be run.
Results of all three will be displayed.
If you would like one not to run, you can simply comment the call to that method in main.
The first two methods (exploration without collision and exploration with collision) take a little longer to run that I would like.
Both should easily complete in under 30-60 seconds.
As we often find a path fairly quickly in the path finding method, this often completes much quicker.
From time to time a path is not found during the path finding method.  In this case, the resulting exploration tree will be printed out, but there will be no path.
This is pretty rare, but depends on the number of iterations you run, and the size of dt.

The parameters for the program can be found in the main function at the bottom of hw4.py.
They are pretty self explanatory.
The radius of the circles will be 1 - dt.
The step size is used for object detection.

For both exploration and path finding, the algorithm runs for 100 iterations.
This can be changed in planning.py in the appropriate method, depending on whether you are running exploration without collision detection, exploration with collision detection, or path finding.
Note that 10% of the time, our goal will be selected as our random point ai.  This occurs in all three methods, and will result in less than 100 random points being chosen.
There is also the change that a random point can be chosen more than once.
Currently, random points are chosen with a precision of one decimal place.  For example (2.5, 1.2).
If you would like to increase the precision this can be done by altering the getRandomPoint() method in planning.py

Let me know if you have any issues or questions.
