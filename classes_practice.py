# import turtle
# import prettytable
# thomas = turtle.Turtle()

# from turtle import Turtle, Screen

# thomas = Turtle()
# thomas.shape("turtle")
# thomas.color("#D00000")
# thomas.forward(100)
# # print(thomas)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)