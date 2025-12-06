from core.utils import DISPLAY_WIDTH, DISPLAY_HEIGHT
import math

class FormationManager:

    def __init__(self):
        self.W = DISPLAY_WIDTH
        self.H = DISPLAY_HEIGHT

    
    def get_positions(self, formation_type, count=5, start_x=100, start_y=50, spacing=80):
        positions = []
        if formation_type == "manual_line":
            for i in range(count):
                positions.append((start_x + (i * spacing), start_y))
        elif formation_type == "line":
            positions = self.line(count)
        elif formation_type == "grid":
            rows, cols = 2, 4
            for r in range(rows):
                for c in range(cols):
                    positions.append((start_x + c * spacing, start_y + r * spacing))
        elif formation_type == "slant_right":
            y_axis = -100
            for i in range(count):
                positions.append((start_x - (50 * i), y_axis - (50 * i)))
        elif formation_type == "slant_left":
            y_axis = -100
            for i in range(count):
                positions.append((start_x + (50 * i), y_axis + (50 * -i)))
        return positions
    
    
    def line(self, count):
        x = self.W // (count + 1)
        poses = []
        for i in range(1, count+1):
            poses.append((x * i, -100))
        return poses

    def circle_formation(self, center, radius, count):
        cx, cy = center
        positions = []
        for i in range(count):
            angle = (2 * math.pi / count) * i
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            positions.append((x, y))
        return positions
    
    def spiral_formation(self, center, spacing, turns, count):
        cx, cy = center
        positions = []
        for i in range(count):
            angle = (i / count) * (2 * math.pi * turns)
            radius = spacing * i
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            positions.append((x, y))
        return positions
    
    def v_wave(self, count, spacing=80):
        
        positions = []
        mid = count // 2
        start_y = -100
        center_x = self.W // 2

        for i in range(count):
            offset = i - mid
            x = center_x + offset * spacing
            y = start_y - abs(offset) * 40
            positions.append((x, y))

        return positions


