from tkinter import *
import game.engine as eng
import game.board as bd


class CONST:
    WIDTH = 400
    HEIGHT = 300
    DEFAULT_SCORE = 2048
    DEFAULT_SIZE = (4, 4)
    TILE_HEIGHT = 5
    TILE_WIDTH = 10
    DEFAULT_WEIGHT = 1


class Game(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.frame = Frame(self.master)
        self.board = bd.Board(CONST.DEFAULT_SIZE)
        self.engine = eng.Engine(self.board, CONST.DEFAULT_SCORE)
        self.create_menu()
        self.frame.grid(row=0, column=0, sticky="NSEW")
        self.create_tiles()
        self.pack()

    def create_tiles(self):
        Grid.grid_rowconfigure(self.frame, 0, weight=CONST.DEFAULT_WEIGHT)
        Grid.grid_columnconfigure(self.frame, 0, weight=CONST.DEFAULT_WEIGHT)
        x = self.board.tiles.shape[0]
        y = self.board.tiles.shape[1]

        for i in range(x):
            Grid.columnconfigure(self.frame, i, weight=CONST.DEFAULT_WEIGHT)
            Grid.rowconfigure(self.frame, i, weight=CONST.DEFAULT_WEIGHT)

        for i in range(x):
            for j in range(y):
                s = StringVar()
                label = Button(self.frame,
                               textvariable=s,
                               height=CONST.TILE_HEIGHT,
                               width=CONST.TILE_WIDTH)
                s.set(str(""))

                label.grid(column=j, row=i)

    @classmethod
    def create_score_menu(cls, menu_bar):
        score_menu = Menu(menu_bar)

        for i in range(8, 14):
            score_menu.add_cascade(label=str(2 ** i))

        return score_menu

    def create_menu(self):
        menu_bar = Menu(self.master, tearoff=0)
        score_menu = self.create_score_menu(menu_bar)
        menu_bar.add_cascade(label='Score', menu=score_menu)
        menu_bar.add_cascade(label='Dims')
        menu_bar.add_command(label='Quit', command=self.master.quit)
        self.master.config(menu=menu_bar)

    @staticmethod
    def escape(e):
        sys.exit()

    def up(self):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass


def main():
    # create app
    root = Tk()
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    root.title('2048')

    # set window size
    root.minsize(width=CONST.WIDTH, height=CONST.HEIGHT)
    root.maxsize(width=CONST.WIDTH, height=CONST.HEIGHT)

    # setup app
    app = Game(master=root)

    # click handlers
    root.bind("<Escape>", app.escape)
    root.bind("<Left>", app.left)
    root.bind("<Right>", app.right)
    root.bind("<Down>", app.down)
    root.bind("<Up>", app.up)

    # control flow
    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()
