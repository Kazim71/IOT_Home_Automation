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
        # Adjust microphone settings
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.energy_threshold = 300  # Adjust based on environment
        print("Listening... Please speak into the laptop's microphone.")
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""
        except sr.UnknownValueError:
            print("Could not understand the audio")
            speak_command("Could not understand the audio")
            return ""
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
        # Replace 'COM5' with the appropriate port for your system
        arduino = serial.Serial('COM5', 9600, timeout=1)
        time.sleep(2)  # Give time for the connection to establish

        while True:
            command = recognize_speech()
            if command:
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
      