# füge das oben in deine spinne.py ein um die verbindung zu aktivieren
from scanner import revolte_gegen_geschwafel, zünd_das_warnlicht

def verarbeite_agb(url):
    agb_link = suche_agb_link(url) # deine spinne sucht den link
    if agb_link:
        text = requests.get(agb_link).text # die spinne holt den inhalt
        
        # jetzt wird es welluminös:
        print("🔍 starte automatische prüfung...")
        
        # wir prüfen auf gesappel
        revolte_gegen_geschwafel(text) 
        
        # hier simulieren wir die punktzahl - wenn es zu viel ist:
        # zünd_das_warnlicht("automatischer fund") 
    else:
        print("nichts gefunden das system bleibt ruhig")


import requests
from bs4 import BeautifulSoup # das ist wie eine lupe für die spinne

def suche_agb_link(start_url):
    print(f"🕵️ suche nach der nadel im heuhaufen auf: {start_url}")
    try:
        r = requests.get(start_url)
        suppe = BeautifulSoup(r.text, 'html.parser')
        
        # die spinne schaut sich alle links (<a> tags) an
        for link in suppe.find_all('a'):
            text = str(link.string).lower()
            # fährte aufnehmen:
            if 'agb' in text or 'nutzung' in text or 'bedingungen' in text:
                ziel = link.get('href')
                print(f"🎯 fährte gefunden: {text} -> {ziel}")
                return ziel
    except Exception as e:
        print(f"⚠️ fehler beim suchen: {e}")
    return None

# test: suche_agb_link("https://www.beispielseite.de")

# deine persönliche "futter-liste"
ziel_seiten = [
    "https://www.google.de",
    "https://www.instagram.com",
    "https://www.paypal.com"
]

def starte_großreinemachen():
    for seite in ziel_seiten:
        print(f"\n--- 🧺 nächste seite wird welluminiert: {seite} ---")
        verarbeite_agb(seite)

# mit diesem befehl schickst du sie los:
# starte_großreinemachen()

# Deine erweiterten Schlagwörter für die Fährte
SCHLAGWOERTER = ['agb', 'nutzung', 'bedingungen', 'vertrag', 'kaufvertrag', 'richtlinie']

def suche_agb_link(start_url):
    print(f"🕵️ Tiefen-Scan startet auf: {start_url}")
    try:
        r = requests.get(start_url)
        suppe = BeautifulSoup(r.text, 'html.parser')
        
        for link in suppe.find_all('a'):
            # Wir machen den Text klein, damit wir alles finden
            link_text = str(link.string).lower()
            href = link.get('href')
            
            # Die Spinne prüft jetzt auf deine neuen Schlagwörter
            if any(wort in link_text for wort in SCHLAGWOERTER):
                print(f"🎯 Treffer im Versteck gefunden: {link_text} -> {href}")
                return href
    except Exception as e:
        print(f"⚠️ Fehler im Unterholz: {e}")
    return None

def tiefe_wuehl_tour(url, aktuelle_tiefe=0, max_tiefe=2):
    # bremse damit wir nicht das ganze internet scannen
    if aktuelle_tiefe > max_tiefe:
        return

    # 1. fährte aufnehmen
    link = suche_agb_link(url)
    if link:
        # 2. direkt verarbeiten (ernten und prüfen)
        verarbeite_agb(link)
        
        # 3. jetzt gehen wir eine ebene tiefer
        # die spinne schaut ob auf der neuen seite noch mehr verträge lauern
        tiefe_wuehl_tour(link, aktuelle_tiefe + 1, max_tiefe)

# ganz oben in deine spinne.py
ergebnis_liste = []

def verarbeite_agb(url):
    agb_link = suche_agb_link(url)
    if agb_link:
        text = requests.get(agb_link).text
        # wir holen uns den score vom scanner (simuliert)
        score = 8 # hier würde dein scanner-wert stehen
        
        status = "🔴 GEFAHR" if score >= 8 else "🟢 OK"
        ergebnis_liste.append(f"{status} | Seite: {url}")
        
        if score >= 8:
            zünd_das_warnlicht(f"Dreck gefunden auf {url}")

def zeige_bericht():
    print("\n--- 📋 DER WELLUMINÖSE ABSCHLUSS-BERICHT ---")
    for eintrag in ergebnis_liste:
        print(eintrag)
    print("--- ALLES DURCHGEWÜHLT ---")
