"""Modulo Translator"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(apikey=APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

#language_translator.set_disable_ssl_verification(True)
language_translator.set_service_url(URL)


def englishtofrench(englishtext):
    """Funcion Ingles to Frances"""
    frenchtext= language_translator.translate(englishtext,model_id='en-fr').get_result()
    frenchtext= frenchtext['translations'][0]['translation']
    return frenchtext


def frenchtoenglish(frenchtext):
    """Funcion Frances to Ingles"""
    englishtext= language_translator.translate(frenchtext, model_id='fr-en').get_result()
    englishtext= englishtext['translations'][0]['translation']
    return englishtext

#frenchText = englishToFrench('Hello')
#print (frenchText)
#englishText = frenchToEnglish('Bonjour')
#print (englishText)
