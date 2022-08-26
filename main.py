from binary_tree import BinaryTree
from morse_code import morse

# Alimentando a arvore com o 'conjunto de dados' vindo do dicionário morse
print(f"Alimentando a árvore com {len(morse.items())} letras.")
root = BinaryTree("start")
for k, v in morse.items():
    root.push(k, v)

# Traducao
codigos = [
    "... --- ...",
    "-.-. .- ... .-",
    "- . ... - .   .----",
    "-.-. .-. .. ... - .. .- -. ---",
    ".--. .--. --. .. .-   .--. ..- -.-. .--. .-."
]

for codigo in codigos:
    print(f"Traduzindo o termo {codigo}")

    translated_sentence = ""
    for phrase in codigo.split("   "):
        for word in phrase.split(" "):
            translated_sentence += root.find(word)
        translated_sentence += " "

    print(translated_sentence)


