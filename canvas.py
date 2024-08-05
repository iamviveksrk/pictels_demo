from ipycanvas import Canvas, hold_canvas

width, height = 1500, 750
mid = int(0.95*width*0.5)

canvas = Canvas(width=width, height=height, sync_image_data=True)
canvas.fill_style = "#DA7297"
canvas.fill_rect(mid, 0, width/40, height)
canvas.fill_style = "#667BC6"

font_size = int(height * 0.064)
canvas.font = f"{font_size}px serif"

drawing = False
marker_size = int(height/10)
zeros = [(i, j) for i in range(9) for j in range(10)]
    
index_to_base = lambda i: int(marker_size*(i))
base_to_index = lambda x: round((x-marker_size//2)/marker_size)

for i in zeros:
    canvas.stroke_text('0', mid + width/20 + index_to_base(i[0]), index_to_base(i[1]) + font_size)

def myround(x, base=marker_size):
    return marker_size * base_to_index(x)

def on_mouse_down(x, y):
    global drawing
    global zeros
    drawing = True
    

    if abs(x - mid) <= width/40:
        canvas.clear_rect(0, 0, mid, height)
        canvas.clear_rect(mid + width/40, 0, mid, height)
        zeros = [(i, j) for i in range(9) for j in range(10)]
        
        for i in zeros:
            canvas.stroke_text('0', mid + width/20 + index_to_base(i[0]), index_to_base(i[1]) + font_size)
    

def on_mouse_move(x, y):
    global drawing
    global zeros
    if not drawing:
        return

    with hold_canvas():
        if x < mid - width/40:
            canvas.fill_rect(myround(x), myround(y), marker_size)
            canvas.clear_rect(mid + width/20 + myround(x) - font_size/4, myround(y) + font_size/4, font_size, font_size)
            canvas.stroke_text('1', mid + width/20 + myround(x), myround(y) + font_size)
            

def on_mouse_up(x, y):
    global drawing
    global zeros
    drawing = False


canvas.on_mouse_down(on_mouse_down)
canvas.on_mouse_move(on_mouse_move)
canvas.on_mouse_up(on_mouse_up)

canvas