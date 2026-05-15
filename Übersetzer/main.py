import requests

URL = "https://translation.googleapis.com/language/translate/v2"

def translate_text(text, target_lang, API_KEY):
    params = {
        "q": text,
        "target": target_lang,
        "key": API_KEY
    }

    response = requests.post(URL, data=params)
    result = response.json()

    return result["data"]["translations"][0]["translatedText"]

print("Google Translator CLI gestartet (X = Exit)")

while True:
    api_key = input("\nAPI-Schlüssel eingeben: ")
    text = input("\nText eingeben: ")

    if text.upper() == "X":
        print("Beendet.")
        break

    lang = input("Zielsprache (z.B. de, en, fr): ")

    if lang.upper() == "X":
        print("Beendet.")
        break

    try:
        translation = translate_text(text, lang, api_key)
        print("Übersetzung:", translation)

    except Exception as e:
        print("Fehler bei der Übersetzung:", e)