# Beam Search in AI

## Description :
**Similar to greedy search. However, initializing from one start state, search in solution space, keeping the BeamK best current solution under the current step.     
Iteration, until meeting the end state .** 

## Hypeparameters:
1. BeamK ---  the number of Beam



## What happen in Search Algorithm 
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

## Where to use
For all of peoblem which need to do search tasks in the solution space

For example: 
[Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%2Farxiv.org%2Fpdf%2F1609.08144.pdf%2520(7.pdf&clen=1688289&chunk=true)

