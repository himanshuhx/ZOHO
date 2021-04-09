Given:
 matrix N*N
 x, y = 2,2
 initialize a cnt variable with 0
 algorithm:
  we implement a recursive function solve()
  as knight can move up down left right from its pos
  we do a dfs traversal from the knight's index and
  whenever we hit an index with curr ele==1 we increment the count
  base case ==> to check the boundaries of our matrix
  i.e if we are outside i<0 and j<0 or i>N-1 and j>n-1
  by keeping this boundary check we can solve the problem
