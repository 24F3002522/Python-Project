"""
Turtle Racing
=============
An interactive terminal-and-graphics racing game built with Python's turtle module.
Pick your turtle, watch the countdown, and cheer it on to victory!

Usage:   python turtle_racing.py
Python:  3.9+  |  No external packages required
"""

import random
import time
import turtle

# ── Constants ──────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 700, 600
FINISH_Y = HEIGHT // 2 - 30
START_Y = -HEIGHT // 2 + 50
ALL_COLORS = [
    "red", "green", "blue", "orange", "yellow",
    "black", "purple", "pink", "brown", "cyan",
]


# ── Terminal I/O ───────────────────────────────────────────────────────────────

def get_number_of_racers() -> int:
    """Prompt until the user enters a valid racer count (2–10)."""
    while True:
        entry = input("How many turtles should race? (2–10): ").strip()
        if entry.isdigit() and 2 <= int(entry) <= 10:
            return int(entry)
        print("  Please enter a whole number between 2 and 10.")


def get_player_bet(colors: list) -> str:
    """Display available colors and return the color the player bets on."""
    print("\nPick your turtle:")
    for idx, color in enumerate(colors, 1):
        print(f"  {idx}. {color}")
    while True:
        entry = input("Enter the number of your turtle: ").strip()
        if entry.isdigit() and 1 <= int(entry) <= len(colors):
            return colors[int(entry) - 1]
        print(f"  Enter a number between 1 and {len(colors)}.")


# ── Screen & Track ─────────────────────────────────────────────────────────────

def init_screen() -> turtle.Screen:
    """Create and configure the turtle Screen."""
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor("lightyellow")
    screen.tracer(0)    # manual screen.update() for smoother animation
    return screen


def configure_screen(screen: turtle.Screen) -> None:
    """Re-apply visual settings after a screen.clear() call (play again)."""
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor("lightyellow")
    screen.tracer(0)


def draw_track(num_racers: int) -> None:
    """Draw lane dividers, a start line, and the finish line."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    spacing = WIDTH // (num_racers + 1)

    # Lane dividers
    pen.pensize(1)
    pen.color("#cccccc")
    for i in range(num_racers + 2):
        x = -WIDTH // 2 + i * spacing
        pen.penup()
        pen.goto(x, -HEIGHT // 2)
        pen.pendown()
        pen.goto(x, HEIGHT // 2)

    # Start line
    pen.penup()
    pen.goto(-WIDTH // 2, START_Y + 5)
    pen.color("blue")
    pen.pensize(2)
    pen.pendown()
    pen.goto(WIDTH // 2, START_Y + 5)
    pen.penup()
    pen.goto(0, START_Y + 8)
    pen.write("START", align="center", font=("Arial", 10, "bold"))

    # Finish line
    pen.penup()
    pen.goto(-WIDTH // 2, FINISH_Y)
    pen.color("red")
    pen.pensize(3)
    pen.pendown()
    pen.goto(WIDTH // 2, FINISH_Y)
    pen.penup()
    pen.goto(0, FINISH_Y + 6)
    pen.write("FINISH", align="center", font=("Arial", 10, "bold"))


def label_player_turtle(colors: list, player_color: str, screen: turtle.Screen) -> None:
    """Write 'YOU' below the player's starting turtle so they know which one to watch."""
    spacing = WIDTH // (len(colors) + 1)
    idx = colors.index(player_color)
    x = -WIDTH // 2 + (idx + 1) * spacing
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(x, START_Y - 22)
    label.color(player_color if player_color != "yellow" else "goldenrod")
    label.write("YOU", align="center", font=("Arial", 10, "bold"))
    screen.update()


def create_turtles(colors: list) -> list:
    """Spawn and position one turtle per color on the start line."""
    spacing = WIDTH // (len(colors) + 1)
    turtles = []
    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.shape("turtle")
        t.left(90)
        t.penup()
        t.setpos(-WIDTH // 2 + (i + 1) * spacing, START_Y)
        t.pendown()
        t.speed(0)
        turtles.append(t)
    return turtles


# ── Animations ─────────────────────────────────────────────────────────────────

def draw_countdown(screen: turtle.Screen) -> None:
    """Show a 3 → 2 → 1 → GO! countdown in the center of the screen."""
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 0)

    for text, color in [("3", "red"), ("2", "orange"), ("1", "gold"), ("GO!", "green")]:
        msg.clear()
        msg.color(color)
        msg.write(text, align="center", font=("Arial", 72, "bold"))
        screen.update()
        time.sleep(0.7)
        msg.clear()

    screen.update()


def draw_winner_banner(winner: str, player_bet: str, screen: turtle.Screen) -> None:
    """Overlay the winner and the player's result on screen."""
    # Use a safe contrast color for yellow turtles
    banner_color = winner if winner != "yellow" else "goldenrod"

    title = turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.goto(0, 30)
    title.color(banner_color)
    title.write(
        f"{winner.upper()} WINS!",
        align="center",
        font=("Arial", 34, "bold"),
    )

    sub = turtle.Turtle()
    sub.hideturtle()
    sub.penup()
    sub.goto(0, -15)

    if winner == player_bet:
        sub.color("darkgreen")
        sub.write(
            "Your turtle won!  Great pick!",
            align="center",
            font=("Arial", 15, "bold"),
        )
    else:
        sub.color("firebrick")
        sub.write(
            f"You picked {player_bet}.  Better luck next time!",
            align="center",
            font=("Arial", 13, "normal"),
        )

    screen.update()


# ── Race Logic ─────────────────────────────────────────────────────────────────

def race(colors: list, screen: turtle.Screen) -> str:
    """
    Move each turtle forward by a random distance each tick.
    Return the color of the first turtle to cross FINISH_Y.
    """
    turtles = create_turtles(colors)
    color_map = dict(zip(turtles, colors))
    screen.update()

    while True:
        for t in turtles:
            t.forward(random.randint(1, 20))
            if t.ycor() >= FINISH_Y:
                screen.update()
                return color_map[t]
        screen.update()


# ── Entry Point ────────────────────────────────────────────────────────────────

def main() -> None:
    print("=" * 44)
    print("        Welcome to Turtle Racing!")
    print("=" * 44)

    screen = init_screen()

    while True:
        # ── Setup ──────────────────────────────────────
        num_racers = get_number_of_racers()
        shuffled = ALL_COLORS[:]
        random.shuffle(shuffled)
        race_colors = shuffled[:num_racers]

        player_bet = get_player_bet(race_colors)
        print(f"\n  You're backing the [{player_bet}] turtle. Good luck!\n")

        # ── Track ───────────────────────────────────────
        draw_track(num_racers)
        screen.update()
        label_player_turtle(race_colors, player_bet, screen)
        time.sleep(0.5)

        # ── Countdown + Race ────────────────────────────
        draw_countdown(screen)
        winner = race(race_colors, screen)

        # ── Result ──────────────────────────────────────
        draw_winner_banner(winner, player_bet, screen)
        print(f"\n  Winner: {winner.upper()}")
        if winner == player_bet:
            print("  Your turtle won!")
        else:
            print("  Better luck next time!")

        time.sleep(4)

        # ── Play Again ──────────────────────────────────
        again = input("\nPlay again? (y / n): ").strip().lower()
        if again != "y":
            break

        # Clear canvas and re-apply settings for the next round
        screen.clear()
        configure_screen(screen)

    screen.bye()
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()