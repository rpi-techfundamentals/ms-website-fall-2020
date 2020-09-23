# Computational Solutions 
## Introduction to Linear Programming

Computational environments provide organizations with the ability to implement solutions to complex time, in real time.  

[Scikit Learn, Pulp, CPLEX, and Gurobi](https://medium.com/opex-analytics/optimization-modeling-in-python-pulp-gurobi-and-cplex-83a62129807a) are  Python packages which provide capabilities for Linear programming and optimization. 


!pip install pulp

#Import some required packages. 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

## Product mix problem - Farmers Fields

Problem: How much of each brand to purchase to minimize total cost of fertilizer given following data?

Product resource requirements and unit profit:

Two brands of fertilizer available – Super-gro, Crop-quick.

Field requires at least 16 pounds of nitrogen and 24 pounds of phosphate.

Super-gro costs: `$6 per bag` 

Crop-quick: `$3 per bag`


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


#Initialize the model as a minimization problem. 
import pulp as pl
opt_model = pl.LpProblem("MIPModel", pl.LpMinimize)


#Set the variables. Notice this is where we put 
# the "non-negativity" constraint
x1 =pl.LpVariable(cat=pl.LpInteger, lowBound=0, name="$x_{1}$") 
x2 =pl.LpVariable(cat=pl.LpInteger, lowBound=0, name="$x_{2}$") 

#Set the objective function
opt_model += 6 * x1 + 3 * x2 

#Set the Constraints
opt_model += 2 * x1  + 4* x2  >= 16

opt_model += 4 * x1 + 3 * x2 >= 24

## Review Model

Now that we have created the model we can review it. 

opt_model

## Markdown of output
If we copy the above text into a markdown cell you will see the implications of the varous models. 


MIPModel:

MINIMIZE

6*$x_{1}$ + 3*$x_{2}$ + 0

SUBJECT TO

_C1: 2 $x_{1}$ + 4 $x_{2}$ >= 16

_C2: 4 $x_{1}$ + 3 $x_{2}$ >= 24

VARIABLES

0 <= $x_{1}$ Integer

0 <= $x_{2}$ Integer


## Solve

We now solve the system of equations with the solve command. 

#Solve the program
opt_model.solve()


## Check the Status

Here are 5 status codes:
* **Not Solved**: Status prior to solving the problem.
* **Optimal**: An optimal solution has been found.
* **Infeasible**: There are no feasible solutions (e.g. if you set the constraints x <= 1 and x >=2).
* **Unbounded**: The constraints are not bounded, maximising the solution will tend towards infinity (e.g. if the only constraint was x >= 3).
* **Undefined**: The optimal solution may exist but may not have been found.

pl.LpStatus[opt_model.status]

for variable in opt_model.variables():
    print(variable.name," = ", variable.varValue)

## Hurray! 
We got the same answer as we did before. 

## Exercise

Solve the LP problem for Beaver Creek Pottery using the maximization model type (`pl.LpMaximize`).


### Product mix problem - Beaver Creek Pottery Company
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



## Sensitivity Analysis

for name, c in opt_model.constraints.items():
    print (name, ":", c, "\t", c.pi, "\t\t", c.slack)

