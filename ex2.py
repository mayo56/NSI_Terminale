from ex1 import CodeCesar

def letter_count(texte):
    count = {}
    for lettre in texte:
        if lettre in CodeCesar(0).alphabet:
            if lettre in count.keys():
                count[lettre] += 1
            else:
                count[lettre] = 1
    return count

texte = "He quoi ? charmante Elise, vous devenez melancolique, apres les obligeantes assurances que vous avez eu la bonte de me donner de votre foi ? Je vous vois soupirer, helas ! au milieu de ma joie. Est-ce du regret, dites-moi, de m'avoir fait heureux, et vous repentez-vous de cet engagement ou mes feux ont pu vous contraindre ?"
crypted_texte = CodeCesar(3).cryptage(texte)

c = letter_count(crypted_texte)
