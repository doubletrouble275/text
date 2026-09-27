from src.board import Board
from src.player import HumanPlayer, ComputerPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer("Игрок", "X")
        self.computer = ComputerPlayer("Компьютер", "O")
        self.current_player = self.human

    def switch_player(self):
        self.current_player = (
            self.computer if self.current_player == self.human else self.human
        )

    def run(self):
        print("=== Крестики-нолики: Человек vs Компьютер ===")
        print("Ты играешь за X, компьютер за O")
        print("Позиции клеток:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 \n")

        while True:
            self.board.display()

            if self.current_player == self.human:
                move = self.current_player.make_move(self.board)
            else:
                print("Компьютер думает...")
                move = self.current_player.make_move(self.board)
                print(f"Компьютер походил на клетку {move + 1}")

            self.board.make_move(move, self.current_player.symbol)

            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                if self.current_player == self.human:
                    print("🎉 Ты победил!")
                else:
                    print("💻 Компьютер победил!")
                break

            if self.board.is_full():
                self.board.display()
                print("🤝 Ничья!")
                break

            self.switch_player()

        again = input("\nСыграть ещё раз? (да/нет): ").lower()
        if again in ["да", "д", "yes", "y"]:
            self.__init__()  # сброс игры
            self.run()
        else:
            print("Спасибо за игру!")