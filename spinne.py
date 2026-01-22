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
