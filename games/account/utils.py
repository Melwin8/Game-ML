from google.cloud import translate_v2 as translate
from django.conf import settings
from googletrans import Translator
from deep_translator import GoogleTranslator


def translate_text(text, target_language):
    if target_language:
        translator = GoogleTranslator(source='auto', target=target_language)
    else:
        translator = GoogleTranslator(source='auto', target='en')  # Default to English if target language is not provided

    return translator.translate(text)
