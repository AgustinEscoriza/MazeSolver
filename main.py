from graphics import Window, Line, Point

def main():
    win = Window(800, 600)

    line1 = Line(Point(50, 100), Point(0, 75))
    line2 = Line(Point(66, 33), Point(100, 75))
    win.draw_line(line1, "black")
    win.draw_line(line2, "black")
    win.wait_for_close()

main()
