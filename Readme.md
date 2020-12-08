In this project i tried to develop markov sentence generator thorugh my understanding

First i needed the data to build a probability list for the words in my generator.
I am trying to scrape the data from the wikipedia plot section since they are more coherent and will form our system to be a
story type markov generator giving us a realistic look. Although this system will be a very naive language generator 

The movies plot which i would scrape are

Avengers Endgame
Avengers
Shawshank Redemption
Good Will hunting
Sherlock holmes
Knives out

The most important decision is to choose the datastructure for the same
We will try to build a dictionary of each word which in turn will consist of a dictionary that will store the frequency of the words. Each word frequency/total words frequency will give us the probability of that word to come next to the current word 
This way we will move from one state to the next
Although i expected this to not be that good but this is worse than except. I will try to brainstrom other ideas of improving this at this moment this generator is very naive and unusable.

How to run

Load your data in the input.txt the more the data resemble real world the better
Run the markov.py 
