import turtle
import math
import const 
import ru_local


def get_num_hexagons() -> int:
    '''
    Function asks the user for the number of hexagons. 
    After the last correct user input, the function returns 
    the number of hexagons as an integer.
    :return color:
    '''
    #display the color selection header
    print(ru_local.COLOR_TITLE)

    #flag for detecting the first input
    t = True

    #Infinite cycle for repeated request in case of incorrect input
    while True:
        try:
            #NUMBER_INPUT for the first input, and INPUT_AGAIN for the second input
            if t == True:
                number = int(input(ru_local.NUMBER_INPUT))
            else:
                number = int(input(ru_local.INPUT_AGAIN))
            
            #Check that the number is in the acceptable range
            if number >= 4 and number <= 20:
                break
            else:
                t = False
                print(ru_local.NUMBER_ERROR)

        except:
            t = False
            print(ru_local.ERROR)

    return number


def get_color_choice() -> str:
    '''
    Function displays a list of colors for the user to choose. 
    After the last correct user input, the function returns the color name string.
    :return color:
    '''
    #display the number selection header
    print(ru_local.COLOR_TITLE)

    #flag for detecting the first input
    t = True

    #Infinite cycle for repeated request in case of incorrect input
    while True:
        try:
            #COLOR_INPUT for the first input, and INPUT_AGAIN for the second input
            if t == True:
                color_index = int(input(ru_local.COLOR_INPUT))
            else:
                color_index = int(input(ru_local.INPUT_AGAIN))
            
            #Getting the color from the list by index
            color = const.COLOR[color_index - 1]
            break

        except:
            print(ru_local.COLOR_ERROR)

    return color


def draw_hexagon(x: int, y: int, side_len: int, color: str) -> None:
    '''
    function for drawing hexagon

    :param x:
    :param y:
    :param side_len:
    :param color:
    :return:
    '''
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(90)

    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.end_fill()


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
    d_2 = 500 / ( 2* q+1)
    d = d_2 * 2
    l = (d_2/math.sqrt(3)) * 2

    #turning off drawing animation
    turtle.tracer(0)

    #Cycle for line-by-line drawing
    for numb_horiz in range(q):
        for numb_vert in range(q):
            #Condition for checking a row.
            #Depending on whether the row is even, the row should be shifted to the left or not.
            if numb_horiz%2 != 0:
                x, y = -250 + (d * numb_vert), 250 - (l/2) - (numb_horiz * 1.5 * l)
            else:
                x, y = -250 + d_2 + (d * numb_vert), 250 - (l/2) - (numb_horiz * 1.5 * l)

            #Condition for choosing the color of hexes so that there is a diagonal coloring. 
            #Group in pairs rows and watch on ewen.
            if (numb_horiz//2)%2 != 0:
                if numb_vert%2 != 0:
                    draw_hexagon(x, y, l, first_color)
                else:
                    draw_hexagon(x, y, l, second_color)
            else:
                if numb_vert%2 != 0:
                    draw_hexagon(x, y, l, second_color)
                else:
                    draw_hexagon(x, y, l, first_color)

    turtle.mainloop()


def main():
    '''
    The main function of the program is to draw hexagons.
    
    The function performs a sequence of actions:
    1. Requests the user to select the first color
    2. Requests the user to select a second color  
    3. Requests the number of hexagons to draw
    4. Calls the function for drawing hexagons with the received parameters
    
    The program is designed to create a graphic composition of hexagons
    with alternating two colors.
    
    Functions used:
    - get_color_choice(): getting the color from the user
    - get_num_hexagons(): getting the number of hexagons
    - draw_hexagons(): drawing hexagons with the previously specified parameters
    '''
    first_color = get_color_choice()
    second_color = get_color_choice()
    number = get_num_hexagons()

    draw_hexagons(number, first_color, second_color)


if __name__ == '__main__':
    '''
    The entry point to the program when launching the file directly.
    This block of code is executed only when the script is run directly,
    and is not imported as a module in another program.

    Calls the main() main function to start the program.
    '''
    main()
