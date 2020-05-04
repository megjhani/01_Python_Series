
from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas.io.json import json_normalize
from ibm_watson import LanguageTranslatorV3

# Speech to Text : https://cocl.us/PY0101EN_Coursera_SpeechToText

# Language Translator : https://cocl.us/PY0101EN_Coursera_LanguageTranslator

url_s2t = "https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/cab24d61-aac8-4e69-8945-a1a3a15c2a3f"
iam_apikey_s2t = "gUtAaTtY6IrDautFM6PGlgnONP_7HvbBh-7JzC9ff8qW"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# give the file name
# open the file
filename='files/file_6_surrender.mp3' #
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
print(response.result)
json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)

##  Language Translator

url_lt='https://api.us-east.language-translator.watson.cloud.ibm.com/instances/b9f408ba-3153-4d55-9e21-22bb4083cbc0'
apikey_lt='Rv_AAL9J-Z1s5j1fcikrisAJlcEE-696MwqWn-B2rvPX'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

from pandas.io.json import json_normalize

temp_list = json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
temp_list['name']
# temp_list[temp_list['name']=='Turkish']

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation_response

translation=translation_response.get_result()
translation

spanish_translation =translation['translations'][0]['translation']
spanish_translation

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng