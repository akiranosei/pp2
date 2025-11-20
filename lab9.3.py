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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
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
                elif event.key == pygame.K_5:
                    mode = 'square'
                elif event.key == pygame.K_6:
                    mode = 'right_triangle'
                elif event.key == pygame.K_7:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_8:
                    mode = 'rhombus'

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
                    elif mode == 'square' and start_pos:
                        end_pos = event.pos
                        side = max(abs(end_pos[0]-start_pos[0]), abs(end_pos[1]-start_pos[1]))
                        x = min(start_pos[0], end_pos[0])
                        y = min(start_pos[1], end_pos[1])
                        rect = pygame.Rect(x, y, side, side)
                        pygame.draw.rect(screen, color if mode != 'eraser' else (0,0,0), rect, 0)

                    elif mode == 'right_triangle' and start_pos:
                        end_pos = event.pos
                        points_triangle = [start_pos, (start_pos[0], end_pos[1]), end_pos]
                        pygame.draw.polygon(screen, color if mode != 'eraser' else (0,0,0), points_triangle)

                    elif mode == 'equilateral_triangle' and start_pos:
                        end_pos = event.pos
                        dx = end_pos[0] - start_pos[0]
                        height_triangle = int(abs(dx) * (3**0.5) / 2)
                        if end_pos[1] < start_pos[1]:
                            top = (start_pos[0] + dx // 2, start_pos[1] - height_triangle)
                        else:
                            top = (start_pos[0] + dx // 2, start_pos[1] + height_triangle)
                        points_triangle = [start_pos, end_pos, top]
                        pygame.draw.polygon(screen, color if mode != 'eraser' else (0,0,0), points_triangle)

                    elif mode == 'rhombus' and start_pos:
                        end_pos = event.pos
                        mid_x = (start_pos[0] + end_pos[0]) // 2
                        mid_y = (start_pos[1] + end_pos[1]) // 2
                        points_rhombus = [(mid_x, start_pos[1]),
                        (end_pos[0], mid_y),
                        (mid_x, end_pos[1]),
                        (start_pos[0], mid_y) ]
                        pygame.draw.polygon(screen, color if mode != 'eraser' else (0,0,0), points_rhombus)
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
            "1 → Draw    2 → Rectangle    3 → Circle    4 → Eraser 5 → Square  6 → Right Triangle  7 → Equilateral Triangle  8 → Rhombus R/G/B/Y → Change color"]

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