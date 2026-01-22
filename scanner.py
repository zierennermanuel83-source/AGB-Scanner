# ==========================================
# PROJEKT: WELLUMINÖSER AGB-SCANNER (Master)
# VERSION: 1.1.6 - "The Life-Guardian" 🛡️
# PARTNER: Aura & Gemini
# ==========================================

def welluminoeser_master_scanner(text):
    # Die gesammelte Weisheit aus Auras Recherche (Ali, Netflix, Tech-Giganten & Lifestyle)
    datenbank = {
        # GEFAHREN (Logistik, Shopping & Tech)
        "abstellerlaubnis": (8, "Gefahr: Bei Verlust haftest du komplett selbst."),
        "bonitätsprüfung": (7, "Hintergrund-Check deiner Finanzen bei jedem Kauf."),
        "fitness-daten": (6, "App saugt Daten über deine Bewegung (Nike/Adidas)."),
        "übergabe an nachbarn": (5, "Paket gilt als zugestellt, sobald der Nachbar es hat."),
        "ki-training": (9, "Deine Eingaben machen die KI reich (OpenAI)."),
        "kontosperrung": (10, "Totalverlust deines digitalen Lebens droht."),
        "lizenz zum zugriff": (9, "Du besitzt nichts, du leihst nur (Apple/Amazon)."),
        "daten-fusion": (9, "Riesiges Super-Profil über alle Dienste (Google/Ali)."),
        "billigem ermessen": (7, "Willkürliche Preisänderungen möglich."),
        "nicht im gleichen haushalt": (8, "Passwort-Sharing Verbot."),
        "automatisierte prüfung": (10, "Deine privaten Daten werden gescannt."),
        "fahrzeugdaten": (8, "Dein Auto filmt und überwacht dich (Tesla)."),
        "mars-recht": (5, "Verrückt: Auf dem Mars gilt kein Erd-Recht (Starlink)."),
        
        # RECHTE & HILFE
        "dsa": (0, "EU-Schutzrecht: Du hast mehr Transparenz."),
        "schlichtungsstelle": (0, "Streitfälle in der EU klärbar."),
        "widerrufsrecht": (0, "14 Tage Zeit zum Zurückschicken (EU-Standard).")
    }
    
    uebersetzungen = {
        "abstellerlaubnis": "Wenn es geklaut wird, ist es dein Problem.",
        "scoring": "Wir schauen heimlich in dein Portemonnaie.",
        "health data": "Wir wissen, wie viel du läufst und wie fit du bist.",
        "indemnify": "Du zahlst die Zeche für die Firma.",
        "input": "Deine Gedanken gehören jetzt einem Algorithmus.",
        "termination at our discretion": "Wir können dich ohne Grund rausschmeißen.",
        "diagnostic data": "Wir wissen, wie schnell du fährst und wo du parkst."
    }

    text_clean = text.lower()
    treffer = []
    score_summe = 0

    print("--- 🛡️ WELLUMINÖSE ANALYSE v1.1.6 (LIFE-GUARDIAN) ---")
    
    for wort, (punkte, info) in datenbank.items():
        if wort in text_clean:
            treffer.append((wort, punkte, info))
            score_summe += punkte

    print("\n🗣️ KLARTEXT-CHECK:")
    for phrase, klartext in uebersetzungen.items():
        if phrase in text_clean:
            print(f"-> '{phrase.upper()}' BEDEUTET: {klartext}")
            
    print("\n📊 RISIKO-AUSWERTUNG:")
    if not treffer:
        print("✅ Keine bekannten Fallen gefunden. Alles im grünen Bereich!")
    else:
        gefahren_treffer = [t for t in treffer if t[1] > 0]
        if gefahren_treffer:
            score = sum(t[1] for t in gefahren_treffer) / len(gefahren_treffer)
            for t, p, i in treffer:
                prefix = "⚠️" if p > 0 else "✅"
                print(f"{prefix} [{p}/10] {t.upper()}: {i}")
            
            print(f"\nGESAMT-RESONANZ: {score:.1f} / 10")
            if score >= 8: print("🚨 FAZIT: Level IV - System-Alarm! Hohe Kontrolle.")
            elif score >= 5: print("🟡 FAZIT: Level II/III - Pass auf dich auf.")
            else: print("🔵 FAZIT: Level I - Sicherer Hafen.")

# Beispiel-Test
welluminoeser_master_scanner("Abstellerlaubnis und Scoring für KI-Training.")
