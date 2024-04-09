import machine # type: ignore
import utime # type: ignore
import esp8266_utils

LED_ON_HOUR = 19
LED_OFF_HOUR = 21

is_led_on = False
led_green = machine.Pin(4, machine.Pin.OUT)
led_switch = machine.Pin(10, machine.Pin.OUT)

def handle_led_strip(hour):
  global is_led_on

  if hour >= LED_ON_HOUR and hour <= LED_OFF_HOUR:
    if not is_led_on:
      is_led_on = True
      led_green.value(1)
      led_switch.value(1)
  else:
    if is_led_on:
      is_led_on = False
      led_green.value(0)
      led_switch.value(0)

def start():
  utc_offset = 7 * 60 * 60 # production mode 7 * 60 * 60

  while True:
    now = utime.localtime(utime.time() + utc_offset)
    handle_led_strip(now[3])

    if now[3] % 10 == 0:
      esp8266_utils.sync_ntp_time() # synchronize time periodically to keep RTC works exactly

    utime.sleep(60)
