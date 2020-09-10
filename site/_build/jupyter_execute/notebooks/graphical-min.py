# Graphical Solutions 
## Introduction to Linear Programming

#Import some required packages. 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

Graphical solution is limited to linear programming models containing only two decision variables (can be used with three variables but only with great difficulty).

Graphical methods provide a picture of how a solution for a linear programming problem is obtained.


## Product mix problem - Farmers Fields
Problem: How much of each brand to purchase to minimize total cost of fertilizer given following data ?

Product resource requirements and unit profit:
Two brands of fertilizer available – Super-gro, Crop-quick.
Field requires at least 16 pounds of nitrogen and 24 pounds of phosphate.
Super-gro costs $6 per bag, Crop-quick $3 per bag.


Decision Variables:

$x_{1}$ = number of bags of Super-gro

$x_{2}$ = number of bags of Crop-quick


Cost (Z) minimization 

Z = 6$x_{1}$ + 3$x_{2}$


Nitrogen Constraint

2$x_{1}$ + 4$x_{2}$ >= 16

Phosphate Constraint Check

4$x_{1}$ + 3$x_{2}$ >= 24

Non-negativitiy Constraint

$x_{1}$ > 0

$x_{2}$ > 0



#Create an Array X2 from 0 to 60, and it should have a length of 61.
x2 = np.linspace(0, 14, 15) 

#This is the same as starting your Excel Spreadsheet with incrementing X2
x2

#Nitrogen Constraint
# 2x1  + 4x2  >= 16
# x1= 8-2x2
c1 =  8 - 2*x2
c1

#Clay (Physicial Resource) Constraint Check
#4x1 + 3x2 <= 120
#4x1  + 3 x2  >= 24
c2  = (24 - 3*x2)/4
c2

#Calculate the maximim value of X1 you can make per the 2 different constraints.

ct = np.maximum(c1,c2)
ct

ct=ct[0:9] #removes negative values
ct

#Calculate the minimum cost from ct
#Z = 6 x1  + 3 x2
cost = 6*ct+3*x2[0:9]#Shape of array must be the same.
cost

# Make plot for the Nitrogen Constraint

plt.plot(c1, x2, label=r'2$x_{1}$ + 4$x_{2}$ >= 16')
plt.xlim((0, 14))
plt.ylim((0, 14))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.fill_between(x2,c1, color='grey', alpha=0.5)


#Graph Phosphate Constraint Check


plt.plot(c2, x2, label=r'4$x_{1}$ + 3$x_{2}$ >= 24')
plt.xlim((0, 14))
plt.ylim((0, 14))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.fill_between(c2, x2, color='grey', alpha=0.5)

# Make plot for the combined constraints.
plt.plot(c1, x2, label=r'2$x_{1}$ + 4$x_{2}$ >= 16')
plt.plot(c2, x2, label=r'4$x_{1}$ + 3$x_{2}$ >= 24')
#plt.plot(ct, x2, label=r'min(x$x_{1}$)')
plt.xlim((0, 14))
plt.ylim((0, 14))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.fill_between(ct, x2,  color='grey', alpha=0.5)

Our solution must be in in lies somewhere in the grey feasible region in the graph above. However, according to the fundamental theorum of Linear programming we know it is at a vertex. 

"In mathematical optimization, the fundamental theorem of linear programming states, in a weak formulation, that the maxima and minima of a linear function over a convex polygonal region occur at the region's corners. Further, if an extreme value occurs at two corners, then it must also occur everywhere on the line segment between them."

- [Wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_programming)

#This returns the index position of the maximum value
min_value = np.argmin(cost)
min_value

#Calculate The min cost that is made. 
profit_answer=cost[min_value]
profit_answer

# Verify all constraints are integers
x2_answer = x2[min_value]
x2_answer

# Verify all constraints are integers
ct_answer = ct[min_value]
ct_answer

