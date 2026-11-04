import turtle
import pandas
import time

from pandas.core.interchange.dataframe_protocol import DataFrame

TOTAL_STATES = 27

def main():
    screen = turtle.Screen()
    screen.title("Brazil States Game")
    data = pandas.read_csv("27_states.csv")
    states = list(data['state'])
    screen.setup(width=700, height=800)

    image = "mapa_brasil_pequeno.gif"
    screen.addshape(image)

    turtle.shape(image)

    states = [state.lower() for state in states]

    game_is_on = True
    num_states_guessed = 0
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    states_guessed = []

    while game_is_on:
        if num_states_guessed == 27:
            game_is_on = False
            writer.write("You Win!",align="center", font=("Arial", 24, "bold"))
            continue

        answer_state: str = str(screen.textinput(title=f"{num_states_guessed}/{TOTAL_STATES} States Corr ", prompt="What's another state's name?")).lower()
        time.sleep(0.7)

        if answer_state == "exit":
            states = list(data['state'])
            missing_states = [state for state in states if state not in states_guessed]
            missing_states = pandas.DataFrame(missing_states)
            missing_states.to_csv("missing_states.csv", index=False)
            break

        if answer_state in states and answer_state not in states_guessed:
            answer_state = answer_state.title()
            if " Do " in answer_state:
                answer_state = answer_state.replace(" Do ", " do ")

            if " De " in answer_state:
                answer_state = answer_state.replace(" De ", " de ")

            num_states_guessed += 1
            states_guessed.append(answer_state)
            state_data = data[data['state'] == answer_state]
            writer.goto(int(state_data.x.item()), int(state_data.y.item()))
            writer.write(state_data.state.item())
        screen.update()


if __name__ == "__main__":
    main()