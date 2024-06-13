import RPi.GPIO as GPIO
import time

FAN_PIN = 18

TEMP_THRESHOLD = 45

def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return float(temp) / 1000


GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

try:
    while True:
        temp = get_cpu_temperature()
        print(f"CPU Temp: {temp} °C")
        if temp > TEMP_THRESHOLD:
            GPIO.output(FAN_PIN, GPIO.HIGH)  # Turn the fan on
            print("Fan ON")
        else:
            GPIO.output(FAN_PIN, GPIO.LOW)   # Turn the fan off
            print("Fan OFF")
        time.sleep(15)  
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
