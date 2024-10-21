def draw_square(width, height):

    print('-' * width)
    
    for _ in range(height):
        print('|' + ' ' * (width-2) + '|')
    
    if height > 1:
        print('-' * width)

draw_square(10, 3)
