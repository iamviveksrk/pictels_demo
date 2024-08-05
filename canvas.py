from ipycanvas import Canvas, hold_canvas

width, height = 1500, 750
mid = int(0.95*width*0.5)

canvas = Canvas(width=width, height=height, sync_image_data=True)
canvas.fill_style = "#DA7297"
canvas.fill_rect(mid, 0, width/40, height)
canvas.fill_style = "#667BC6"

font_size = 32
canvas.font = f"{font_size}px serif"

drawing = False
marker_size = int(height/20)

def myround(x, base=marker_size):
    return base * round((x-base//2)/base)

def on_mouse_down(x, y):
    global drawing
    drawing = True

    if abs(x - mid) <= width/40:
        canvas.clear_rect(0, 0, mid, height)
        canvas.clear_rect(mid + width/40, 0, mid, height)

def on_mouse_move(x, y):
    global drawing
    if not drawing:
        return

    with hold_canvas():
        if x < mid:
            canvas.fill_rect(myround(x), myround(y), marker_size)

def on_mouse_up(x, y):
    global drawing
    drawing = False
    
    canvas.clear_rect(mid + width/40, 0, mid, height)
    pixels = ['  '.join(list(i)) for i in (canvas.get_image_data().sum(axis=2)[:,:int(mid)][::marker_size, ::marker_size] > 0).astype(int).astype(str)]

    for row in range(len(pixels)):
        canvas.stroke_text(pixels[row], int(width*0.55), font_size*row + int(height*0.1))


canvas.on_mouse_down(on_mouse_down)
canvas.on_mouse_move(on_mouse_move)
canvas.on_mouse_up(on_mouse_up)

canvas