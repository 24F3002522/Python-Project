"""
Turtle Racing Game
==================

A simple animated turtle race built with Python's built-in `turtle` module.
Multiple turtles race to the finish line at random speeds — bet on a winner
and watch the race unfold!

Requirements:
    - Python 3.x (turtle module is included in the standard library)
    - No external dependencies

Usage:
    python turtle_race.py

Author: (your name here)
License: MIT
"""

import time
import random
import turtle


# ---------------------------- Configuration ---------------------------- #

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
FINISH_LINE_X = SCREEN_WIDTH // 2 - 50
START_X = -SCREEN_WIDTH // 2 + 50
TURTLE_SPEED_RANGE = (1, 5)  # min/max steps per move

COLORS = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow"]


# ------------------------------ Game Setup ------------------------------ #

def get_number_of_racers() -> int:
    """Prompt the user for how many turtles should race (2-8)."""
    while True:
        try:
            count = int(input("How many turtles should race? (2-8): "))
            if 2 <= count <= 8:
                return count
            print("Please enter a number between 2 and 8.")
        except ValueError:
            print("Please enter a valid number.")


def get_bet(colors: list) -> str:
    """Prompt the user to bet on a color."""
    print(f"Available colors: {', '.join(colors)}")
    while True:
        bet = input("Which turtle (color) do you bet on? ").strip().lower()
        if bet in colors:
            return bet
        print("Invalid color. Please choose from the list above.")


def setup_screen() -> turtle.Screen:
    """Create and configure the race track screen."""
    screen = turtle.Screen()
    screen.title("Turtle Race!")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)  # manual screen updates for smoother animation
    return screen


def draw_track(colors: list) -> None:
    """Draw the start line, finish line, and lane guides."""
    artist = turtle.Turtle()
    artist.hideturtle()
    artist.speed(0)
    artist.penup()

    lane_count = len(colors)
    lane_height = SCREEN_HEIGHT / (lane_count + 1)
    top_y = SCREEN_HEIGHT / 2 - lane_height

    # Finish line
    artist.goto(FINISH_LINE_X, top_y)
    artist.setheading(270)
    artist.pendown()
    artist.pensize(3)
    artist.color("black")
    artist.forward(SCREEN_HEIGHT - lane_height)
    artist.penup()

    # Finish label
    artist.goto(FINISH_LINE_X - 20, top_y + 20)
    artist.write("FINISH", font=("Arial", 14, "bold"))


def create_racers(colors: list) -> list:
    """Create turtle objects positioned at the starting line."""
    racers = []
    lane_count = len(colors)
    lane_height = SCREEN_HEIGHT / (lane_count + 1)
    top_y = SCREEN_HEIGHT / 2 - lane_height

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.penup()
        y = top_y - i * lane_height
        racer.goto(START_X, y)
        racer.setheading(0)
        racers.append(racer)

    return racers


# ------------------------------ Race Logic ------------------------------ #

def run_race(screen: turtle.Screen, racers: list) -> turtle.Turtle:
    """Animate the race until a turtle crosses the finish line."""
    winner = None
    while winner is None:
        for racer in racers:
            step = random.randint(*TURTLE_SPEED_RANGE)
            racer.forward(step)
            if racer.xcor() >= FINISH_LINE_X:
                winner = racer
                break
        screen.update()
        time.sleep(0.02)
    return winner


def announce_winner(screen: turtle.Screen, winner: turtle.Turtle, bet: str) -> None:
    """Display the winner and whether the player's bet was correct."""
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, SCREEN_HEIGHT / 2 - 40)
    announcer.color("black")

    winner_color = winner.color()[0]
    announcer.write(
        f"{winner_color.upper()} wins the race!",
        align="center",
        font=("Arial", 20, "bold"),
    )

    print(f"\n🏁 {winner_color.upper()} wins the race!")
    if bet == winner_color:
        print("🎉 You won your bet!")
    else:
        print(f"😢 You bet on {bet}, better luck next time!")

    screen.update()


# --------------------------------- Main ---------------------------------- #

def main() -> None:
    print("=== Welcome to Turtle Racing! ===\n")

    racer_count = get_number_of_racers()
    colors = random.sample(COLORS, racer_count)
    bet = get_bet(colors)

    screen = setup_screen()
    draw_track(colors)
    racers = create_racers(colors)

    print("\nRace starting...\n")
    winner = run_race(screen, racers)
    announce_winner(screen, winner, bet)

    print("\nClose the race window to exit.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
