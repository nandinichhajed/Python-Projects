from translate import Translator

translator = Translator(from_lang='en', to_lang='ja')
translation = translator.translate(input("Enter the sentence: "))
print(translation)