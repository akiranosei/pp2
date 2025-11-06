import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('times new roman', 22)
    radius = 15
    mode = 'draw'
    color_mode = 'blue'
    color = (0, 0, 255)
    drawing = False
    start_pos = None
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                    color_mode = 'red'
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                    color_mode = 'green'
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                    color_mode = 'blue'
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)
                    color_mode = 'yellow'
                elif event.key == pygame.K_1:
                    mode = 'draw'
                elif event.key == pygame.K_2:
                    mode = 'rect'
                elif event.key == pygame.K_3:
                    mode = 'circle'
                elif event.key == pygame.K_4:
                    mode = 'eraser'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if mode == 'draw' or mode == 'eraser':
                        points = points + [event.pos]

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if mode == 'rect' and start_pos:
                        end_pos = event.pos
                        rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.rect(screen, color if mode != 'eraser' else (0, 0, 0), rect, 0)
                    elif mode == 'circle' and start_pos:
                        end_pos = event.pos
                        radius_circle = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                        pygame.draw.circle(screen, color if mode != 'eraser' else (0, 0, 0), start_pos, radius_circle)
                    drawing = False
                    start_pos = None

            elif event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw' or mode == 'eraser':
                    points = points + [event.pos]
                    points = points[-256:]

        if mode == 'draw' or mode == 'eraser':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, 'eraser' if mode == 'eraser' else color_mode)
                i += 1
        instructions = [
            "1 → Draw    2 → Rectangle    3 → Circle    4 → Eraser", "R/G/B/Y → Change color", "Left click → Draw"]

        y_offset = 5
        for line in instructions:
            text_surface = font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (10, y_offset))
            y_offset += 20
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
main()