# Tic-Tac-Toe
Minimax implementation to play the classic game of tic-tac-toe.
___
### Introduction

Tic-tac-toe is a zero-sum and perfect information game, giving it some notable properties that we can exploit while designing the algorithm.

**Definition 1.1**​ ​- A zero-sum game is a mathematical expression of a game state in which the gain and loss of utility of one player is the same as another player. Total gains minus total loss is always 0.

**Definition 1.2**​ ​- A perfect information game is defined to be sequential game where players are perfectly informed of precedent events and, of course, the initialization event. On the contrary, an example of an imperfect game would be poker, where players are unaware of others’ cards.

Seeing that this game is a two-player turn based game with the aforementioned properties, it’s the perfect opportunity to use a popular game theory algorithm called, MiniMax. This is a recursive algorithm, which is used to determine the optimal move. It considers every subsequent game state until it reaches a terminal state and tries to minimize the maximum loss, hence the name MiniMax. Having established the algorithm we will use, let’s explore the inner-workings of it.
___
### MiniMax application on Tic-Tac-Toe

Consider the following board state, we’ll attempt to solve it as O.
How would we solve this (​Figure 1​)? There’s a clear winning move. Put O in the middle! But, is this the only way for O to emerge victorious, or can we win in a different way? 

<img style = "text-align: center" src="/assets/fig1.png" alt="Figure 1: Made with Adobe Illustrator" width="100" height="100"/>

To answer that question, let’s consider a diagram that encompasses every subsequent game state, and the turnout of each move. Let’s analyze the following tree.

<img style = "text-align: center" src="/assets/fig2.png" alt="Figure 2: Made with Adobe Illustrator" width="625" height="454"/>
   
Our current game state is (​1.0​), from here, we have 3 places we can put our O. One of them, namely (​2.1​), will yield an immediate victory, and the other 2 will prolong the game giving the opponent a chance to make another move. In two of the cases (​3.2​,​ 3.3​), we would lose, but in cases (​3.1​,​ 3.4​), we would win.
Let’s simplify the tree and only consider the terminal states so we can easily backpropagate through the tree. Consider the following tree.

<img style = "text-align: center" src="/assets/fig3.png" alt="Figure 3: Made with Adobe Illustrator" width="245" height="155"/>

We can interpret *Figure 3* as follows,
Start with the bottom tier of terminal events. In this tier, we want to maximize, so we’ll send the ​+1​ to the tier above, so node ​C​ becomes ​+1​.​ N​ ow we can proceed to analyze the middle tier. Here, we want to minimize, so we’ll propagate the ​-1​ t​ o ​A​ and ​B​. In the top tier, we want to maximize, so we’ll send ​+1 ​to the head tier, denoted by ​H​, where we will be advised to pick the move associated with the ​+1​.
Hence, the algorithm will choose the move that we initially contemplated proceeding with! Our algorithm will perpetually perform similar analyses at every game state, ensuring the best for the computer. Thus, the algorithm will be unbeatable, the best a user can do is lead the game to a draw.
___
### Sidenote
Because the possible game states is relatively small, 3 <sup>6</sup> = 196839 , the computer can easily iterate through every possibility and choose the optimal move. On the contrary, if we were playing a game like chess, this approach may not be the most efficient because the number of game states would be greater than the number of atoms in the observable universe!
