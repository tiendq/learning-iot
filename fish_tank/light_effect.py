import utime # type: ignore

# Input a value 0 to 255 to get a color value.
# The colours are a transition r - g - b - back to r.
# Ref: https://bhave.sh/micropython-neopixels-1/
def get_wheel_color(index):
  if index < 0 or index > 255:
    return (0, 0, 0)

  if index < 85:
    return (255 - index * 3, index * 3, 0)

  if index < 170:
    index -= 85
    return (0, 255 - index * 3, index * 3)

  index -= 170
  return (index * 3, 0, 255 - index * 3)

# Making cycling rainbow effect.
def make_rainbow_cycle(pixels, delay_ms):
  for j in range(255):
    for i in range(len(pixels)):
      color = (i * 256 // len(pixels)) + j
      pixels[i] = get_wheel_color(color & 255)

    pixels.write()
    utime.sleep_ms(delay_ms)

def turn_light_on(pixels, delay_ms):
  step = 5
  brightness = 0

  while brightness < 225:
    brightness = brightness + step

    for i in range(len(pixels)):
      pixels[i] = (brightness, brightness, brightness)

    pixels.write()
    utime.sleep_ms(delay_ms)

def turn_light_off(pixels, delay_ms):
  step = 5
  brightness = 225

  while brightness > 0:
    brightness = brightness - step

    for i in range(len(pixels)):
      pixels[i] = (brightness, brightness, brightness)

    pixels.write()
    utime.sleep_ms(delay_ms)

def clear_pixels(pixels):
  for i in range(len(pixels)):
    pixels[i] = (0, 0, 0)
  pixels.write()

def turn_on_white(pixels, brightness = 225):
  for i in range(len(pixels)):
    pixels[i] = (brightness, brightness, brightness)
  pixels.write()

def turn_sunlight_on(pixels):
    for i in range(len(pixels)):
      pixels[i] = (244, 233, 155)
    pixels.write()

def turn_sunlight_off(pixels):
    for i in range(len(pixels)):
      pixels[i] = (0, 0, 0)
    pixels.write()
