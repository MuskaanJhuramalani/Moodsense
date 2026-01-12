from textblob import TextBlob
import json
from datetime import datetime
from graphs import graph_menu




# ---------- HELPER FUNCTIONS ----------
def load_json(path):
    """Load JSON data from file, return empty list if file not found"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_json(path, data):
    """Save data to JSON file"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def search_entries(entries, query):
    """Search entries by keyword, mood, or date"""
    query = query.lower()
    results = []
    for entry in entries:
        if (
            query in entry["text"].lower()
            or query in entry["response"].lower()
            or query in entry["mood"].lower()
            or query in entry["date"]
        ):
            results.append(entry)
    return results


def filter_by_mood(entries, mood):
    """Filter entries by mood"""
    mood = mood.lower()
    return [entry for entry in entries if entry["mood"] == mood]


def detect_mood(user_text):
    """Detect mood based on keywords and sentiment polarity"""
    text_lower = user_text.lower()
    analysis = TextBlob(user_text)
    polarity = analysis.sentiment.polarity

    if any(word in text_lower for word in ["tired", "drained", "stressed", "low"]):
        mood = "drained"
    elif any(word in text_lower for word in ["happy", "excited", "hopeful", "glad"]):
        mood = "happy"
    elif any(word in text_lower for word in ["calm", "peaceful", "relaxed"]):
        mood = "calm"
    elif any(word in text_lower for word in ["confused", "lost", "unsure"]):
        mood = "confused"
    elif polarity > 0.3:
        mood = "hopeful"
    elif polarity < -0.2:
        mood = "low"
    else:
        mood = "neutral"

    return mood, polarity


def show_entries(entries):
    """Display a list of entries nicely"""
    for i, entry in enumerate(entries, 1):
        print(f"{i}. 📅 {entry['date']} | Mood: {entry['mood']}")
        print(f"   💭 Text: {entry['text']}")
        if entry["response"]:
            print(f"   ✍️ Response: {entry['response']}")
        print("-" * 50)


def add_entry():
    """Add a new mood entry"""
    user_text = input("\nHow are you feeling today? ")
    mood, polarity = detect_mood(user_text)

    print(f"\nDetected Mood: {mood}")
    print(f"Sentiment Score (polarity): {polarity}")

    # Load prompts and emotion cards
    prompts = load_json("data/prompts.json")
    emotion_cards = load_json("data/emotion_cards.json")

    mood_prompt = prompts.get(mood, ["Write anything you want."])[0]
    print(f"\nYour Writing Prompt:\n -> {mood_prompt}")

    card = emotion_cards.get(mood)
    if card:
        print(f"\nEmotion Card for {mood.upper()}:")
        print(f"Emoji: {card['emoji']}")
        print(f"Color: {card['color']}")
        print(f"Keywords: {', '.join(card['keywords'])}")
        print(f"Quote: \"{card['quote']}\"")

    response = input("\nYour Response (optional): ")

    # Save entry
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "text": user_text,
        "mood": mood,
        "prompt": mood_prompt,
        "response": response
    }

    entries = load_json("data/entries.json")
    entries.append(entry)
    save_json("data/entries.json", entries)
    print("\n✅ Your entry has been saved!")

    # Save mood log
    log_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "mood": mood,
        "polarity": polarity
    }
    mood_log = load_json("data/mood_log.json")
    mood_log.append(log_entry)
    save_json("data/mood_log.json", mood_log)


def main_menu():
    """Show main menu and handle user choices"""
    while True:
        print("\n📌 MoodSense Menu")
        print("1. Add a new mood entry")
        print("2. Filter entries by mood")
        print("3. Search past entries")
        print("4. View mood analytics")
        print("5. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            entries = load_json("data/entries.json")
            mood_query = input("Enter mood to filter by: ").lower()
            filtered = filter_by_mood(entries, mood_query)
            if not filtered:
                print("\n❌ No entries found for this mood.")
            else:
                print(f"\n🎯 Entries with mood '{mood_query}':\n")
                show_entries(filtered)
        elif choice == "3":
            entries = load_json("data/entries.json")
            query = input("Enter a keyword, mood, or date (YYYY-MM-DD): ")
            results = search_entries(entries, query)
            if not results:
                print("\n❌ No matching entries found.")
            else:
                print(f"\n🔍 Found {len(results)} matching entries:\n")
                show_entries(results)
        elif choice == "4":
           graph_menu()
        elif choice == "5":
           print("\n👋 Goodbye! Stay mindful!")
           break


# ---------- RUN PROGRAM ----------
if __name__ == "__main__":
    print("Welcome to MoodSense!")
    main_menu()
