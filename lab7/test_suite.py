# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git

import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
LED_PIN = 11
GPIO.setup(LED_PIN, GPIO.OUT)

# Hardware SPI configuration
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# ADC channels
LIGHT_CHANNEL = 0
SOUND_CHANNEL = 1

# Thresholds (tune these from experimentation)
lux_threshold  = 200   # below = dark, above = bright
sound_threshold = 400  # above = tap detected


# --- Helper functions ---

def blink_led(times, interval_ms):
    """Blink LED a given number of times with on/off interval in ms."""
    interval_s = interval_ms / 1000.0
    for _ in range(times):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(interval_s)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(interval_s)


def read_light_sensor():
    """Return raw ADC value from the light sensor."""
    return mcp.read_adc(LIGHT_CHANNEL)


def read_sound_sensor():
    """Return raw ADC value from the sound sensor."""
    return mcp.read_adc(SOUND_CHANNEL)


def is_bright(value):
    return value > lux_threshold


def is_loud(value):
    return value > sound_threshold


# --- Main test loop ---

try:
    while True:

        # Step 1: Blink LED 5 times, 500ms on/off
        print("=== Step 1: Blinking LED 5x (500ms) ===")
        blink_led(5, 500)

        # Step 2: Read light sensor for ~5 seconds at 100ms intervals
        print("=== Step 2: Reading light sensor for 5s ===")
        start = time.time()
        while time.time() - start < 5.0:
            val = read_light_sensor()
            label = "bright" if is_bright(val) else "dark"
            print(f"Light: {val} -> {label}")
            time.sleep(0.1)

        # Step 3: Blink LED 4 times, 200ms on/off
        print("=== Step 3: Blinking LED 4x (200ms) ===")
        blink_led(4, 200)

        # Step 4: Read sound sensor for ~5 seconds at 100ms intervals
        # LED turns on for 100ms on tap, but does NOT pause the sampling loop
        print("=== Step 4: Reading sound sensor for 5s ===")
        start = time.time()
        while time.time() - start < 5.0:
            val = read_sound_sensor()
            print(f"Sound: {val}")
            if is_loud(val):
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(LED_PIN, GPIO.LOW)
                # Don't sleep again — keep the 100ms cadence
            else:
                time.sleep(0.1)

except KeyboardInterrupt:
    print("\nInterrupted. Cleaning up GPIO.")
finally:
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
