import serial
import time
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Function to recognize speech and return the text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening... Please speak into the laptop's mic.")
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio")
            speak_command("Could not understand the audio")
        except sr.RequestError:
            print("Could not request results; check your network connection")
            speak_command("Network connection error")
        return ""

# Function to send command to Arduino
def send_command(command):
    try:
        arduino.write((command + '\n').encode())
        print(f"Sent command: {command}")
        time.sleep(0.1)  # Short delay to ensure command is sent
    except Exception as e:
        print(f"Error: {e}")
        speak_command(f"Error: {e}")

# Function to speak the command
def speak_command(command):
    tts_engine.say(command)
    tts_engine.runAndWait()

# Main script
if __name__ == "__main__":
    try:
        # Replace 'COM4' with the appropriate port for your system
        arduino = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)  # Give time for the connection to establish

        while True:
            command = recognize_speech()
            print(f"Command received: {command}")
            
            if "red on" in command:
                send_command("red on")
                speak_command("Turning red on")
            elif "red off" in command:
                send_command("red off")
                speak_command("Turning red off")
            elif "blue on" in command:
                send_command("blue on")
                speak_command("Turning blue on")
            elif "blue off" in command:
                send_command("blue off")
                speak_command("Turning blue off")
            elif "fan on" in command:
                send_command("fan on")
                speak_command("Turning fan on")
            elif "fan off" in command:
                send_command("fan off")
                speak_command("Turning fan off")
            elif "all on" in command:
                send_command("all on")
                speak_command("Turning all components on")
            elif "all off" in command:
                send_command("all off")
                speak_command("Turning all components off")
            else:
                print("Unknown command")
                speak_command("Unknown command")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        speak_command(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("Program terminated")
    finally:
        try:
            arduino.close()
        except:
            pass
