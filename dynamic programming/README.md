# Dynamic Programming

* [Edit Distance]
	* Given two strings x and y, find the minimum number of edits needed to transform x into y
	* Runtime O(n^2)
* [Largest Sum](largest_sum.py)
	* Given an array of n integers, find the consecutive indices that give the largest sum.
	* Runtime:
* [Least Amount of Jumps](least_jumps.py)
	* Given an array of non-negative integers, starting at the 0th index, land on the last index of the array. Each element reps the max number of steps you can take from that element.
	* Runtime O(n^2); there are O(n) solutions out there
* [Longest Increasing Subsequence LIS](longest_increasing_subsequence.py)
	* Given an array of integers, return the longest increasing subsequence.
	* Dynamic programming: turns the problem into a DAG. Runtime O(n^2)
* [Trapping Rain Water](trap_rain_water.py)
	* Given an array of non-neg integers that rep the height of a bar in a histogram, find how many units of water you can trap in the histogram.
	* Runtime 

* Notes
	* Define the subproblem; there's an ordering to the subproblems and a (recurrence) relation that shows how to solve the subproblems such that each subproblem only relies on the solution to the smaller ones before it.
	* Define the base case