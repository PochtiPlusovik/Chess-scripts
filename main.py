import os
import chess
import chess.engine
from chess.svg import board

board = chess.Board()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear_console()
    print("_______________")
    print(board)
    print("_______________")

engine = chess.engine.SimpleEngine.popen_uci("/home/pion/Stockfish/src/stockfish")

try:

    win = 0
    while win < 1:

        try:

            print_board()
            hod = input("Ваш ход: ")

            if hod == "exit":
                print("Вы вышли. Игра окончена.")
                os._exit(0)

            try:
                move = chess.Move.from_uci(hod)
            except chess.engine.EngineTerminatedError:
                print("Невозможный ход! Попробуйте снова.")
                # board.pop()

            board.push(move)
            print_board()

            usr = 2
            while usr > 1:
                result = engine.play(board, chess.engine.Limit(time=2))
                clear_console()
                board.push(result.move)
                break

            if board.is_checkmate():
                print("Мат!")
                win += 2
            elif board.is_stalemate():
                print("Пат!")
                win += 2
            elif board.is_check():
                print("Шах!")
            elif board.is_legal(move):
                print("Пат!")
                win += 2

        except AssertionError:
            print("Невозможный ход! Попробуйте снова.")
        except chess.InvalidMoveError:
            print("Невозможный ход! Попробуйте снова.")
        except chess.engine.EngineTerminatedError:
            print("Невозможный ход! Попробуйте снова.")
            board.pop()

        continue

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем.")

print("Игра окончена.")
os._exit(0)
