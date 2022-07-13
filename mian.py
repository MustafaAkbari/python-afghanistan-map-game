import turtle
from turtle import Turtle, Screen
import pandas
import random
from tkinter import messagebox

# turtle.colormode(255)
#
#
# def generate_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     generated_color = (r, g, b)
#     return generated_color

color_list = ["red", "white", "blue", "black"]
window = Screen()
window.title("Afghanistan State Detection")
window.setup(width=1000, height=759)
image = "Afghan_map.gif"
window.addshape(image)
turtle.shape(image)
# def get_x_y_core(x, y):
#     print(x, y)
#
#
#
# window.onscreenclick(get_x_y_core)

data = pandas.read_csv("afghanistan_states.csv")
all_state = data.state.tolist()
guessed_states = []
while len(guessed_states) < 34:
    answer = window.textinput(title=f"{len(guessed_states)}/34 States Correct",
                              prompt="Type name of state.\nType 'Exit' to exit.").capitalize()
    try:
        if answer == "Exit":
            missed_states = []
            for state in all_state:
                if state not in guessed_states:
                    missed_states.append(state)
            new_missed_data = pandas.DataFrame(missed_states)
            new_missed_data.to_csv("missed_states.csv")
            break
        if answer in all_state:
            guessed_states.append(answer)
        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.color(random.choice(color_list))
        state_turtle.penup()
        state_data = data[data.state == answer]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(answer, font=("arial", 10, "bold"))
    except TypeError:
        messagebox.showerror("Type Error", "please type correctly")
        pass
