class Animation:
    def __init__(self, frames, frame_duration=100, loop=True):
        self.frames = frames
        self.frame_duration = frame_duration
        self.loop = loop
        self.current_time = 0
        self.current_frame = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.frame_duration:
            self.current_time = 0
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.current_frame = 0 if self.loop else len(self.frames) - 1

    def get_frame(self):
        return self.frames[self.current_frame]
