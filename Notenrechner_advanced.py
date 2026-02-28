# Listen für Noten
tests = []
klassenarbeiten = []

# Schritt 1: Verteilung auswählen
print("Wähle die Verteilung aus:")
print("1 - 30% Tests / 70% Klassenarbeiten")
print("2 - 40% Tests / 60% Klassenarbeiten")
print("3 - 50% Tests / 50% Klassenarbeiten")


wahl = input("Gib 1, 2 oder 3 ein: ")

if wahl == "1":
    gewicht_tests = 0.3
    gewicht_ka = 0.7
    gewichtstext = "30% 70%"
elif wahl == "2":
    gewicht_tests = 0.4
    gewicht_ka = 0.6
    gewichtstext = "40% 60%"
elif wahl == "3":
    gewicht_tests = 0.5
    gewicht_ka = 0.5
    gewichtstext = "50% 50%"
else:
    print("Ungültige Wahl, Standard: 50/50")
    gewicht_tests = 0.5
    gewicht_ka = 0.5

# Schritt 2: Noten eingeben
anzahl_tests = int(input("Wie viele Tests hattest du? "))
for i in range(anzahl_tests):
    note = float(input(f"Note Test {i+1}: "))
    tests.append(note)

anzahl_ka = int(input("Wie viele Klassenarbeiten hattest du? "))
for i in range(anzahl_ka):
    note = float(input(f"Note Klassenarbeit {i+1}: "))
    klassenarbeiten.append(note)

# Schritt 3: Durchschnitt pro Kategorie berechnen
durchschnitt_tests = sum(tests) / len(tests) if tests else 0
durchschnitt_ka = sum(klassenarbeiten) / len(klassenarbeiten) if klassenarbeiten else 0

# Schritt 4: Gewichteten Durchschnitt berechnen
endnote = durchschnitt_tests * gewicht_tests + durchschnitt_ka * gewicht_ka

print(f"Dein Notendurchschnitt liegt bei:", round(endnote, 2))
print(f"Du hattest die Aufteilung:{gewichtstext}")
