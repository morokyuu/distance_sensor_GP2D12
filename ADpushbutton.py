from machine import ADC, Pin
import time

D3 = Pin(29, Pin.IN, Pin.PULL_UP)
BLUE = Pin(25, Pin.OUT)
A1 = ADC(Pin(27))

#button push -> AD value will be printed

count = 0
while True:
    if D3.value() == 0:
        ad = A1.read_u16()
        print(f"{count}\t{ad}")
        BLUE.on()
        time.sleep(2)
        BLUE.off()
        count += 1
    time.sleep_ms(10)