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
        print(board)
        hod = input("Ваш ход: ")

        if hod == "exit":
            print("Вы вышли.")
            exit()

        move = chess.Move.from_uci(hod)
        board.push(move)
        clear_console()
        print(board)

        usr = 2
        while usr > 1:
            result = engine.play(board, chess.engine.Limit(time=2))
            clear_console()
            board.push(result.move)
            print(board)
            break

        if board.is_checkmate():
            print("Мат!")
            win += 2
        elif board.is_stalemate():
            print("Пат!")
            win += 2
        elif board.is_check():
            print("Невозможный ход!")
            win += 2

        continue

except KeyboardInterrupt:
    print("\nПрограмма прервана пользователем")

print("Игра окончена.")
exit()
