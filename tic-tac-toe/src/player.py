import random
from abc import ABC, abstractmethod
from src.board import Board

class Player(ABC):
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board: Board) -> int:
        pass


class HumanPlayer(Player):
    def make_move(self, board: Board) -> int:
        while True:
            try:
                move = int(input(f"{self.name}, твой ход (1-9): ")) - 1
                if 0 <= move <= 8 and board.is_empty(move):
                    return move
                print("Неверный ход! Попробуй ещё раз.")
            except ValueError:
                print("Введи число от 1 до 9!")


class ComputerPlayer(Player):
    def make_move(self, board: Board) -> int:
        # 1. Попытаться выиграть
        for pos in board.get_empty_cells():
            board.cells[pos] = self.symbol
            if board.check_winner(self.symbol):
                board.cells[pos] = " "
                return pos
            board.cells[pos] = " "

        # 2. Заблокировать игрока
        opponent = "X" if self.symbol == "O" else "O"
        for pos in board.get_empty_cells():
            board.cells[pos] = opponent
            if board.check_winner(opponent):
                board.cells[pos] = " "
                return pos
            board.cells[pos] = " "

        # 3. Центр
        if board.is_empty(4):
            return 4

        # 4. Углы
        corners = [0, 2, 6, 8]
        empty_corners = [c for c in corners if board.is_empty(c)]
        if empty_corners:
            return random.choice(empty_corners)

        # 5. Случайный ход
        return random.choice(board.get_empty_cells())