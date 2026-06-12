import network # type: ignore
import ntptime # type: ignore
import utime # type: ignore

ntptime.host = 'time.google.com'
ntptime.timeout = 10

def connect_wifi(ssid, password):
  sta_if = network.WLAN(network.STA_IF)

  print('Connecting to network', ssid, '...')

  if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(ssid, password)

    while not sta_if.isconnected():
      utime.sleep(15)

  print('Connected at', sta_if.ifconfig())

# Local time is 01-01-2000 00:00:00 at boot time.
# Sync. time with NTP server to get correct local time.
def sync_ntp_time():
  try:
    ntptime.settime()
  except OSError as error:
    print('Time synchronization fails: ', error.args[0]) # 116 ETIMEDOUT
    return False
  except:
    print('Time synchronization fails')
    return False

  hcmc_offset = 7 * 60 * 60
  now = utime.localtime(utime.time() + hcmc_offset)

  print('Synchronized time, local time is ', now)
  return True
