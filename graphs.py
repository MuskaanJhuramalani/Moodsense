import json
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime


def load_mood_log():
    with open("data/mood_log.json", "r", encoding="utf-8") as f:
        return json.load(f)


# ---------- GRAPH 1: Mood Frequency ----------
def mood_frequency():
    data = load_mood_log()
    moods = [entry["mood"] for entry in data]

    mood_counts = Counter(moods)

    plt.figure()
    plt.bar(mood_counts.keys(), mood_counts.values())
    plt.title("Mood Frequency")
    plt.xlabel("Mood")
    plt.ylabel("Count")
    plt.show()


# ---------- GRAPH 2: Mood Over Time ----------
def mood_timeline():
    data = load_mood_log()

    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in data]
    polarity = [entry["polarity"] for entry in data]

    plt.figure()
    plt.plot(dates, polarity)
    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Polarity")
    plt.show()


# ---------- GRAPH MENU ----------
def graph_menu():
    while True:
        print("\n📊 Analytics Menu")
        print("1. Mood frequency chart")
        print("2. Sentiment trend over time")
        print("3. Back to main menu")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            mood_frequency()
        elif choice == "2":
            mood_timeline()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice")
