import RPi.GPIO as GPIO
import tkinter as tk
#Ehsen Tahir
# GPIO pins for LEDs
WHITE_PIN = 17  
GREEN_PIN = 18
BLUE_PIN = 27

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(WHITE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Setup PWM for each LED
WHITE_PWM = GPIO.PWM(WHITE_PIN, 100)  # Frequency set to 100 Hz
GREEN_PWM = GPIO.PWM(GREEN_PIN, 100)
BLUE_PWM = GPIO.PWM(BLUE_PIN, 100)

# Initialize PWM duty cycle
WHITE_PWM.start(0)
GREEN_PWM.start(0)
BLUE_PWM.start(0)

# Function to set intensity of a specific LED
def set_intensity(led_pwm, duty_cycle):
    led_pwm.ChangeDutyCycle(duty_cycle)

# Function to handle slider movement
def handle_slider(led_pwm, slider_value):
    set_intensity(led_pwm, int(slider_value))

# Create GUI
root = tk.Tk()
root.title("LED Controller")

# Slider for white LED
white_label = tk.Label(root, text="White")
white_label.pack()
white_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: handle_slider(WHITE_PWM, value))
white_slider.pack()

# Slider for green LED
green_label = tk.Label(root, text="Green")
green_label.pack()
green_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: handle_slider(GREEN_PWM, value))
green_slider.pack()

# Slider for blue LED
blue_label = tk.Label(root, text="Blue")
blue_label.pack()
blue_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: handle_slider(BLUE_PWM, value))
blue_slider.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Run the GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
