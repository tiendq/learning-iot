# ESP8266 NodeMCU Lua V3 CH340 LoLin wemos.cc

## Features

Đây chính là NodeMCU nổi tiếng xây dựng trên nền SoC ESP8266 WiFi. Đây là phiên bản thứ 3 và nó dựa trên ESP-12E (một module WiFi ESP8266). NodeMCU cũng là một bộ mã nguồn mở (opensource) và bộ kit phát triển giúp bạn xây dựng các ứng dụng IoT với ngôn ngữ lập trình LUA, hoặc sử dụng nó với Arduino IDE.

![Front](./ESP8266-LoLin.jpg)

![Pinout](./ESP8266-LoLin-Pinout.jpg)

Source: [ESP8266 NodeMCU Lua V3 CH340 LoLin](https://www.cytrontech.vn/p-nodemcu-lua-v3-esp8266-wifi-with-ch340c)

![LED RGB WS2812](./led-rgb-ws2812-1.jpg)

[Neopixel wiring](https://nshopvn.com/product/led-day-ws2812-phu-epoxy-5vdc-1m-144-bong/)

## Setup MicroPython

Download firmware [ESP8266](https://micropython.org/download/ESP8266_GENERIC/)

```bash
esptool.py --chip esp8266 --port /dev/tty.usbserial-110 erase_flash

esptool.py --chip esp8266 --port /dev/tty.usbserial-110 --baud 460800 write_flash --flash_size=detect 0 ESP8266_GENERIC-20240222-v1.22.2.bin
```

If the above commands run without error then MicroPython should be installed on your board!
