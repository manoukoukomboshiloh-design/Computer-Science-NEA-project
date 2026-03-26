import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question_bank import question_data as data
from timer import auto_timer


def display_menu(data):
    all_topics = list(data["topics"].keys())
    print("Welcome, please select a topic number")
    for i, topic in enumerate(all_topics, start=1):
        print(f"{i}. {topic}")
    print("0. Exit")
    try:
        choice = int(input("Enter a topic number: "))
        if choice == 0:
            print("Okie dokie see you soon..")
            return None
        elif 1 <= choice <= len(all_topics):
            return all_topics[choice - 1]
        else:
            print(f"Gotta be a number between 1 and {len(all_topics)}")
            return display_menu(data)
    except ValueError:
        print("Enter a valid whole number")
        return display_menu(data)

while True:
    selected_topic = display_menu(data)
    if selected_topic is None:
        print("Program ended")
        break
    topic_data = data["topics"][selected_topic]
    notes = topic_data["notes"]
    print(f"\n{'='*60}")
    print(f"TOPIC: {selected_topic}")
    print(f"{'='*60}\n")
    print("NOTES:")
    print("-" * 60)
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}\n")
    print(f"{'='*60}\n")
    print("\nYou have 10 minutes to revise the information.")
    auto_timer(selected_topic, data)