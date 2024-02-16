# Das ist ein Kommentar

a = 100                                 # Deklaration und Wertzuweisung der Variablen a mit dem Wert 100

# Ausgabe der Variablen a mit der Funktion print()
print(a)

# Die print()-Funktion kann zur gleichen Zeit auchg mehrere Parameter übernehmen, diese
# werden dann durch ein Komma voneinander getrennt. Hier geben wir im Weiteren einen 
# String zur Ausgabe und dann den Wert von a aus.
print("Der Wert von a ist: ", a)

# a erhält einen neuen Wert. Die Zahl links vom Gleichheitszeichen bedeutet der Wert und das 
# selbst ist der sog. Zuweisungsoperator, d.h. der Wert rechts von = wird der Speicherstelle
a = -10
print("a nach neuer Zuweisung:", a)

# Wir stellen eine neue Variable: n bereit
n = 0xab3               # Zuweisung einer Hexadezimalzahl
print("n:", n)

# Python ist Case-Sensitive. Die Variable N ist eine andere als n.
N = 0b1010              # Zuweisung einer Binärzahl 0b <=> Binär
print("N:", N)

# Eine int-Variable als Oktalzahlliteral angegeben
oct_num = 0o10          # 8(10) <=> 10(8)
print("Die Oktalzahl 0o10: ", oct_num)

# Den Typ einer Variablen kann man mit der Funktion type() messen.
print("Der Typ von: a ist:", type(a))
print("Der Typ von: n ist:", type(n))
print("Der Typ von: N ist:", type(N))
print("Der Typ von: oct_num ist:", type(oct_num))

# => Alles Objekte vom Typ/der Klasse int

# Mit der FUnktion dir() kann man sich die Attribute/Methoden anzeigen lassen.
print("dir(a):", dir(a))

# Neben den oben zugewiesenen sog. Literalen kann man auch die Funktion int() nutzen.
n = int()

print()
print("n = int() =>", n)

n = int(-900)
print()
print("n = int(-900) =>", n)

# Wenn man an int() eine Binärzahl abgeben will, muss dies der Funktion int im Rahmen eines zweiten Parameters mitgeteilt werden, ferner muss dann der erste Parameter als String angegeben werden.
n = int("110101", 2)
print('n = int("110101"),2 => ', n)

# Ein Integer wird immer im 10er-System dargestellt. Wenn man die Darstellung bezüglich einem anderen System haben möchte, nutzt man dafür entsprechende Funktionen.
print("") 
