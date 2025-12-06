import pygame

def load_frames(sheet, frame_width, frame_height, size=None):
    frames = []
    sheet_width, sheet_height = sheet.get_size()

    for y in range(0, sheet_height, frame_height):
        for x in range(0, sheet_width, frame_width):
            frame = sheet.subsurface((x, y, frame_width, frame_height))
            frame = pygame.transform.scale(frame, size=size) if size else frame
            frames.append(frame)

    return frames
