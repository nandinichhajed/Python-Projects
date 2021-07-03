from translate import Translator

translator = Translator(to_lang='ja')
# we can change language here based on the documantation

try:
    with open(r"File Path", 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('test-ja.txt', 'w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
# the encoding is changed to UTF-8 when using the file, so characters in UTF-8 are able to be converted to text, instead of returning an error when it encounters a UTF-8 character that is not suppord by the current encoding.

except FileNotFoundError as e:
    print('check your file path')
