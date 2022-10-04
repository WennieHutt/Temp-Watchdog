from smtp import message
from temperature import temp_check, time

send = 0

while True:
    temperature = temp_check()
    if len(temperature) >= 4:
        temperature = temperature[0:2]
        temperature = int(temperature)
    else:
        temperature = int(temperature)
    print(temperature)
    if temperature >= 30 and send == 0:
        message()
        send = 1 
    if temperature < 30:
        send = 0
    time.sleep(60)
    