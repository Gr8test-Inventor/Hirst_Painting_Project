# import colorgram
#
# color_list = []
# colors = colorgram.extract('image.jpg', 60)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)


import turtle as turtle_module
import random
brush = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(240, 228, 200), (213, 239, 225), (209, 227, 241), (242, 216, 232), (209, 158, 113), (228, 216, 111),
              (122, 173, 204), (205, 136, 171), (124, 189, 158), (206, 78, 129), (56, 100, 152), (229, 167, 195),
              (162, 60, 110), (152, 215, 188), (179, 14, 60), (153, 86, 57), (141, 212, 225), (59, 172, 132),
              (212, 88, 69), (31, 171, 200), (234, 171, 160), (106, 111, 181), (178, 182, 224), (61, 121, 90),
              (172, 155, 55), (43, 48, 121), (25, 35, 72), (68, 19, 48), (168, 18, 10), (17, 57, 33), (61, 26, 15),              (24, 90, 53), (218, 218, 18), (80, 76, 31), (17, 82, 98), (253, 4, 59)]

brush.hideturtle()
brush.penup()
brush.setheading(135)
brush.forward(300)
brush.setheading(0)
brush.speed('fastest')


for _ in range(5):
    for _ in range(10):
        brush.dot(20, random.choice(color_list))
        brush.forward(50)
    # brush.goto(0, -100)
    brush.setheading(270)
    brush.forward(50)
    brush.setheading(180)
    for _ in range(10):
        brush.forward(50)
        brush.dot(20, random.choice(color_list))
    brush.setheading(270)
    brush.forward(50)
    brush.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
