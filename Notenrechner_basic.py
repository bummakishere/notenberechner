
noten = []
print("\033[34mSchreibe deine Noten ein, wenn alle eingetragen sind drücke Gleich\033[0m")
while True:
    eingabe = input("\033[32mNote eingeben:\033[0m ")
    
    if eingabe.lower() == "=":
        break
    
    note = float(eingabe)
    noten.append(note)

durchschnitt = sum(noten) / len(noten)

print("\033[33mDein Notendurchschnitt ist:\033[0m", round(durchschnitt, 2))