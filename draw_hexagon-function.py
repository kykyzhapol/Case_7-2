import turtle as t
import math as m


def draw_hexagon(q: int, first_color: str, second_color: str) -> None:
    '''
    Два цвета для окрашивания
    количество (N) шестиугольников в одном ряду (от 4 до 20)
    картинка 500x500 пикселей
    Чередование цвета в каждой строке
    :return:
    '''
    d_2 = 500/(2*q+1)
    d = d_2*2
    l = (d_2/m.sqrt(3))*2
    t.speed(100)


    for numb_horiz in range(q):
        for numb_vert in range(q):
            if numb_horiz%2 != 0:
                t.teleport(-250 + d_2 + (d * numb_vert), (250 - (d_2 / 2) - (numb_horiz * d)) - l/2)
            else:
                t.teleport(-250 + d + (d * numb_vert), (250 - (d_2 / 2) - (numb_horiz * d)) - l/4)
            if numb_vert%2 != 0:
                t.pen(pencolor='black', fillcolor=first_color, pensize=1)
            else:
                t.pen(pencolor='black', fillcolor=second_color, pensize=1)
            t.down()
            t.begin_fill()
            t.left(30)
            for _ in range(6):
                t.forward(l)
                t.right(60)
            t.right(30)
            t.up()
    t.mainloop()


q = 10
first_color = 'red'
second_color = 'blue'

draw_hexagon(q, first_color, second_color)