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
