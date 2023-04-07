To change the odds of you picking the goal as your alpha_i, you can edit this in the rrt method of the planning.py file.
The variable you want to change is pG.

Problem 2
1. "and the configuration space obstacle"
This wording seems a bit odd.  In lecture 9, on slide 3, we formally define C_obs.
It is the set of all configurations, q, at which A(q) intersects O,
where O is the obstacle region, which is a subset of the world,
and A is a rigid robot, which is a subset of the world.
Also A and O are semi-algebraic models.
The way it is worded in the problem statement seems incomplete and inaccurate.

2. "attempts to find a feasible path Tau : [q_I, q_G] ^ T, ..."
This seems wrong to me.  In lecture 7, a path should be a continuous function
Tau : [0, 1] -> X where X is a topological space.  Each point along the path
is given by Tau(s) for some s which is an element of the set [0,1].
Tau is a function.  I'm not sure what they mean by Tau:[q_I, q_G] ^ T

3. "If such a feasible path does not exist, a motion planning algorithm should return failure"
I'm not sure this is absolutely possible.  How can you check all the points in a
continuous space?  Aren't they uncountable infinite?  Wouldn't you want to return
failure if the algorithm runs for a certain number of iterations and can't find a path?
Seems like it would be impossible for an algorithm to definitively say a path absolutely
does not exist.  Maybe for a certain configuration space and obstacles it would take
1,000 iterations.  Maybe for another it would take 100,000,000,000 iterations.
While an algorithm might be able to tell you in a finite amount of time or iterations
that a path does exist, I'm not sure there is an algorithm that can run for a set
number of iterations in a finite amount of time that could definitively say
that a feasible path certainly doesn't exist.