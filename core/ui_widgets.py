class ScoreDisplay:
    def __init__(self, font, pos):
        self.font = font
        self.pos = pos
        self.score = 0

    def set_score(self, value):
        self.score = value

    def update(self, dt):
        pass

    def render(self, screen):
        txt = self.font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(txt, self.pos)

class LivesDisplay:
    def __init__(self, font, pos):
        self.font = font
        self.pos = pos
        self.lives = 5

    def set_lives(self, value):
        self.lives = value

    def update(self, dt):
        pass

    def render(self, screen):
        txt = self.font.render(f"Lives: {self.lives}", True, (255,255,255))
        screen.blit(txt, self.pos)

class WaveOverlay:
    def __init__(self, font, center):
        self.font = font
        self.center = center
        self.text = ""
        self.alpha = 0
        self.state = "idle"

    def show_wave(self, wave_number):
        self.text = f"Wave {wave_number}"
        self.alpha = 255
        self.state = "fade_out"

    def update(self, dt):
        if self.state == "fade_out":
            self.alpha -= 100 * (dt / 1000)
            if self.alpha <= 0:
                self.alpha = 0
                self.state = "idle"

    def render(self, screen):
        if self.alpha <= 0:
            return

        surface = self.font.render(self.text, True, (255,255,255))
        surface.set_alpha(int(self.alpha))
        rect = surface.get_rect(center=self.center)
        screen.blit(surface, rect)
