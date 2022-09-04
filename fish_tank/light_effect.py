import utime

def wheel(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

# Moving rainbow effect.
def rainbow_cycle(pixels, delay_ms):
  for j in range(255):
    for i in range(pixels.__len__):
      rc_index = (i * 256 // pixels.__len__) + j
      pixels[i] = wheel(rc_index & 255)
    pixels.write()
    utime.sleep_ms(delay_ms)
