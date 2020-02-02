# Shri's problem.
\
Shriram sent me a problem to solve in python.


2D Array - DS

Given a 6 x 6 2D array, arr:

111000
010000
111000
000000
000000
000000

We define an hourglass in A to be a subset of values with indicies falling in this pattern in arr's graphical representationL

abc
 d 
efg

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maxiumum hourglass sum.

For example. given the 2D array:

-9 -9 -9  1 1 1  
 0 -9  0  4 3 2
-9 -9 -9  1 2 3 
 0  0  8  6 6 0 
 0  0  0 -2 0 0 
 0  0  1  2 4 0

We calculate the following 16 hourglass values:

-63, -34, -9, 12,
-10, 0, 28, 23, 
-27, -11, -2, 10, 
 9, 17, 25, 18

 Our highest hourglass value is 28 from the hourglass:

 0 4 3
   1
 8 6 6 