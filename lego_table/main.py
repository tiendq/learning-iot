import machine # type: ignore
import network # type: ignore
import esp8266_utils
import lego_table

led_red = machine.Pin(3, machine.Pin.OUT)
led_red.value(1)

ap = network.WLAN(network.AP_IF)
ap.active(False)

wifi_ini = open('wifi.ini', 'r')
ssid = wifi_ini.readline()
password = wifi_ini.readline()
wifi_ini.close()

esp8266_utils.connect_wifi(ssid.split('\n')[0], password.split('\n')[0])
esp8266_utils.sync_ntp_time()

led_red.value(0)
lego_table.start()
