import os
import chess.engine
from chess.svg import board
from pathlib import Path

folder = Path(".")

if Path("Stockfish.txt").exists():
    with open("Stockfish.txt", "r", encoding="utf-8") as file:
        spath = file.read()
else:
    path = input("\nВведите путь к движку Stockfish:")
    with open("Stockfish.txt", "w", encoding="utf-8") as file:
        file.write(path)
    with open("Stockfish.txt", "r", encoding="utf-8") as file:
        spath = file.read()

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


    try:
        engine = chess.engine.SimpleEngine.popen_uci(spath)
    except FileNotFoundError:
        print("Неверный путь к движку. Убедитесь в его правильности и попробуйте снова.")
        Path("Stockfish.txt").unlink()
        os._exit(1)
    except PermissionError:
        print("Неверный путь к движку или отсутствие прав. Если вы уверены в правильности пути, решите проблему с правами доступа.")
        Path("Stockfish.txt").unlink()
        os._exit(1)

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
