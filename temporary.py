import pyxel


WINDOW_W = 192
WINDOW_H = 192

SCENE_TITLE = 0
SCENE_PLAY = 1

PLAYER_STOP_DOWN = 0
PLAYER_STOP_UP = 1
PLAYER_STOP_RIGHT = 2
PLAYER_STOP_LEFT = 3
PLAYER_WALK_DOWN = 4
PLAYER_WALK_UP = 5
PLAYER_WALK_RIGHT = 6
PLAYER_WALK_LEFT = 7

MUSIC_BUTTON_X = WINDOW_W - 8
MUSIC_BUTTON_Y = 0

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = PLAYER_STOP_DOWN

    def update(self):
        if pyxel.btn(pyxel.KEY_DOWN):
            self.state = PLAYER_WALK_DOWN
            self.y = min(self.y + 2, WINDOW_H - 16)
        elif pyxel.btn(pyxel.KEY_UP):
            self.state = PLAYER_WALK_UP
            self.y = max(self.y - 2, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.state = PLAYER_WALK_RIGHT
            self.x = min(self.x + 2, WINDOW_W - 14)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.state = PLAYER_WALK_LEFT
            self.x = max(self.x - 2, -1)
        else:
            if self.state == PLAYER_STOP_DOWN or self.state == PLAYER_WALK_DOWN:
                self.state = PLAYER_STOP_DOWN
            elif self.state == PLAYER_STOP_UP or self.state == PLAYER_WALK_UP:
                self.state = PLAYER_STOP_UP
            elif self.state == PLAYER_STOP_RIGHT or self.state == PLAYER_WALK_RIGHT:
                self.state = PLAYER_STOP_RIGHT
            elif self.state == PLAYER_STOP_LEFT or self.state == PLAYER_WALK_LEFT:
                self.state = PLAYER_STOP_LEFT

    def draw(self):
        if self.state == PLAYER_STOP_DOWN:
            pyxel.blt(self.x, self.y, 0, 64, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_STOP_UP:
            pyxel.blt(self.x, self.y, 0, 80, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_STOP_RIGHT:
            pyxel.blt(self.x, self.y, 0, 96, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_STOP_LEFT:
            pyxel.blt(self.x, self.y, 0, 112, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_WALK_DOWN:
            pyxel.blt(self.x, self.y, 0, 0, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_WALK_UP:
            pyxel.blt(self.x, self.y, 0, 16, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_WALK_RIGHT:
            pyxel.blt(self.x, self.y, 0, 32, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.state == PLAYER_WALK_LEFT:
            pyxel.blt(self.x, self.y, 0, 48, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)

class UI:
    def __init__(self):
        self.music_on = True
        self.line_on = False

    def update(self):
        self.update_music()

    def music_button_pressed(self,mouse_x,mouse_y):
        judge1 = MUSIC_BUTTON_X < mouse_x < MUSIC_BUTTON_X + 8
        judge2 = MUSIC_BUTTON_Y < mouse_y < MUSIC_BUTTON_Y + 8
        judge3 = pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
        return judge1 and judge2 and judge3

    def update_music(self):
        if self.music_button_pressed(pyxel.mouse_x, pyxel.mouse_y):
            if self.music_on:
                pyxel.stop()
                self.music_on = False
            else:
                pyxel.playm(0, loop=True)
                self.music_on = True

    def draw(self,string=""):
        self.draw_music()
        self.draw_line(string)

    def draw_music(self):
        if self.music_on:
            pyxel.blt(MUSIC_BUTTON_X, MUSIC_BUTTON_Y, 1, 64, 0, 8, 8, 6)
        else:
            pyxel.blt(MUSIC_BUTTON_X, MUSIC_BUTTON_Y, 1, 72, 0, 8, 8, 6)

    def draw_line(self,string):
        if self.line_on:
            pyxel.rect(0, (WINDOW_H*3) // 4, WINDOW_W,WINDOW_H // 4, 0)
            pyxel.rectb(0, (WINDOW_H*3) // 4, WINDOW_W,WINDOW_H // 4, 7)
            pyxel.text(2, (WINDOW_H*3) // 4 + 2, string, 7)

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, title="Hello Pyxel", fps=10)
        pyxel.load("my_resource.pyxres")
        pyxel.image(2).load(0, 0, "pyxel_examples/assets/pyxel_logo_38x16.png")
        pyxel.mouse(True)
        self.scene = SCENE_TITLE
        self.player = Player((WINDOW_W // 2) - 8, 64)
        self.ui = UI()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_title_scene()
        self.player.update()
        self.ui.update()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.scene = SCENE_PLAY
            pyxel.playm(0, loop=True)

    def draw(self):
        if self.scene == SCENE_TITLE:
            pyxel.cls(0)
            self.draw_title_scene()
        if self.scene == SCENE_PLAY:
            pyxel.cls(7)
            pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 6)
            pyxel.blt((WINDOW_W // 2) - 32, 8, 1, 0, 0, 64, 64, 6)
            self.player.draw()
            pyxel.blt((WINDOW_W // 2) - 32, 104, 1, 0, 64, 64, 64, 6)
            """
            for i in range(3):
                pyxel.blt((WINDOW_W // 2) - 32, 80 + 32*i, 1, 0, 64, 64, 64, 6)
            """
            # pyxel.blt(self.player.x + 20,self.player.y + 20, 0, 0, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)
            self.ui.draw()

    def draw_title_scene(self):
        s = "Hello, Pyxel!"
        pyxel.text((WINDOW_W // 2) - len(s)*2, 41, s, pyxel.frame_count % 16)
        pyxel.blt((WINDOW_W // 2) - 19, 66, 2, 0, 0, 38, 16)


App().run()
