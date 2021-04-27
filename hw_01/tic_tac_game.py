class TicTacGame:

    class Winner:
        NO = ''
        PLAYER_1 = 'X'
        PLAYER_2 = 'O'
        DRAW = 'DRAW'

    def init_board(self, n=3):
        self.board = [[' '] * n for i in range(n)]
        self.board_size = n

    def init_game(self, n=3):
        self.init_board(n)
        self.player = self.Winner.PLAYER_1

    def show_board(self):
        print('-' * (self.board_size * 2 + 1))
        for row in self.board:
            print('', *row, sep='|', end='|\n')
            print('-' * (self.board_size * 2 + 1))

    def validate_input(self, coords):
        try:
            x, y = list(map(int, coords.split()))
            x -= 1
            y -= 1
            if self.board[y][x] != ' ':
                print('This cell is already occupied')
                return False
        except ValueError:
            print('X and Y must be two integers')
            return False
        except IndexError:
            print(f'X and Y must be from 1 to {self.board_size}')
            return False
        return (x, y)

    def safe_input_move(self):
        print(f'Current player {self.player}')
        coords = input('Enter x, y coords: ')

        data = self.validate_input(coords)

        while not data:
            coords = input('Enter x, y coords: ')
            data = self.validate_input(coords)

        return data[0], data[1]

    def make_move(self, x, y):
        self.board[y][x] = self.player
        self.switch_player()

    def switch_player(self):
        self.player = self.Winner.PLAYER_1 if self.player == \
            self.Winner.PLAYER_2 else self.Winner.PLAYER_2

    def start_game(self, n=3):
        self.init_game(n)
        winner = self.Winner.NO
        move_count = 0

        while not winner:
            x, y = self.safe_input_move()
            move_count += 1

            self.make_move(x, y)
            self.show_board()

            winner = self.check_winner(x, y) if move_count < \
                self.board_size * self.board_size else self.Winner.DRAW

        if winner == 'DRAW':
            print("It is draw")
        else:
            print(f'Winner is player {winner}')

    def check_winner(self, x, y):
        for i in range(x - 2, x + 1):
            for j in range(y - 2, y + 1):
                if i < 0 or j < 0:
                    continue
                try:
                    if self.board[j][i] == self.board[j][i + 1] and \
                       self.board[j][i + 1] == self.board[j][i + 2] and \
                       self.board[j][i] != ' ':
                        return self.board[j][i]
                except IndexError:
                    pass
                try:
                    if self.board[j][i] == self.board[j + 1][i] and \
                       self.board[j + 1][i] == self.board[j + 2][i] and \
                       self.board[j][i] != ' ':
                        return self.board[j][i]
                except IndexError:
                    pass
                try:
                    if self.board[j][i] == self.board[j + 1][i + 1] and \
                       self.board[j + 1][i + 1] == self.board[j + 2][i + 2] \
                       and self.board[j][i] != ' ':
                        return self.board[j][i]
                except IndexError:
                    pass
        return self.Winner.NO


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
