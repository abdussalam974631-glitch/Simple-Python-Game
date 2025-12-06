import pygame

class WaveOverlay:
    def __init__(self, font, screen_rect):
        self.font = font
        self.screen_rect = screen_rect
        self.text_surf = None
        self.alpha = 0
        self.state = "hidden"
        self.timer = 0

        self.fade_in_time = 500
        self.hold_time = 1200
        self.fade_out_time = 500

    def show(self, wave_number):
        text = f"WAVE {wave_number}"
        self.text_surf = self.font.render(text, True, (255, 255, 255))
        self.text_surf = self.text_surf.convert_alpha()
        self.alpha = 0
        self.state = "fade_in"
        self.timer = 0

    def update(self, dt):
        if self.state == "hidden":
            return

        self.timer += dt

        # FADE IN
        if self.state == "fade_in":
            progress = min(self.timer / self.fade_in_time, 1)
            self.alpha = int(progress * 255)

            if progress >= 1:
                self.state = "hold"
                self.timer = 0

        # HOLD STILL
        elif self.state == "hold":
            self.alpha = 255
            if self.timer >= self.hold_time:
                self.state = "fade_out"
                self.timer = 0

        # FADE OUT
        elif self.state == "fade_out":
            progress = min(self.timer / self.fade_out_time, 1)
            self.alpha = int(255 * (1 - progress))

            if progress >= 1:
                self.state = "hidden"

    def draw(self, screen):
        if self.state == "hidden" or self.text_surf is None:
            return

        surf = self.text_surf.copy()
        surf.set_alpha(self.alpha)
        rect = surf.get_rect(center=self.screen_rect.center)

        screen.blit(surf, rect)
