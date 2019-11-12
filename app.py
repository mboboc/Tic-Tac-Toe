from tkinter import *


# draw table of X si O
def draw_table(table):
    print("\t   -------------    \n"
          "\t   | {} | {} | {} | \n"
          "\t   | {} | {} | {} | \n"
          "\t   | {} | {} | {} | \n"
          "\t   -------------    \n".format(table[0][0], table[0][1], table[0][2],
                                            table[1][0], table[1][1], table[1][2],
                                            table[2][0], table[2][1], table[2][2], ))


# check if elements from list are identical
def all_same_element(lst):
    if not lst:
        print("[all_same_element: list empty]")
        return -1
    ret = lst.count(lst[0]) == len(lst) and lst[0] != "+"
    return ret


# check rows if game is won
def check_row_win(table):
    for i in table:
        if all_same_element(i):
            return True


def check_col_win(table):
    if not table:
        print("[check_col_win: list empty]")
    for i in range(3):
        count = 0
        for j in range(3):
            if table[j][i] == table[0][i] and table[0][i] != "+":
                count += 1
        if count == 3:
            return True
    return False


# check diagonals if game is won
def check_diag_win(table):
    if not table:
        print("[check_diag_win: list empty]")
    count_primary = 0
    count_secondary = 0
    for i in range(3):
        if table[i][i] == table[0][0] and table[0][0] != "+":
            count_primary += 1
        for j in range(3):
            if i + j == 2:
                if table[i][j] == table[0][2] and table[0][2] != "+":
                    count_secondary += 1
    if count_primary == 3 or count_secondary == 3:
        return True
    return False


class Application(Frame):
    game_table = [["+", "+", "+"],
                  ["+", "+", "+"],
                  ["+", "+", "+"]]
    round = 0

    def check_over(self):
        not_over = False
        if check_col_win(self.game_table) or check_row_win(self.game_table) or check_diag_win(self.game_table):
            if self.round % 2 == 0:
                print("Congrats! First player WON!")
                Frame.quit(self)
                return
            else:
                print("Congrats! Second player WON!")
                Frame.quit(self)
                return
        for row in range(3):
            for col in range(3):
                if self.game_table[row][col] == "+":
                    not_over = True
        if not not_over:
            print("GAME OVER!It's a TIE!")
            Frame.quit(self)
            return

    def click(self, row, col):
        if self.game_table[row][col] != "X" and self.game_table[row][col] != "O":
            if self.round % 2 == 0:
                player = "O"
            else:
                player = "X"
            self.game_table[row][col] = player
            self.round += 1
            draw_table(self.game_table)
            self.check_over()

    def create_widgets(self):
        buttons = []
        for row in range(3):
            for col in range(3):
                b = Button(self, text=self.game_table[row][col], height=5, width=10,
                           command=lambda r=row, c=col: self.click(r, c))
                b.grid(row=row, column=col)
                buttons.append(b)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()


root = Tk()
app = Application(root)
app.mainloop()
root.destroy()
