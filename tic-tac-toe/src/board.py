from typing import List, Optional

class Board:
    def __init__(self):
        self.cells: List[str] = [" "] * 9

    def display(self) -> None:
        print("\n")
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("-----------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("-----------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print()

    def is_empty(self, position: int) -> bool:
        return self.cells[position] == " "

    def make_move(self, position: int, symbol: str) -> bool:
        if 0 <= position <= 8 and self.is_empty(position):
            self.cells[position] = symbol
            return True
        return False

    def get_empty_cells(self) -> List[int]:
        return [i for i in range(9) if self.cells[i] == " "]

    def is_full(self) -> bool:
        return " " not in self.cells

    def check_winner(self, symbol: str) -> bool:
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if all(self.cells[i] == symbol for i in combo):
                return True
        return False