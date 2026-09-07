import os
import chess.engine
from chess.svg import board

try:

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

    win = 0
    while win < 1:
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

        continue

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем.")

print("Игра окончена.")
os._exit(0)
