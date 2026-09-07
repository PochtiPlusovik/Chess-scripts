import os
import chess
import chess.engine
from chess.svg import board

board = chess.Board()
path = input("\nВведите путь к движку Stockfish:")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear_console()
    print("_______________")
    print(board)
    print("_______________")

engine = chess.engine.SimpleEngine.popen_uci(path)

try:

    win = 0
    while win < 1:

        try:

            print_board()
            hod = input("Ваш ход: ")

            if hod == "exit":
                print("Вы вышли. Игра окончена.")
                os._exit(0)

            move = chess.Move.from_uci(hod)
            if board.is_legal(move):
                print("Ход обрабатывается...")
            else:
                print("Невозможный ход! Попробуйте снова.")
                continue

            board.push(move)
            print_board()

            result = engine.play(board, chess.engine.Limit(time=2))
            clear_console()
            board.push(result.move)

            if board.is_checkmate():
                print("Мат!")
                win += 2
            elif board.is_stalemate():
                print("Пат!")
                win += 2
            elif board.is_check():
                print("Шах!")

        except AssertionError:
            print("Невозможный ход! Попробуйте снова.")
        except chess.InvalidMoveError:
            print("Невозможный ход! Попробуйте снова.")

        continue

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем.")

print("Игра окончена.")
os._exit(0)
