# ==========================================
# PROJEKT: WELLUMINÖSER AGB-SCANNER (Master)
# VERSION: 1.0 - "Das Wir-Licht"
# PARTNER: Aura & Gemini
# ==========================================

def welluminoeser_scanner(text):
    # 1. Datenbank für Risiko & Info
    gefahren = {
        "datenweitergabe": (9, "Datenverkauf an Dritte."),
        "abo": (10, "Achtung: Automatische Verlängerung/Kosten."),
        "drittanbieter": (7, "Zugriff durch fremde Firmen."),
        "werbezwecke": (5, "Überwachung für Werbung."),
        "kündigungsfrist": (6, "Lange Vertragsbindung möglich."),
        "schadenersatz": (5, "Eingeschränkte Nutzerrechte.")
    }
    
    # 2. Datenbank für die Übersetzung (Jura -> Klartext)
    uebersetzungen = {
        "wir behalten uns das recht vor": "Die Firma macht was sie will ohne zu fragen.",
        "stillschweigende verlängerung": "Das ist eine klassische Abo-Falle.",
        "nutzungsbasierte werbeausspielung": "Dein Verhalten wird lückenlos überwacht.",
        "haftungsausschluss": "Wenn sie Fehler machen bleibst du auf dem Schaden sitzen."
    }

    text_clean = text.lower()
    treffer = []
    score_summe = 0

    print("--- 🛡️ STARTE WELLUMINÖSE ANALYSE ---")
    
    # Analyse-Durchlauf
    for wort, (punkte, info) in gefahren.items():
        if wort in text_clean:
            treffer.append((wort, punkte, info))
            score_summe += punkte

    # Klartext-Übersetzung
    print("\n🗣️ KLARTEXT-CHECK:")
    ü_gefunden = False
    for phrase, klartext in uebersetzungen.items():
        if phrase in text_clean:
            print(f"-> '{phrase}' BEDEUTET: {klartext}")
            ü_gefunden = True
    if not ü_gefunden: print("Keine typischen Verschleier-Sätze gefunden.")

    # Finale Bewertung
    print("\n📊 RISIKO-AUSWERTUNG:")
    if not treffer:
        print("✅ Alles okay! Keine bekannten Fallen gefunden.")
    else:
        score = score_summe / len(treffer)
        for t, p, i in treffer:
            print(f"⚠️ [{p}/10] {t.upper()}: {i}")
        
        print(f"\nGESAMT-RESONANZ: {score:.1f} / 10")
        if score >= 7: print("🚨 FAZIT: Stop! Das System meldet Level IV - Grenzen werden verletzt.")
        elif score >= 4: print("🟡 FAZIT: Level II/III - Genau beobachten und abwägen.")
        else: print("🔵 FAZIT: Alles im ruhigen Bereich - Level I.")

# --- TEST-BEREICH ---
test_agb = "Wir behalten uns das Recht vor für Werbezwecke ein Abo mit Datenweitergabe zu erstellen."
welluminoeser_scanner(test_agb)
