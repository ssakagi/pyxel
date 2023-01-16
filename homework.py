import pyxel


WINDOW_W = 192
WINDOW_H = 192

SCENE_TITLE = 0
SCENE_EVENT1 = 1
SCENE_PLAY = 2

PLAYER_STOP_DOWN = 0
PLAYER_STOP_UP = 1
PLAYER_STOP_RIGHT = 2
PLAYER_STOP_LEFT = 3
PLAYER_WALK_DOWN = 4
PLAYER_WALK_UP = 5
PLAYER_WALK_RIGHT = 6
PLAYER_WALK_LEFT = 7

CAT_WALK_DOWN = 0
CAT_WALK_UP = 1
CAT_WALK_RIGHT = 2
CAT_WALK_LEFT = 3

MUSIC_BUTTON_X = WINDOW_W - 8
MUSIC_BUTTON_Y = 0

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.posture = PLAYER_STOP_DOWN

    def update(self):
        if pyxel.btn(pyxel.KEY_DOWN):
            self.posture = PLAYER_WALK_DOWN
            self.y = min(self.y + 2, WINDOW_H - 16)
        elif pyxel.btn(pyxel.KEY_UP):
            self.posture = PLAYER_WALK_UP
            self.y = max(self.y - 2, 0)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.posture = PLAYER_WALK_RIGHT
            self.x = min(self.x + 2, WINDOW_W - 14)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.posture = PLAYER_WALK_LEFT
            self.x = max(self.x - 2, -1)
        else:
            if self.posture == PLAYER_STOP_DOWN or self.posture == PLAYER_WALK_DOWN:
                self.posture = PLAYER_STOP_DOWN
            elif self.posture == PLAYER_STOP_UP or self.posture == PLAYER_WALK_UP:
                self.posture = PLAYER_STOP_UP
            elif self.posture == PLAYER_STOP_RIGHT or self.posture == PLAYER_WALK_RIGHT:
                self.posture = PLAYER_STOP_RIGHT
            elif self.posture == PLAYER_STOP_LEFT or self.posture == PLAYER_WALK_LEFT:
                self.posture = PLAYER_STOP_LEFT

    def draw_stop_down(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 6)

    def draw(self):
        if self.posture == PLAYER_STOP_DOWN:
            pyxel.blt(self.x, self.y, 0, 64, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_STOP_UP:
            pyxel.blt(self.x, self.y, 0, 80, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_STOP_RIGHT:
            pyxel.blt(self.x, self.y, 0, 96, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_STOP_LEFT:
            pyxel.blt(self.x, self.y, 0, 112, ((pyxel.frame_count // 3) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_WALK_DOWN:
            pyxel.blt(self.x, self.y, 0, 0, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_WALK_UP:
            pyxel.blt(self.x, self.y, 0, 16, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_WALK_RIGHT:
            pyxel.blt(self.x, self.y, 0, 32, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)
        elif self.posture == PLAYER_WALK_LEFT:
            pyxel.blt(self.x, self.y, 0, 48, ((pyxel.frame_count // 2) % 4)*16, 16, 16, 6)

class Cat:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.posture = CAT_WALK_UP

    def update_walk_down(self):
        self.y += 2

    def draw_walk_up(self):
        pyxel.blt(self.x, self.y, 0, 16, 64, 16, 16, 6)

    def draw(self):
        if self.posture == CAT_WALK_DOWN:
            pyxel.blt(self.x, self.y, 0, 0, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)
        elif self.posture == CAT_WALK_UP:
            pyxel.blt(self.x, self.y, 0, 16, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)
        elif self.posture == CAT_WALK_RIGHT:
            pyxel.blt(self.x, self.y, 0, 32, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)
        elif self.posture == CAT_WALK_LEFT:
            pyxel.blt(self.x, self.y, 0, 48, 64 + ((pyxel.frame_count // 2) % 2)*16, 16, 16, 6)

class Shrine:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 0, 0, 64, 64, 6)

class Torii:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 0, 64, 64, 64, 6)

class UI:
    def __init__(self):
        self.music_on = True

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

    def draw_music(self):
        if self.music_on:
            pyxel.blt(MUSIC_BUTTON_X, MUSIC_BUTTON_Y, 1, 64, 0, 8, 8, 6)
        else:
            pyxel.blt(MUSIC_BUTTON_X, MUSIC_BUTTON_Y, 1, 72, 0, 8, 8, 6)

    def draw_line(self,string):
        pyxel.rect(0, (WINDOW_H*3) // 4, WINDOW_W,WINDOW_H // 4, 0)
        pyxel.rectb(0, (WINDOW_H*3) // 4, WINDOW_W,WINDOW_H // 4, 7)
        pyxel.text(2, (WINDOW_H*3) // 4 + 2, string, 7)

class Event1Manager:
    def __init__(self,player,cat,shrine,torii,ui,time):
        self.state = 0
        self.player = player
        self.cat = cat
        self.shrine = shrine
        self.torii = torii
        self.ui = ui
        self.time = time

    def update(self):
        if self.state == 0:
            return self.update_state0()
        elif self.state == 1:
            return self.update_state1()
        elif self.state == 2:
            return self.update_state2()

    def update_state0(self):
        if pyxel.frame_count >= self.time + 20:
            self.state = 1
        return SCENE_EVENT1

    def update_state1(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.state = 2
            self.cat.posture = CAT_WALK_DOWN
        return SCENE_EVENT1

    def update_state2(self):
        self.cat.update_walk_down()
        if self.cat.y >= WINDOW_H + 8:
            pyxel.playm(0, loop=True)
            return SCENE_PLAY
        return SCENE_EVENT1

    def draw(self):
        if self.state == 0:
            self.draw_state0()
        elif self.state == 1:
            self.draw_state1()
        elif self.state == 2:
            self.draw_state2()

    def draw_state0(self):
        pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 6)
        self.shrine.draw()
        self.player.draw_stop_down()
        self.cat.draw_walk_up()
        self.torii.draw()

    def draw_state1(self):
        pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 6)
        self.shrine.draw()
        self.player.draw_stop_down()
        self.cat.draw_walk_up()
        self.torii.draw()
        s = ""
        for i in range(min((pyxel.frame_count - 20) // 5, 15)):
            s += list("key...return...")[i]
        self.ui.draw_line(s)

    def draw_state2(self):
        pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 6)
        self.shrine.draw()
        self.player.draw_stop_down()
        self.cat.draw()
        self.torii.draw()

class SceneManager:
    def __init__(self):
        self.scene = SCENE_TITLE
        self.player = Player((WINDOW_W // 2) - 8, 64)
        self.cat = Cat(self.player.x, self.player.y + 20)
        self.shrine = Shrine((WINDOW_W // 2) - 32, 8)
        self.torii = Torii((WINDOW_W // 2) - 32, 104)
        self.ui = UI()

    def update(self):
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_EVENT1:
            self.scene = self.event1_manager.update()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            args = [self.player, self.cat, self.shrine, self.torii, self.ui, pyxel.frame_count]
            self.event1_manager = Event1Manager(*args)
            self.scene = SCENE_EVENT1

    def update_play_scene(self):
        self.player.update()
        self.ui.update_music()

    def draw(self):
        pyxel.cls(0)
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_EVENT1:
            self.event1_manager.draw()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()

    def draw_title_scene(self):
        s = "Homework"
        pyxel.text((WINDOW_W // 2) - len(s)*2, 41, s, pyxel.frame_count % 16)
        pyxel.blt((WINDOW_W // 2) - 19, 66, 2, 0, 0, 38, 16)

    def draw_play_scene(self):
        pyxel.bltm(0, 0, 0, 0, 0, WINDOW_W, WINDOW_H, 6)
        self.shrine.draw()
        self.player.draw()
        self.torii.draw()
        self.ui.draw_music()

class App:
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, title="Homework", fps=10)
        pyxel.load("my_resource.pyxres")
        pyxel.image(2).load(0, 0, "pyxel_logo_38x16.png")
        pyxel.mouse(True)
        self.scene_manager = SceneManager()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw()


App().run()
