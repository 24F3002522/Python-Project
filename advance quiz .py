"""
Brain Rot Memes Quiz Game
Run: python brainrot_quiz.py
"""

import random

QUESTIONS = [
    {
        "topic": "Skibidi Toilet",
        "question": "What is the name of the viral series that features singing human heads inside porcelain bathroom fixtures?",
        "choices": {
            "A": ("Skibidi Toilet", True, "This is the wildly popular series created by DaFuq!?Boom! on YouTube."),
            "B": ("Cameraman", False, "Cameramen are the heroic rivals fighting the toilets in the series."),
            "C": ("Clockmen", False, "Clockmen appear later in the series as powerful allies."),
            "D": ("Speakerman", False, "Speakermen are allies with speakers for heads."),
        },
    },
    {
        "topic": "The State of Ohio",
        "question": 'When internet users say "Only in Ohio," what kind of situations are they usually describing?',
        "choices": {
            "A": ("Perfectly normal, quiet, and boring days", False, "The meme is actually used to describe the exact opposite of normal."),
            "B": ("Delicious food recipes and cooking shows", False, "This meme has nothing to do with cooking."),
            "C": ("Weird, chaotic, and bizarre events", True, '"Only in Ohio" is used to describe wild, unpredictable, and funny situations.'),
            "D": ("Peaceful beach vacations", False, "The meme is about chaos, not relaxation."),
        },
    },
    {
        "topic": "Mewing",
        "question": 'What is "Mewing," the popular internet trend and tongue posture technique, used for?',
        "choices": {
            "A": ("Making a loud cat sound", False, "Even though it sounds like a cat's meow, it is actually about facial posture."),
            "B": ("Improving your jawline by resting your tongue", True, "Mewing involves resting your tongue on the roof of your mouth to help define your jawline."),
            "C": ("Running very fast in a race", False, "Mewing is done silently, not during cardio workouts."),
            "D": ("A style of painting", False, "It is a personal grooming trend, not an art style."),
        },
    },
    {
        "topic": "Fanum Tax",
        "question": 'What does the slang term "Fanum Tax" mean?',
        "choices": {
            "A": ("Paying your parents for doing chores", False, "It's not a real tax or a payment to parents."),
            "B": ("Stealing or taking food from a friend", True, "Named after streamer Fanum, it means taking a portion of your friend's food."),
            "C": ("A tax you pay when buying video games", False, "It's a funny slang term for stealing snacks, not a real financial tax."),
            "D": ("A penalty for not doing your homework", False, "It has nothing to do with school."),
        },
    },
    {
        "topic": "Rizz",
        "question": 'If someone is said to have "W Rizz", what are they incredibly good at?',
        "choices": {
            "A": ("Winning video games every time", False, 'While "W" stands for "win," this term is about social skills.'),
            "B": ("Fixing broken items around the house", False, "It doesn't mean being handy or good at repairs."),
            "C": ("Running really fast", False, "This is not about athleticism."),
            "D": ("Charming people romantically", True, '"Rizz" is short for "charisma." Having "W Rizz" means you are great at charming your crush.'),
        },
    },
    {
        "topic": "Palate Cleanser",
        "question": "Just to check your brain still works outside of TikTok: what is the capital of France?",
        "choices": {
            "A": ("Marseille", False, "Marseille is France's second-largest city, but not the capital."),
            "B": ("Paris", True, "Paris has been the capital of France since long before Skibidi Toilet existed."),
            "C": ("Lyon", False, "Lyon is known for food and silk history, not the capital."),
            "D": ("Nice", False, "Nice is a coastal city on the French Riviera, not the capital."),
        },
    },
]


def ask_question(index, item):
    print(f"\nQ{index}. [{item['topic']}]")
    print(item["question"])
    for key in ["A", "B", "C", "D"]:
        print(f"  {key}) {item['choices'][key][0]}")

    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            return answer
        print("Please type A, B, C, or D.")


def verdict(score, total):
    if score == total:
        return "Maximum rot achieved. You have officially lost (won?) the internet."
    elif score >= total * 0.65:
        return "Deep in the algorithm. Your For You Page knows you well."
    elif score >= total * 0.3:
        return "Mild exposure. You've heard the terms but haven't fully absorbed the lore."
    else:
        return "Refreshingly untouched by brain rot. Please stay this way."


def run_quiz(shuffle=False):
    questions = QUESTIONS.copy()
    if shuffle:
        random.shuffle(questions)

    score = 0
    print("=" * 50)
    print("   BRAIN ROT IQ TEST")
    print("=" * 50)
    print(f"{len(questions)} questions. No skips. The algorithm is watching.")

    for i, item in enumerate(questions, start=1):
        answer = ask_question(i, item)
        text, is_correct, note = item["choices"][answer]
        if is_correct:
            print(f"✅ Correct! {note}")
            score += 1
        else:
            correct_key = next(k for k, v in item["choices"].items() if v[1])
            correct_text = item["choices"][correct_key][0]
            print(f"❌ Incorrect. {note}")
            print(f"   Correct answer: {correct_key}) {correct_text}")

    print("\n" + "=" * 50)
    print(f"FINAL SCORE: {score}/{len(questions)}")
    print(verdict(score, len(questions)))
    print("=" * 50)


if __name__ == "__main__":
    run_quiz(shuffle=False)a
    