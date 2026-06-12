import machine # type: ignore
import utime # type: ignore
import esp8266_utils

LED_STRIP_ON_HOUR = 16
LED_STRIP_OFF_HOUR = 17
LED_MODELS_ON_HOUR = 16
LED_MODELS_OFF_HOUR = 17

# Onboard RGB LED: Red 3, Green 4, Blue 5
led_blue = machine.Pin(5, machine.Pin.OUT)
led_strip = machine.Pin(6, machine.Pin.OUT)
led_models = machine.Pin(8, machine.Pin.OUT)

# LED strips on table sides.
def handle_led_strip(hour):
  if hour >= LED_STRIP_ON_HOUR and hour < LED_STRIP_OFF_HOUR:
    print('LED strip ON')
    led_blue.value(1)
    led_strip.value(1)
  else:
    print('LED strip OFF')
    led_blue.value(0)
    led_strip.value(0)

# Individual LEDs in LEGO models.
def handle_model_leds(hour):
  if hour >= LED_MODELS_ON_HOUR and hour < LED_MODELS_OFF_HOUR:
    print('LED models ON')
    led_blue.value(1)
    led_models.value(1)
  else:
    print('LED models OFF')
    led_blue.value(0)
    led_models.value(0)

def run(is_time_synchronized):
  is_time_ok = is_time_synchronized

  led_strip.value(0)
  led_blue.value(0)
  led_models.value(0)

  hcmc_offset = 7 * 60 * 60

  while True:
    now = utime.localtime(utime.time() + hcmc_offset)
    hour = now[3] # hour [3] minute [4]

    handle_led_strip(hour)
    handle_model_leds(hour)

    # Sync. time periodically to keep RTC works exactly.
    if not is_time_ok or hour == 23:
      is_time_ok = esp8266_utils.sync_ntp_time()

    utime.sleep(60) # seconds
