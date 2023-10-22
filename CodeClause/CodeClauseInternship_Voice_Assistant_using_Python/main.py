import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit as kit
import datetime
import requests
import re

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define your OpenWeatherMap API key here
weather_api_key = "ba43220a3b900010ac46ac8da0906546"

# Function to get weather information
def get_weather(city="vetapalem"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
        return f"The weather in {city} is {weather_description} with a temperature of {temperature:.2f}°C."
    else:
        return "I couldn't fetch weather information at the moment."

# Function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define the voice assistant function
def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()
            print("You said:", text)

            # Add your commands and responses here
            if "hello mike" in text:
                response = "Hello sir I am Mike! How can I assist you?"
            elif "open google" in text:
                response = "Opening Google."
                webbrowser.open("https://www.google.com")
            elif "search" in text:
                query = re.search(r'search (.+)', text).group(1)
                response = f"Searching for '{query}' on Google."
                kit.search(query)
            elif "play music" in text:
                response = "Playing music on YouTube."
                kit.playonyt("music")
            elif "play song" in text:
                song_name = re.search(r'play song (.+)', text).group(1)
                response = f"Playing '{song_name}' on YouTube."
                kit.playonyt(song_name)
            elif "what's the time" in text:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                response = f"The current time is {current_time}."
            elif "what's the weather like" in text:
                response = get_weather()
            elif "open linkedin" in text:
                response="Opening LinkedIn"
                webbrowser.open("https://in.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F")
            elif "thank you mike" in text:
                response = "It's my pleasure sir! If you have more questions or requests, feel free to ask."
            else:
                response = "I didn't understand your command."

            print("Assistant:", response)
            speak(response)

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the request: {e}")

if __name__ == "__main__":
    voice_assistant()
