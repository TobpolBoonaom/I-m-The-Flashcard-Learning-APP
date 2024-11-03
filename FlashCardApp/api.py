import requests
from googletrans import Translator

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        if response.status_code == 200:
            word = response.json()[0]
            return word
        else:
            return None
    except Exception as e:
        print(f"Error fetching random word: {e}")
        return None

def translate_word(word, dest_language='th'):
    try:
        translator = Translator()
        translation = translator.translate(word, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Error translating word: {e}")
        return None
