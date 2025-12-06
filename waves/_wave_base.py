# waves/wave_base.py
from abc import ABC, abstractmethod
from core.formation_manager import FormationManager

class Wave(ABC):
    """Base class for all enemy waves — handles stage timing and progression."""
    Fm = FormationManager()
    registry = {}  # Holds all subclasses: {wave_number: class}
    def __init__(self, scene):
        self.scene = scene
        self.enemies = []
        self.stages = []          # [(delay_in_ms, function), ...]
        self.stage_index = 0
        self.stage_timer = 0
        self.finished = False

    def __init_subclass__(cls, wave_number=None, **kwargs):
        """Automatically register wave subclasses."""
        super().__init_subclass__(**kwargs)
        if wave_number is None and cls.__name__.lower().startswith("wave"):
            try:
                wave_number = int(''.join(filter(str.isdigit, cls.__name__)))
            except ValueError:
                wave_number = None

        if wave_number is not None:
            Wave.registry[wave_number] = cls
    
    @abstractmethod
    def setup(self):
        """Each wave defines its stages here, e.g.:
        self.stages = [(0, self.stage_1), (3000, self.stage_2)]"""
        pass

    def update(self, dt):
        """Handles stage timing and automatic progression."""
        if self.finished:
            return

        self.stage_timer += dt

        # Run the next stage if its delay has passed
        if self.stage_index < len(self.stages):
            delay, func = self.stages[self.stage_index]
            if self.stage_timer >= delay:
                # print(f"[Wave] Running stage {self.stage_index+1}/{len(self.stages)}")
                func()
                self.stage_index += 1
                self.stage_timer = 0

        # If all stages are complete and no enemies remain
        elif not self.scene.enemies:
            self.finished = True
            # print("[Wave] Wave finished!")

    def is_finished(self):
        return self.finished
    
    def stage_rest(self):
        pass
