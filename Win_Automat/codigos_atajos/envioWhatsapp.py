import pywhatkit

""" numero con codigo de pais +59895290062 """

numero_telefono = input("Ingresa el numero de telefono:")
"""pywhatkit.sendwhatmsg(numero_telefono, "mensaje Automatico", 16, 59)"""

pywhatkit.sendwhatmsg(numero_telefono, "MensajeAutomatico", 18, 54, 15, True, 2)