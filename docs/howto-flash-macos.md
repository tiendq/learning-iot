# How to install MicroPython on ESP8266 from macOS M1

## Hardware

- Macbook Pro M1 (2020) with macOS Big Sur (11.1)
- NodeMCU Lua V3 ESP8266 (model: ESP-12E, vendor: DOITING), board made by LOL1n.

## Instruction

### 1. Install USB to serial driver

Since this board uses CH340 chip then it needs `CH341SER_MAC.ZIP` from [this page](http://www.wch-ic.com/downloads/CH341SER_MAC_ZIP.html).

Unzip and follow instructions in the included PDF file and restart macOS.

After the system is restarted, connect ESP8266 to your laptop (a MBP in this case, I used a USB 3.0 to USB-C adapter) and check to see what USB serial port name is.

```bash
ls /dev/tty*

# output will be a long list of tty*, then you should easily identify a USB serial port by its unique name,
# /dev/tty.usbserial-110 in this case

/dev/tty
/dev/tty.Bluetooth-Incoming-Port
/dev/tty.debug-console
/dev/tty.usbserial-110
/dev/tty.wlan-debug
...
```

### 2. Get MicroPython firmware

Follow guidelines on [MicroPython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#getting-the-firmware), a stable firmware file will be something like this `esp8266-1m-20220618-v1.19.1.bin`.

### 3. Deploy MicroPython firmware

Install `esptool` to copy firmware to the board `pip3 install esptool`.

Erase the current flash using:

```bash
esptool.py --port /dev/tty.usbserial-110 erase_flash

# expected output
esptool.py v4.2.1
Serial port /dev/tty.usbserial-110
Connecting....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: 48:3f:da:9e:32:b1
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 17.7s
Hard resetting via RTS pin...
```

And then deploy the new firmware using:

```bash
esptool.py --port /dev/tty.usbserial-110 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20220618-v1.19.1.bin

# expected output
esptool.py v4.2.1
Serial port /dev/tty.usbserial-110
Connecting....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting....
Detecting chip type... ESP8266
Chip is ESP8266EX
Features: WiFi
Crystal is 26MHz
MAC: 48:3f:da:9e:32:b1
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Flash will be erased from 0x00000000 to 0x00090fff...
Flash params set to 0x0040
Compressed 591476 bytes to 392427...
Wrote 591476 bytes (392427 compressed) at 0x00000000 in 10.4 seconds (effective 456.5 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

If the above commands run without error then MicroPython should be installed on your board!

### 4. Tests

`screen /dev/tty.usbserial-110 115200`, then press Enter once and you should see REPL promt as `>>>`.

You also see new Wi-Fi network named `MicroPython-xxxxxx`.

Helpful `screen` commands in case you cannot connect to REPL, thanks to [TimNode](https://superuser.com/a/1345071/149213).

```bash
screen -ls # list all screen sessions
screen -XS 4581 quit # kill a screen sessions
```
