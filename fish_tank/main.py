import machine # type: ignore
import network # type: ignore
import env
import esp8266_utils
import fish_tank

led_onboard = machine.Pin(2, machine.Pin.OUT)
led_onboard.value(0) # on

ap = network.WLAN(network.AP_IF)
ap.active(False)

esp8266_utils.connect_wifi(env.WIFI_SSID, env.WIFI_PASSWORD)
esp8266_utils.sync_ntp_time()

led_onboard.value(1) # off
fish_tank.run()
