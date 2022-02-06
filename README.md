# Beam Search in AI

## Description :
**Similar to greedy search. However, initializing from one start state, search in solution space, keeping the BeamK best current solution under the current step.     
Iteration, until meeting the end state .**    

In this task, I use Beam Search to generate sentence, and develop 2 different versions of Beam-Search to generate sentence:  
1. normal one
2. Beam search with `normalization` of `sentence length`

## Hypeparameters:
1. BeamK ---  the number of Beam





## What happen in Search Algorithm 
> **Input**
1. Solution space
2. BeamK
3. initial state

> **Process**
1. Keep searching in the solution space
2. update `K` best solutions after step

> **Output**
1. Get a solution set (containing `K` best solutions)
2. Ruturn the best one in the solution set

## Where to use
For all of peoblem which need to do search tasks in the solution space

For example:  
1. [Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](https://arxiv.org/pdf/1609.08144.pdf (7.pdf)) 
2. [Single-Queue Decoding for Neural Machine Translation](https://arxiv.org/pdf/1707.01830.pdf![image](https://user-images.githubusercontent.com/39432361/152667989-496df029-43a7-49ce-b9b5-61d600887121.png)
)

