# Beam Search in AI

## Description :
**Similar to greedy search. However, initializing from one start state, search in solution space, keeping the BeamK best current solution under the current step.     
Iteration, until meeting the end state .** 

## Hypeparameters:
1. BeamK ---  the number of Beam


> Input
1. Solution space
2. BeamK
3. initial state

> Process
1. Keep searching in the solution space
2. update `K` best solutions after step

> Output
1. Get a solution set (containing `K` best solutions)
2. Ruturn the best one in the solution set

