import machine # type: ignore
import network # type: ignore
import env
import esp8266_utils
import lego_table

led_red = machine.Pin(3, machine.Pin.OUT)
led_red.value(1)

ap = network.WLAN(network.AP_IF)
ap.active(False)

esp8266_utils.connect_wifi(env.WIFI_SSID, env.WIFI_PASSWORD)
esp8266_utils.sync_ntp_time()

led_red.value(0)
lego_table.run()
