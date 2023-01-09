import pyxel


WINDOW_W = 200
WINDOW_H = 200

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

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = PLAYER_STOP_DOWN

    def update(self):
        if pyxel.btn(pyxel.KEY_DOWN):
            self.state = PLAYER_WALK_DOWN
            self.y = min(self.y + 2, 104)
        elif pyxel.btn(pyxel.KEY_UP):
            self.state = PLAYER_WALK_UP
            self.y = max(self.y - 2, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.state = PLAYER_WALK_RIGHT
            self.x = min(self.x + 2, 146)
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

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, title="Hello Pyxel", fps=10)
        pyxel.load("my_resource.pyxres")
        pyxel.image(2).load(0, 0, "pyxel_examples/assets/pyxel_logo_38x16.png")
        self.scene = SCENE_TITLE
        self.player = Player(75,45)

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_title_scene()
        self.player.update()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_PLAY
            pyxel.playm(0, loop=True)

    def draw(self):
        if self.scene == SCENE_TITLE:
            pyxel.cls(0)
            self.draw_title_scene()
        if self.scene == SCENE_PLAY:
            pyxel.cls(7)
            pyxel.blt(50, 0, 1, 0, 0, 64, 64, 6)
            self.player.draw()
            pyxel.blt(50, 64, 1, 0, 64, 64, 64, 6)
            # pyxel.blt(self.player.x + 20,self.player.y + 20, 0, 0, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)

    def draw_title_scene(self):
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 2, 0, 0, 38, 16)


App().run()
