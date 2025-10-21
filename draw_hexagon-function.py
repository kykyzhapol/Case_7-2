import turtle as t
import math as m


def draw_hexagon(x: int, y: int, side_len: int, color: str) -> None:
    '''
    function for drawing each hexagon

    :param x:
    :param y:
    :param side_len:
    :param color:
    :return:
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(90)

    t.fillcolor(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side_len)
        t.right(60)
    t.end_fill()


def draw_hexagons(q: int, first_color: str, second_color: str) -> None:
    '''
        Two colors to color
    Number (N) of hexagons in one row (4 to 20)
    500x500 pixel image
    Alternating colors in each row

        * * *
      *       *
    *           *
      *       *
        * * *

    difference between top and botoom = 2l
    d - diameter of the inscribed circle
    d_2 - radius of the inscribed circle

    :param q:
    :param first_color:
    :param second_color:
    :return:
    '''
    d_2 = 500 / (2 * q + 1)
    d = d_2 * 2
    l = (d_2 / m.sqrt(3)) * 2
    # turning off animation
    t.tracer(0)

    # Cycle for line-by-line drawing
    for numb_horiz in range(q):
        for numb_vert in range(q):
            # Condition for checking a row.
            # Depending on whether the row is even, the row should be shifted to the left or not.
            if numb_horiz % 2 != 0:
                x, y = -250 + (d * numb_vert), 250 - (l / 2) - (numb_horiz * 1.5 * l)
            else:
                x, y = -250 + d_2 + (d * numb_vert), 250 - (l / 2) - (numb_horiz * 1.5 * l)

            # Condition for choosing the color of hexes so that there is a diagonal coloring.
            # Group in pairs rows and watch on ewen.
            if (numb_horiz // 2) % 2 != 0:
                if numb_vert % 2 != 0:
                    draw_hexagon(x, y, l, first_color)
                else:
                    draw_hexagon(x, y, l, second_color)
            else:
                if numb_vert % 2 != 0:
                    draw_hexagon(x, y, l, second_color)
                else:
                    draw_hexagon(x, y, l, first_color)
    t.mainloop()


q = 10
first_color = 'red'
second_color = 'blue'


draw_hexagons(q, first_color, second_color)
