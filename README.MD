# Flocking implemented in Python
This is a rudimentary implementation of the flocking algorithm, by
[Craig Reynolds](https://www.red3d.com/cwr/boids/ "Craig Reynold's boids").
More explanation on how flocking works can be found at the link.

This was written as a way for testing a vector class I wrote and to see if
everything with the vectors is working as expected. I wrote this in a single
evening, with a few changes the day after.

The vector class will be released at a later time, as it is part of a module I
am currently writing.

The boids sort of act like they should, but not completely. This most likely
due to incorrect tuning of the parameters. I might come back to this later and
rewrite this.

Due to some limitations and performance issues with pygame, the boids is
limited to somewhere around 80 - 120 boids.

Feel free to make changes and optimize the program, and let me know if you
 find issues or bugs in the code.