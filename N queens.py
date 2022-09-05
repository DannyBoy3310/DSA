class NQueens:
    def __init__(self,n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]

    def solve_n_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("No solution")

    def solve(self,col_index):
        #base case
        if col_index==self.n:
            return True
        for row_index in range(self.n):
            if self.place_valid(row_index,col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True

                print("BACKTRACKING....")
                self.chess_table[row_index][col_index] = 0
        return False
    def place_valid(self, row_index, col_index):
        #check horizontally
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False
        #check diagnally
        j = col_index
        for i in range(row_index,-1,-1):
            if i < 0:
                break
            if self.chess_table[i][j]==1:
                return False
            j = j - 1

        j = col_index
        for i in range(row_index,self.n):
            if j < 0:
                break
            if self.chess_table[i][j]==1:
                return False
            j = j - 1

        return True
    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j]==1:
                    print("Q",end="   ")
                else:
                    print("-",end="   ")
            print("\n")

if __name__ == "__main__":
    queens = NQueens(6)
    queens.solve_n_queens()
