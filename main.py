import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.penup()
t.hideturtle()


data = pandas.read_csv("50_states.csv")
states = data.state

all_states_list = data.state.to_list()
# for state in states:
#    all_states_list.append(state)

#game_is_on = True
states_list_guessed = []

while len(states_list_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_list_guessed)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states_not_guessed = []
        # for item in all_states_list:
        #     if item not in states_list_guessed:
        #         states_not_guessed.append(item)

        states_not_guessed = [item for item in all_states_list if item not in states_list_guessed]
        data_to_csv = pandas.DataFrame(states_not_guessed)
        data_to_csv.to_csv("states_to_learn.csv")
        break
    if str(answer_state) in all_states_list:
        states_list_guessed.append(answer_state)
        state_data = data[data.state == answer_state]
        # x_coordinate = int((data[data.state == answer_state]).x)
        # y_coordinate = int((data[data.state == answer_state]).y)
        t.goto(x=int(state_data.x), y=int(state_data.y))
        t.write(answer_state)





#screen.exitonclick()