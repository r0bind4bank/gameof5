def kolko_i_krzyzyk():
    # stworzenie planszy
    board_size = int(input("Podaj wielkość tablicy (od 5 do 20): "))
    if board_size < 5 or board_size > 20:
        print("Nieprawidłowa wielkość tablicy.")
        return

    # zapelnienie planszy znakami zapytania
    board = []
    for i in range(board_size):
        board.append(["?"] * board_size)

    player_1_turn = True

    while True:
        print_board(board)

        # wykonanie ruchu
        if player_1_turn:
            print("Gracz 1:")
        else:
            print("Gracz 2:")
        row = int(input("Podaj wiersz: ")) - 1
        col = int(input("Podaj kolumnę: ")) - 1

        # niepoprawne lub zajete pole
        if row < 0 or col < 0 or row >= board_size or col >= board_size:
            print("Nieprawidłowe współrzędne.")
            continue
        if board[row][col] != "?":
            print("To pole jest już zajęte.")
            continue

        # wykonanie ruchu (wpisanie wartosci)
        if player_1_turn:
            board[row][col] = "x"
        else:
            board[row][col] = "o"

        # sprawdzenie wygranej
        if check_win(board, player_1_turn):
            print_board(board)

            if player_1_turn:
                print("Gracz 1 wygrywa!")
            else:
                print("Gracz 2 wygrywa!")
            break

        # zmiana tury
        player_1_turn = not player_1_turn


def print_board(board):
    # wyswietlanie aktualnej planszy
    n = len(board)
    print("    ", end='')
    for i in range(n):
        print("  %02d " % (i + 1), end='')
    print()
    for i, row in enumerate(board):
        print(" %02d " % (i + 1), end='')
        for j in range(n):
            print(" %3s " % row[j], end='')
        print()


def check_win(board, player_1):
    # sprawdzanie wygranej
    symbol = "x" if player_1 else "o"

    n = len(board)

    # sprawdzanie wierszy
    for row in board:
        if row.count(symbol) == 5:
            return True

    # sprawdzanie kolumn nowe
    for col in range(len(board[0])):
        if [board[i][col] for i in range(n)].count(symbol) == 5:
            return True

    # sprawdzanie kolumn stare
    """
    for col in range(len(board[0])):
        if all(board[i][col] == symbol for i in range(5)):
            return True
            """

    # skosy \
    for row in range(0, n - 4):
        for col in range(0, n - 4):
            if all(board[row + i][col + i] == symbol for i in range(5)):
                return True

    # skosy /
    for row in range(0, n - 4):
        for col in range(4, n):
            if all(board[row + i][col - i] == symbol for i in range(5)):
                return True

    return False


kolko_i_krzyzyk()
