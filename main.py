import turtle
import pandas
screen = turtle.Screen()
screen.title("State Game")
image = ("100_day_py/25_csv_pandas/50_states_game/blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("100_day_py/25_csv_pandas/50_states_game/50_states.csv")
all_state = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answere_state = screen.textinput(title=f"{len(guessed_state)}/50 States correct", prompt="what's another state name").title()

    if answere_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("100_day_py/25_csv_pandas/50_states_game/state_to_learn.csv")
        break
        
    if answere_state in all_state:
        guessed_state.append(answere_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answere_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answere_state)
        
