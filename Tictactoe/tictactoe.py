from itertools import combinations
class Tictactoe(object):

    def __init__(self):
        self.p1_won = False
        self.p2_won = False
        self.board_not_full = True
        self.board = ['_' for x in range(9)]
        self.counter = 0

    def print_board(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])

    def is_valid_input(self, x):
        try:
            x = int(x)
            return True
        except Exception:
            return False

    def argument_in_range(self, x):
        x = int(x)
        if x < 1 or x > 9:
            print('Not in Range, please choose a number between 1 and 9')
            return False
        else:
            return True

    def not_already_taken(self, x):
        if self.board[int(x)-1] == '_':
            return True
        else:
            print('Spot already taken, go again please')
            return False

    def set_mark(self, x):
        if self.is_valid_input(x) and self.argument_in_range(x) and self.not_already_taken(x):
            if self.counter%2 == 0:
                self.board[int(x)-1] = 'x'
            else:
                self.board[int(x)-1] = 'o'
            self.counter += 1
        else:
            print('Invalid input')

    def choose_winner(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        ix = [i for i, x in enumerate(self.board) if x == "x"]
        io = [i for i, x in enumerate(self.board) if x == "o"]
        if len(ix) < 3 and len(io) < 3:
            return 0
        else:
            for c in combinations(ix, 3):
                if list(c) in winning_combinations:
                    self.p1_won = True
                else:
                    for d in combinations(io, 3):
                        if list(d) in winning_combinations:
                            self.p2_won = True


    def start(self):
        print("Welcome")
        self.print_board()
        while self.board_not_full and not self.p1_won and not self.p2_won:
            i = input('Player {}, please input the position for your next mark [1-9]:'
                      .format(self.counter % 2 + 1))
            self.set_mark(i)
            self.print_board()
            self.choose_winner()
            self.board_not_full = not self.counter == 9
        if self.p1_won:
            print('congratulations p1 you won!')
        elif self.p2_won:
            print('congratulations p2 you won!')
        else:
            print('What a pitty, a draw')

app = Tictactoe()
app.start()
