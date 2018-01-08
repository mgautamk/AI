#include<stdio.h>
#include<stdlib.h>
#define N 8

void printSolution(int board[N][N])
{
  int i,j;
  for(i=0;i<N;i++) {
    for(j=0;j<N;j++)
      printf("%d ",board[i][j]);
    printf("\n");    }

}
int isSafe(int row,int col,int board[N][N])
{
  //check for all column in this row (since this is first one placing in this column
  int i,j;
  for(i=0;i<col;i++){
    if(board[row][i])
      return 0;        }

  //check for upper diagonal
  for(i=row,j=col;i>=0&&j>=0;i--,j--)
    {if(board[i][j])
	return 0;
    }
  //check for lower diagonal
  for(i=row,j=col;i<N&&j>=0;i++,j--)
    {if(board[i][j])
	return 0;    }

  return 1;
}
int solveNQUtil(int board[N][N], int col)
{
  
  int k;
  if(col>=N)
    return 1;

  for(k=0;k<N;k++)
    {
      if(isSafe(k,col,board))
	{
	  board[k][col]=1;

	  if(solveNQUtil(board,col+1))
	    return 1;

	  board[k][col]=0;
	}
    }
  return 0;
}

void solveNQ()
{
  int board[N][N] = { {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0},
		      {0, 0, 0, 0, 0, 0, 0, 0}
  };

  if ( !solveNQUtil(board, 0)  )
    {
      printf("Solution does not exist");
      return;
    }

  printSolution(board);
}

// driver program to test above function
int main()
{
  solveNQ();
  return 0;
}
