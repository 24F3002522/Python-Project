import time
import sys


def typewriter(text, delay=0.03):
    """Print text one character at a time, like it's being typed live."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def countdown(seconds, message="Get ready"):
    """Show a small countdown before revealing the story."""
    print(message)
    for i in range(seconds, 0, -1):
        print(f"...{i}")
        time.sleep(1)


def load_story(filename="story.txt"):
    with open(filename, "r") as f:
        return f.read()


def find_placeholders(story):
    """Scan the story text and collect every <placeholder> exactly once,
    preserving the order they first appear in."""
    words = []
    seen = set()
    start_of_word = -1
    target_start = "<"
    target_end = ">"

    for i, char in enumerate(story):
        if char == target_start:
            start_of_word = i
        if char == target_end and start_of_word != -1:
            word = story[start_of_word:i + 1]
            if word not in seen:
                seen.add(word)
                words.append(word)
            start_of_word = -1

    return words


def collect_answers(words):
    """Ask the user for each placeholder, with light timing feedback."""
    answers = {}
    print(f"\nThis story needs {len(words)} words from you. Let's go!\n")
    time.sleep(0.5)

    for idx, word in enumerate(words, start=1):
        start_time = time.time()
        clean_name = word.strip("<>").replace("_", " ")
        answer = input(f"[{idx}/{len(words)}] Enter a word for '{clean_name}': ")
        elapsed = time.time() - start_time

        # A little playful feedback based on how fast they answered
        if elapsed < 2:
            print("  -> Wow, fast!")
        elif elapsed > 10:
            print("  -> Took your time there, hehe.")

        answers[word] = answer

    return answers


def build_story(story, answers):
    for word, answer in answers.items():
        story = story.replace(word, answer)
    return story


def main():
    story = load_story("story.txt")
    words = find_placeholders(story)
    answers = collect_answers(words)

    countdown(3, "\nAssembling your story")

    final_story = build_story(story, answers)

    print("\n===== YOUR STORY =====\n")
    typewriter(final_story, delay=0.02)
    print("\n=======================")


if __name__ == "__main__":
    main()