# ==========================================
# PROJEKT: WELLUMINÖSER AGB-SCANNER (Master)
# VERSION: 1.1.3 - "Der Streaming-Wächter" 🛡️
# PARTNER: Aura & Gemini
# ==========================================

def welluminoeser_master_scanner(text):
    # Die gesammelte Weisheit aus Auras Recherche (Ali & Netflix)
    datenbank = {
        # GEFAHREN (Level III - IV)
        "datenweitergabe": (9, "Datenverkauf an Dritte."),
        "unwiderrufliche lizenz": (10, "Die Firma nutzt deine Fotos/Videos ewig."),
        "schiedsverfahren": (8, "Klagen fast unmöglich (z.B. Hongkong)."),
        "schadlos halten": (10, "Du zahlst deren Anwaltskosten bei Problemen."),
        "höhere gewalt": (7, "Firma haftet für gar nichts."),
        "widerrufsrecht erlischt": (8, "Keine Rückgabe, kein Geld zurück."),
        "zahlung einbehalten": (10, "Willkürlicher Geld-Stopp möglich."),
        "daten-fusion": (9, "Riesiges Super-Profil über alle Dienste."),
        "billigem ermessen": (7, "Firma kann Preise fast willkürlich anpassen."),
        "nicht im gleichen haushalt": (8, "Passwort-Sharing Verbot: Konto-Sperre droht."),
        "keine schlichtung": (7, "Firma weigert sich an einfachen Schlichtungen teilzunehmen."),
        
        # RECHTE & HILFE (Level I - II)
        "dsa": (0, "EU-Schutzrecht: Du hast mehr Transparenz."),
        "schlichtungsstelle": (0, "Streitfälle in der EU klärbar."),
        "pünktlichkeitsgarantie": (0, "Geld zurück wenn es zu spät kommt."),
        "kostenlose rückgabe": (0, "Sicherer Hafen für deine Retoure.")
    }
    
    uebersetzungen = {
        "weltweite lizenz": "Du bist ihr kostenloser Werbestar.",
        "indemnify": "Du bist die Versicherung für die Firma.",
        "hong kong": "Recht haben heißt hier nicht Recht bekommen.",
        "erlischt das widerrufsrecht": "Geld weg, Ware behalten - Pech.",
        "deemed acceptance": "Einmal geklickt und du bist gefangen.",
        "dispute": "Du hast nur 15 Tage Zeit, sonst ist dein Geld weg.",
        "dsa": "Das EU-Gesetz, das dich schützt.",
        "billigem ermessen": "Wir machen den Preis wie wir ihn brauchen.",
        "nicht übertragbares recht": "Nur du darfst gucken, niemand sonst.",
        "automatisch bis zu ihrer kündigung": "Die Bezahl-Maschine stoppt nie von allein."
    }

    text_clean = text.lower()
    treffer = []
    score_summe = 0

    print("--- 🛡️ WELLUMINÖSE ANALYSE v1.1.3 ---")
    
    for wort, (punkte, info) in datenbank.items():
        if wort in text_clean:
            treffer.append((wort, punkte, info))
            score_summe += punkte

    print("\n🗣️ KLARTEXT-CHECK:")
    for phrase, klartext in uebersetzungen.items():
        if phrase in text_clean:
            print(f"-> '{phrase}' BEDEUTET: {klartext}")
            
    print("\n📊 RISIKO-AUSWERTUNG:")
    if not treffer:
        print("✅ Keine bekannten Fallen gefunden. Schwingt neutral.")
    else:
        gefahren_treffer = [t for t in treffer if t[1] > 0]
        if gefahren_treffer:
            score = sum(t[1] for t in gefahren_treffer) / len(gefahren_treffer)
            for t, p, i in treffer:
                prefix = "⚠️" if p > 0 else "✅"
                print(f"{prefix} [{p}/10] {t.upper()}: {i}")
            
            print(f"\nGESAMT-RESONANZ: {score:.1f} / 10")
            if score >= 8: print("🚨 FAZIT: Level IV - System-Alarm! Grenzen werden massiv verletzt.")
            elif score >= 5: print("🟡 FAZIT: Level II/III - Hohes Risiko, bleib wachsam.")
            else: print("🔵 FAZIT: Level I - Akzeptabel.")
        else:
            print("💎 FAZIT: Nur positive Rechte gefunden. Sehr gut!")

# Test mit Netflix-Klausel
welluminoeser_master_scanner("Abo läuft automatisch bis zur Kündigung nach billigem Ermessen.")
