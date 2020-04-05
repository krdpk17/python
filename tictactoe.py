
class tictactoe:
	def __init__(self):
		row1=[' ',' ',' ']
		row2=[' ',' ',' ']
		row3=[' ',' ',' ']
		self.board=[row1, row2, row3]
	def mov(self,row, col, alpha):
		self.board[row][col]=alpha
	def print_board(self):
		for row in self.board:
			print(row)
t=tictactoe()
while True:
    t.print_board()
    row = int(input("row:"))
    col = int(input("col:"))
    t.mov(row-1,col-1, 'X')
    t.print_board()
    row = int(input("row:"))
    col = int(input("col:"))
    t.mov(row-1,col-1, 'O')
