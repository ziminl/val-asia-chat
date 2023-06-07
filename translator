from googletrans import Translator
korean_text = "안녕하세요"
translator = Translator()
japanese_text = translator.translate(korean_text, dest='ja').text
print(japanese_text)

romanized_text = ""

for char in japanese_text:
    if char in ["あ", "い", "う", "え", "お"]:
        romanized_text += ["a", "i", "u", "e", "o"][["あ", "い", "う", "え", "お"].index(char)]
    elif char in ["か", "き", "く", "け", "こ"]:
        romanized_text += ["ka", "ki", "ku", "ke", "ko"][["", "き", "く", "け", "こ"].index(char)]
    elif char in ["が", "ぎ", "ぐ", "げ", "ご"]:
        romanized_text += ["ga", "gi", "gu", "ge", "go"][["が", "ぎ", "ぐ","げ", "ご"].index(char)]
    elif char in ["さ", "し", "す", "せ", "そ"]:
        romanized_text += ["sa", "shi", "su", "se", "so"][["さ", "", "す", "せ", "そ"].index(char)]
    elif char in ["ざ", "じ", "ず", "ぜ", "ぞ"]:
        romanized_text += ["za", "ji", "zu", "ze", "zo"][["ざ", "じ", "ず", "ぜ", "ぞ"].index(char)]
    elif char in ["た", "ち", "つ", "て", "と"]:
        romanized_text += ["ta", "chi", "tsu", "te", "to"][["た", "ち", "つ", "て", "と"].index(char)]
    elif char in ["だ", "ぢ", "づ", "で", "ど"]:
        romanized_text += ["da", "di", "du", "de", "do"][["だ", "ぢ", "づ", "で", "ど"].index(char)]
    elif char in ["な", "に", "ぬ", "ね", "の"]:
        romanized_text += ["na", "ni", "nu", "ne", "no"][["な", "に", "ぬ", "ね", "の"].index(char)]
    elif char in ["は", "ひ", "ふ", "へ", "ほ"]:
        romanized_text += ["ha", "hi", "fu", "he", "ho"][["は", "ひ", "ふ", "へ", "ほ"].index(char)]
    elif char in ["ば", "び", "ぶ", "べ", "ぼ"]:
        romanized_text += ["ba", "bi", "bu", "be", "bo"][["ば", "び", "ぶ", "べ", "ぼ"].index(char)]
    elif char in ["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"]:
        romanized_text += ["pa", "pi", "pu", "pe", "po"][["ぱ", "ぴ", "ぷ", "ぺ", "ぽ"].index(char)]
    elif char in ["ま", "み", "む", "め", "も"]:
        romanized_text += ["", "mi", "mu", "me", "mo"][["ま", "み", "む", "め", "も"].index(char)]
    elif char in ["や", "ゆ", "よ"]:
        romanized_text += ["ya","yu", "yo"][["や", "ゆ", "よ"].index(char)]
    elif char in ["ら", "り", "る", "れ", "ろ"]:
        romanized_text += ["ra", "ri", "ru","re", "ro"][["ら", "り", "る", "れ", "ろ"].index(char)]
    elif char in ["わ", "ゐ", "ゑ", "を"]:
        romanized_text += ["wa", "wi", "we", "wo"][["わ", "ゐ", "ゑ", "を"].index(char)]
    elif char in ["ん"]:
        romanized_text += "n"
    elif char in ["っ"]:
        romanized_text += "k"

print(romanized_text)
