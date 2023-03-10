SAVE YOURSELF A LOT OF TIME!!!
I have completed all 3 tasks for the homework.  If you just run task 1 and 2 with the input file provided to us, it taks about 1 or 2 minutes.  If you run task 3 as well, it takes SIGNIFICANTLY longer.  As it is currently set, each step of the path is divided into 10 smaller steps.

You can prevent my program from running task three and commenting everything out below the "# task 3" comment.

For task 3, I just call the method finerCollisionChecking, which returns a list of finer configurations that lie in between the configurations of the path found in task 1 and task 2 that are in collision with an obstacle.  The main method will simply output these to the terminal.
In the method finerCollisionChecking, you can break up each segment into sections as small as you would like, in order to get the precision you desire.  In order to change the precision, simply change the value of the variable "increment" located in that method.
I currently have "increment" set to 0.1, so it will divide each segment of the path into 10 smaller segments.  
