from tkinter import *
import tkinter.font 
from gpiozero import PWMLED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# LEDs setup using PWM
ledBlue = PWMLED(17)
ledRed = PWMLED(27)
ledYellow = PWMLED(22)

# Main window setup
win = Tk()
win.title("3 RADIO LED")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Control variable for the radio buttons and slider
led_control = StringVar(value="None")
intensity = DoubleVar(value=0.5)  # Default intensity at 50%

def updateLEDs():
    # Turn off all LEDs first
    ledBlue.value = 0
    ledRed.value = 0
    ledYellow.value = 0

    # Turn on selected LED with current intensity
    if led_control.get() == "Blue":
        ledBlue.value = intensity.get()
    elif led_control.get() == "Red":
        ledRed.value = intensity.get()
    elif led_control.get() == "Yellow":
        ledYellow.value = intensity.get()

def close():
    ledBlue.off()
    ledRed.off()
    ledYellow.off()
    RPi.GPIO.cleanup()
    win.destroy()

# Radio Buttons
blueButton = Radiobutton(win, text="Turn Blue LED On", variable=led_control, value="Blue", command=updateLEDs, font=myFont, bg='blue', height=1, width=24)
redButton = Radiobutton(win, text="Turn Red LED On", variable=led_control, value="Red", command=updateLEDs, font=myFont, bg='red', height=1, width=24)
yellowButton = Radiobutton(win, text="Turn Yellow LED On", variable=led_control, value="Yellow", command=updateLEDs, font=myFont, bg='yellow', height=1, width=24)

# Slider for controlling the intensity
intensitySlider = Scale(win, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, label="Intensity", variable=intensity, command=lambda x: updateLEDs(), font=myFont)
intensitySlider.grid(row=4, column=0, sticky="we")

# Exit Button
exitButton = Button(win, text="Exit", font=myFont, command=close, bg='black', height=1, width=10)
exitButton.grid(row=5, column=0)

# Button layout
blueButton.grid(row=0, column=0)
redButton.grid(row=1, column=0)
yellowButton.grid(row=2, column=0)

win.mainloop()

