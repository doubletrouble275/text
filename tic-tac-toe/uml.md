# UML-диаграмма игры «Крестики-нолики»

## Диаграмма классов

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam classFontStyle bold
hide empty members
title UML Class Diagram — Крестики-нолики (Человек vs Компьютер)

class Game {
  - board : Board
  - human : HumanPlayer
  - computer : ComputerPlayer
  - current_player : Player
  --
  + __init__()
  + switch_player()
  + run()
}

class Board {
  - cells : List[str]
  --
  + display()
  + is_empty(position : int) : bool
  + make_move(position : int, symbol : str) : bool
  + get_empty_cells() : List[int]
  + is_full() : bool
  + check_winner(symbol : str) : bool
}

abstract class Player {
  + name : str
  + symbol : str
  --
  + make_move(board : Board) : int
}

class HumanPlayer {
  --
  + make_move(board : Board) : int
}

class ComputerPlayer {
  --
  + make_move(board : Board) : int
}

Game "1" *-- "1" Board : содержит
Game "1" o-- "1" HumanPlayer : имеет
Game "1" o-- "1" ComputerPlayer : имеет
Game --> Player : current_player

Player <|-- HumanPlayer
Player <|-- ComputerPlayer

Player --> Board : использует
ComputerPlayer --> Board : анализирует

@enduml