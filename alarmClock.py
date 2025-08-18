import time
import winsound  # For Windows
# For macOS/Linux, you can use: from playsound import playsound
from datetime import datetime
import threading

def set_alarm():
    """Prompt user to set alarm time"""
    print("Set the alarm time (24-hour format):")
    hour = input("Enter hour (00-23): ")
    minute = input("Enter minute (00-59): ")
    
    # Validate input
    try:
        hour = int(hour)
        minute = int(minute)
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            raise ValueError("Invalid time format")
    except ValueError:
        print("Invalid input! Please enter numbers in correct range.")
        return set_alarm()
    
    return hour, minute

def play_alarm_sound():
    """Play alarm sound"""
    try:
        # Windows sound
        frequency = 2500  # Hz
        duration = 1000  # ms
        for _ in range(5):  # Beep 5 times
            winsound.Beep(frequency, duration)
            time.sleep(0.5)
        
        # Alternative for macOS/Linux (requires playsound module)
        # playsound('alarm_sound.mp3')  # You need to have an alarm sound file
    except Exception as e:
        print(f"Error playing sound: {e}")
        print("ALARM TIME! Wake up!")

def check_alarm(alarm_hour, alarm_minute):
    """Check if current time matches alarm time"""
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        
        print(f"\rCurrent time: {now.strftime('%H:%M:%S')}", end="", flush=True)
        
        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("\nALARM TIME! Wake up!")
            play_alarm_sound()
            break
        
        time.sleep(1)  # Check every second

def main():
    print("Python Alarm Clock")
    alarm_hour, alarm_minute = set_alarm()
    
    print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")
    
    # Create a thread for the alarm check
    alarm_thread = threading.Thread(target=check_alarm, args=(alarm_hour, alarm_minute))
    alarm_thread.daemon = True
    alarm_thread.start()
    
    # Keep the main thread running
    try:
        while alarm_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAlarm cancelled")
        exit()

if __name__ == "__main__":
    main()