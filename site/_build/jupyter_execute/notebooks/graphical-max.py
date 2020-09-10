# Graphical Solutions 
## Introduction to Linear Programming

#Import some required packages. 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

Graphical solution is limited to linear programming models containing only two decision variables (can be used with three variables but only with great difficulty).

Graphical methods provide a picture of how a solution for a linear programming problem is obtained.


## Product mix problem - Beaver Creek Pottery Company
How many bowls and mugs should be produced to maximize profits given labor and materials constraints?

Product resource requirements and unit profit:

Decision Variables:

$x_{1}$ = number of bowls to produce per day

$x_{2}$ = number of mugs to produce per day


Profit (Z)  Mazimization

Z = 40$x_{1}$ + 50$x_{2}$

Labor Constraint Check

1$x_{1}$ + 2$x_{2}$ <= 40

Clay (Physicial Resource) Constraint Check

4$x_{1}$ + 3$x_{2}$ <= 120

Negative Production Constaint Check

$x_{1}$ > 0

$x_{2}$ > 0



#Create an Array X2 from 0 to 60, and it should have a length of 61.
x2 = np.linspace(0, 60, 61) 

#This is the same as starting your Excel Spreadsheet with incrementing X2
x2

#Labor Constraint Check
# 1x1 + 2x2 <= 40
#x1 = 40 - 2*x2
c1 =  40 - 2*x2
c1

#Clay (Physicial Resource) Constraint Check
#4x1 + 3x2 <= 120
#x1 = (120 - 3*x2)/4
c2  = (120 - 3*x2)/4
c2

#Calculate the minimum of X1 you can make per the 2 different constraints.
ct = np.minimum(c1,c2)
ct

#remove those valuese that don't follow non-negativity constraint.
ct= ct[0:21]
x2= x2[0:21] #Shape of array must be the same.
ct

#Calculate the profit from the constrained 
profit = 40*ct+50*x2 
profit

# Make plot for the labor constraint
plt.plot(c1, x2, label=r'1$x_{1}$ + 2$x_{2}$ <= 40')
plt.xlim((0, 60))
plt.ylim((0, 60))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.fill_between(c1, x2, color='grey', alpha=0.5)


#Graph Resource Constraint
plt.plot(c2, x2, label=r'4$x_{1}$ + 3$x_{2}$ <= 120')
plt.xlim((0, 60))
plt.ylim((0, 60))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.fill_between(c2, x2, color='grey', alpha=0.5)

# Make plot for the combined constraints.
plt.plot(c1, x2, label=r'1$x_{1}$ + 2$x_{2}$ <= 40')
plt.plot(c2, x2, label=r'4$x_{1}$ + 3$x_{2}$ <= 120')
#plt.plot(ct, x2, label=r'min(x$x_{1}$)')
plt.xlim((0, 60))
plt.ylim((0, 60))
plt.xlabel(r'$x_{1}$') #Latex way of writing X subscript 1 (See Markdown)
plt.ylabel(r'$x_{2}$') #Latex way of writing X subscript 1 (See Markdown)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.fill_between(ct, x2,  color='grey', alpha=0.5)

Our solution must be in in lies somewhere in the grey feasible region in the graph above. However, according to the fundamental theorum of Linear programming we know it is at a vertex. 

"In mathematical optimization, the fundamental theorem of linear programming states, in a weak formulation, that the maxima and minima of a linear function over a convex polygonal region occur at the region's corners. Further, if an extreme value occurs at two corners, then it must also occur everywhere on the line segment between them."

- [Wikipedia](https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_programming)

#This returns the index position of the maximum value
max_value = np.argmax(profit)
max_value

#Calculate The max Profit that is made. 
profit_answer=profit[max_value]
profit_answer

# Verify all constraints are integers
x2_answer = x2[max_value]
x2_answer

# Verify all constraints are integers
ct_answer = ct[max_value]
ct_answer

## Q1 Challenge

What if the profit function is:

Z = 70$x_{1}$ + 20$x_{2}$       

Find the optimal solution using Python. Assign the answers to: 

q1_profit_answer
q1_x1_answer
q1_x2_answer


