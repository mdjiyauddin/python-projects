import time
import random

# ----------------------------
# Typing Speed Test by MD. Jiyauddin 
# ----------------------------

sentences = [
    "Practice makes a man perfect.",
    "Typing speed improves with daily practice.",
    "Consistency is the key to success.",
    "Never stop learning, because life never stops teaching.",
    "Hard work beats talent when talent doesn't work hard.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The future depends on what you do today.",
    "Discipline is the bridge between goals and accomplishment."
]


def typing_test():
    print("="*60)
    print("           🧠 Welcome to Typing Speed Test 🧠")
    print("="*60)
    input("👉 Press Enter to start the test...")

    # Random sentence
    
    sentence = random.choice(sentences)
    print("\n📝 Type this sentence below:\n")
    print(f"➡️ {sentence}")
    print("\nWhen you are ready, press Enter and start typing...")

    input("\nPress Enter to start typing...")
    start_time = time.time()
    typed = input("\n⏩ Start typing here: \n")
    end_time = time.time()

    total_time = end_time - start_time
    time_in_minutes = total_time / 60

    # Word per minute calculation
    
    words = sentence.split()
    typed_words = typed.split()
    correct_words = 0

    for i in range(min(len(words), len(typed_words))):
        if words[i] == typed_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(words)) * 100
    wpm = len(typed_words) / time_in_minutes
    cpm = len(typed) / time_in_minutes

    print("\n" + "="*60)
    print("📊 Typing Test Result:")
    print("="*60)
    print(f"⏱️ Time Taken: {total_time:.2f} seconds")
    print(f"💨 Words Per Minute (WPM): {wpm:.2f}")
    print(f"⌨️ Characters Per Minute (CPM): {cpm:.2f}")
    print(f"🎯 Accuracy: {accuracy:.2f}%")
    print("="*60)

    if accuracy >= 90:
        print("🔥 Excellent typing! Keep it up!")
    elif accuracy >= 70:
        print("👍 Good job! Thoda aur practice karo.")
    else:
        print("💪 Practice more to improve your speed and accuracy!")

# Run testing

typing_test()
