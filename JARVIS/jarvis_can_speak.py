import datetime
import random
import webbrowser
import time
import threading
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get current time
def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

# Function to get current date
def get_date():
    now = datetime.datetime.now()
    return now.strftime("%B %d, %Y")

# Function to get current time of day and provide a greeting
def get_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Function to get a random joke
def tell_joke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you get if you cross a snowman and a vampire? Frostbite.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs.",
        "What’s orange and sounds like a parrot? A carrot!"
    ]
    return random.choice(jokes)

# Function to open websites
def open_website(query):
    if 'youtube' in query:
        webbrowser.open("https://www.youtube.com/")
        return "Opening YouTube..."
    elif 'google' in query:
        webbrowser.open("https://www.google.com/")
        return "Opening Google..."
    elif 'stackoverflow' in query:
        webbrowser.open("https://www.stackoverflow.com/")
        return "Opening StackOverflow..."
    elif 'deadshot' in query:
        webbrowser.open("https://deadshot.io/")
        return "Opening Deadshot Game..."
    else:
        return "Sorry, I can't open that website."

# Function to simulate a weather query (mock response)
def get_weather(city):
    weather_data = {
        "new york": "Sunny, 25°C",
        "london": "Cloudy, 15°C",
        "paris": "Rainy, 12°C",
        "tokyo": "Clear sky, 30°C",
    }
    city = city.lower()
    return weather_data.get(city, "Sorry, I don't have weather information for that city.")

# Function to get a motivational quote
def motivational_quote():
    quotes = [
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "It does not matter how slowly you go as long as you do not stop.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
        "The only way to do great work is to love what you do."
    ]
    return random.choice(quotes)

# Function to play a number guessing game
def play_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    speak("I'm thinking of a number between 1 and 20. Can you guess it?")
    
    while True:
        try:
            user_guess = int(input("Your guess: "))
            attempts += 1
            if user_guess < number_to_guess:
                speak("Too low! Try again.")
            elif user_guess > number_to_guess:
                speak("Too high! Try again.")
            else:
                speak(f"Correct! You've guessed the number in {attempts} attempts.")
                return f"Correct! You've guessed the number in {attempts} attempts."
        except ValueError:
            speak("Please enter a valid number.")

# Function to give a random fun fact
def fun_fact():
    facts = [
        "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible.",
        "A group of flamingos is called a 'flamboyance'.",
        "Octopuses have three hearts and blue blood!",
        "Bananas are berries, but strawberries aren’t.",
        "You can’t hum while holding your nose closed."
    ]
    return random.choice(facts)

# Function to set a reminder
def set_reminder(reminder_time, message):
    # Calculate the time to wait before the reminder
    current_time = datetime.datetime.now()
    time_to_wait = reminder_time - current_time
    if time_to_wait.total_seconds() > 0:
        time.sleep(time_to_wait.total_seconds())
        speak(f"Reminder: {message}")
    else:
        speak("The reminder time has already passed!")

# Function to process and respond to user commands
def respond_to_query(query):
    query = query.lower()

    if "hello" in query or "hi" in query:
        response = f"{get_greeting()} How can I assist you today?"
    
    elif "time" in query:
        response = f"The current time is {get_time()}."
    
    elif "date" in query:
        response = f"Today's date is {get_date()}."
    
    elif "joke" in query:
        response = tell_joke()
    
    elif "fun fact" in query:
        response = fun_fact()
    
    elif "open youtube" in query or "open google" in query or "open stackoverflow" in query:
        response = open_website(query)
    
    elif "weather" in query:
        city = query.split("weather in")[-1].strip()
        if city:
            response = f"The weather in {city.title()} is: {get_weather(city)}."
        else:
            response = "Please provide a city to get the weather."
    
    elif "quote" in query or "motivation" in query:
        response = motivational_quote()
    
    elif "guessing game" in query:
        response = play_guessing_game()
    
    elif "remind me" in query:
        # Extract reminder time and message
        try:
            time_part = query.split("in")[-1].strip()
            message = time_part.split("and")[0].strip()
            reminder_time = datetime.datetime.now() + datetime.timedelta(seconds=int(time_part.split()[0]))
            # Use threading to avoid blocking the main thread
            threading.Thread(target=set_reminder, args=(reminder_time, message)).start()
            response = f"Reminder set for {reminder_time.strftime('%H:%M:%S')}: {message}"
        except Exception as e:
            response = "Sorry, I couldn't set the reminder. Please use the format 'remind me in <X> seconds to <message>'."
    
    elif "exit" in query or "quit" in query:
        response = "Goodbye! Have a great day!"
    
    else:
        response = "Sorry, I didn't understand that. Can you please rephrase?"

    # Make the assistant speak the response
    speak(response)
    return response

# Main function to start the assistant
def start_assistant():
    speak("Hello, I am your assistant. How can I help you? Type 'exit' to quit.")
    
    while True:
        # Get the user input (text)
        user_input = input("You: ")

        # Process the input and respond
        response = respond_to_query(user_input)

        print(f"Assistant: {response}")

        # Exit condition
        if 'exit' in user_input.lower() or 'quit' in user_input.lower():
            break

# Start the assistant
if __name__ == "__main__":
    start_assistant() 
