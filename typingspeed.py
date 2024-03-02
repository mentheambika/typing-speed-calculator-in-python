import time

def typing_speed(start_time, end_time, typed_words):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60.0
    words_per_minute = len(typed_words) / minutes
    return words_per_minute

def main():
    text_to_type = "Hello,how are you..?what is your day plan..? have a gooddd dayyy...!!! goooooddd bbbyyeeeee!!!!"

    print("Type the following text:")
    print(text_to_type)

    input("Press Enter when you are ready to start typing.")
    start_time = time.time()

    typed_input = input("Type here: ")

    end_time = time.time()

    typed_words = typed_input.split()
    correct_words = [word for word in typed_words if word in text_to_type.split()]

    accuracy = (len(correct_words) / len(text_to_type.split())) * 100

    typing_speed = typing_speed(start_time, end_time, typed_words)

    print("\nTyping Speed Results:")
    print(f"Typed Words: {len(typed_words)}")
    print(f"Correct Words: {len(correct_words)}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typing Speed: {typing_speed:.2f} WPM")

    # Provide feedback based on typing speed
    if typing_speed < 30:
        print("Your typing speed is below average. Keep practicing to improve.")
    elif 30 <= typing_speed < 60:
        print("Your typing speed is average. Keep practicing for better accuracy.")
    else:
        print("Great job! Your typing speed is above average.")

if __name__ == "__main__":
    main()
