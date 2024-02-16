"""Aufgabe:

Erstellen Sie ein Python-Skript, dass - eventuell neben einer kurzen print()-Anweisung - nur
aus dem Aufruf exit() besteht.

Übergeben Sie nun einige numerische Werte an exit() und überprüfen Sie den Wert von exit() wenn
der Python beendet wird mit in der cmd bzw. in der PowerShell.


- Den Rückgabewert eines Programms kann man in der cmd mit dem Kommando:

echo %ERRORLEVEL%

messen.

- In der PowerShell kann man den exit-Wert eines Programms mit dem Kommando:

echo $?

messen.


Führen Sie die Aufgabe ergänzend/alternativ direkt mit dem Python interpreter aus."""

print("Aufgabe exit-Codes")
#exit()                          # PS: True  CMD:  0
#exit(0)                         # PS: True  CMD:  0
#exit(1)                         # PS: False CMD:  1
#exit(-1)                        # PS: False CMD: -1
#exit(100)                       # PS: False CMD:100