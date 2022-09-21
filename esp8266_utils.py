import network
import ntptime
import utime

def connect_wifi(ssid, password):
  sta_if = network.WLAN(network.STA_IF)

  if not sta_if.isconnected():
    print('Connecting to {0} network...', ssid)
    sta_if.active(True)
    sta_if.connect(ssid, password)

    while not sta_if.isconnected():
      utime.sleep_ms(500)
  print('Connected: ', sta_if.ifconfig())

# Local time is 01-01-2000 00:00:00 at boot time.
# Sync. time with NTP server to get correct local time.
def sync_ntp_time():
  ntptime.settime()
  utc_offset = 7 * 60 * 60
  now = utime.localtime(utime.time() + utc_offset)
  time_log = open('datetime.log', 'a')
  time_log.write('{0:02}-{1:02}-{2} {3:02}:{4:02}:{5:02}\n'.format(now[1], now[2], now[0], now[3], now[4], now[5]))
  time_log.close()
  return now
