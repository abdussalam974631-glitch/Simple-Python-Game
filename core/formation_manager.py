from core.utils import DISPLAY_WIDTH, DISPLAY_HEIGHT

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
        elif formation_type == "v_shape":
            mid = count // 2
            for i in range(count):
                x = start_x + (i - mid) * spacing
                y = start_y + abs(i - mid) * 20
                positions.append((x, y))
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
    
