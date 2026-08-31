import os
import chess
import chess.engine

board = chess.Board()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


engine = chess.engine.SimpleEngine.popen_uci("/home/pion/Stockfish/src/stockfish")

try:

    win = 0
    while win < 1:

        try:
            clear_console()
            print(board)
            hod = input("Ваш ход: ")

            if hod == "exit":
                print("Вы вышли. Игра окончена.")
                os._exit(0)

            move = chess.Move.from_uci(hod)
            board.push(move)
            clear_console()
            print(board)

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
                print("Невозможный ход! Попробуйте снова.")
                win += 2

        except AssertionError:
            print("Невозможный ход! Попробуйте снова.")

        continue

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем.")

print("Игра окончена.")
os._exit(0)
