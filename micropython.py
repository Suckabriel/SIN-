from microbit import*
import random
import radio

radio.on()
radio.config(channel = 12)
radio.config(address = 0x75626974)
radio.config(group = 2)
radio.config(power = 7)

pierre = Image("00900:"
               "09990:"
               "99999:"
               "09990:"
               "00900:")
feuille = Image("99900:"
                "90090:"
                "90009:"
                "90009:"
                "99999:")
ciseau = Image("99009:"
               "99090:"
               "00900:"
               "99090:"
               "99009:")
debut= [pierre,feuille,ciseau]
display.show(debut, delay=400)
display.scroll('start')
resultat = None

nbmanche = 0
while True:
    if  button_a.is_pressed():
        display.clear()
        nbSecousses = 0
        tirage = random.randint(1,3)
        while nbSecousses != 4:
            if accelerometer.was_gesture("shake"):
                nbSecousses = nbSecousses + 1
                display.show(str(nbSecousses))
        if tirage == 1:
            display.show(pierre)
            radio.send("1")
        if tirage == 2:
            display.show(feuille)
            radio.send("2")
        if tirage == 3:
            display.show(ciseau)
            radio.send("3")
        sleep(1000)
        nbmanche = nbmanche +1
        display.show(nbmanche)
        sleep(1500)
       
        while resultat is None :
            resultat= radio.receive()

        display.scroll(resultat)
