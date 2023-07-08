from machine import ADC, Pin
import time

BLUE = Pin(25, Pin.OUT)
BLUE.on()
A1 = ADC(Pin(27))

#5cmから開始-50cmで終了

xt = [51148, 39145, 30903, 25270, 21077, 18532, 16388, 14819, 13619, 13075, 11138]
yt = [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]

def linear(xran,yran,xa):
    a = (yran[1]-yran[0])/(xran[1]-xran[0])
    return a*(xa - xran[0]) + yran[0]

def search_ran(xspan,yspan,xa):
    for i in range(len(xspan)-1):
        if xspan[i] >= xa and xa > xspan[i+1]:
            kx = (xspan[i],xspan[i+1])
            ky = (yspan[i],yspan[i+1])
            return kx,ky
    if xspan[0] < xa:
        kx = (xspan[0],xspan[1])
        ky = (yspan[0],yspan[1])
    else:
        kx = (xspan[-2],xspan[-1])
        ky = (yspan[-2],yspan[-1])
    return kx,ky

def fit1d(xt,yt,xa):
    kx,ky = search_ran(xt,yt,xa)
    y = linear(kx,ky,xa)
    return y



while True:
    ad = A1.read_u16()
    cm = fit1d(xt,yt,ad)
    print(f"{ad}\t{cm}")
    time.sleep_ms(10)
