import pandas
import turtle

# create the screen with particular image shape
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read into csv document to get data
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_answer = []

while len(correct_answer) < 50:
    # ask for input from player
    player_answer = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                                     prompt="What's the state's name?").title()
    # enter exit to quit the game and create a new csv file to show mission states
    if player_answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_answer:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # write the name of state once player type the right and not repeatable name
    if player_answer in states_list and player_answer not in correct_answer:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == player_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(player_answer)
        correct_answer.append(player_answer)

