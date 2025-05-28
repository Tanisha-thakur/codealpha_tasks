from googletrans import Translator

def translate_text(text, src_lang='auto', dest_lang='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("=== Language Translator ===")
    source_text = input("Enter text to translate: ")
    source_language = input("Enter source language code (or leave blank for auto): ") or 'auto'
    target_language = input("Enter target language code (e.g., 'fr' for French): ")

    result = translate_text(source_text, source_language, target_language)
    print(f"\nTranslated Text: {result}")
