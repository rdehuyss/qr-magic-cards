from httpclient import HttpClient
import machine, network, time


uart_qr = machine.UART(1, baudrate=9600, bits=8, parity=None, stop=1, rx=22, tx=19, timeout=50)
pinTrig = machine.Pin(23, machine.Pin.OUT)
pinDled = machine.Pin(33, machine.Pin.IN)
pinBtn = machine.Pin(39, machine.Pin.IN)

pinTrig.value(1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect('Sint-Truidensesteenweg 70', 'internetisvaniedereen')
    while not wlan.isconnected():
        time.sleep_ms(50)
        pass
print('Connected to network (', wlan.ifconfig(), ')')


print('Starting QR Code reading')
h = HttpClient()
while True:
    time.sleep_ms(200)

    if pinBtn.value() == 0:
        print('Button Pressed')
        pinTrig.value(0)
    else:
        pinTrig.value(1)

    if uart_qr.any() > 0:
        query_url = uart_qr.readline().decode('ascii').replace('\r', '').replace('\n', '')
        url = 'http://192.168.1.250:6005/office' + query_url
        resp = h.get(url)
        print('{} -> status: {}'.format(url, resp.status_code))