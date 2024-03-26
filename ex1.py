
class CodeCesar:

    def __init__(self, cle:int):
        self.cle = cle
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def decale(self, lettre:str) -> str:
        num1 = self.alphabet.find(lettre)
        num2 = num1 + self.cle
        if num2 >= 26:
            num2 -= 26
        if num2 < 0:
            num2 += 26
        nouvelle_lettre = self.alphabet[num2]
        return nouvelle_lettre
    
    def cryptage(self, texte:str) -> str:
        crypted = ""
        for lettre in texte.upper():
            if lettre in self.alphabet:
                crypted += self.decale(lettre)
            else:
                crypted += lettre
                
        return crypted

    def transforme(self, texte):
        self.cle = -self.cle
        message = self.cryptage(texte)
        self.cle = -self.cle
        return message

# ----- 2 ------
# code1 = CodeCesar(3)
# print(code1.decale('A'))
# print(code1.decale('X'))

# print(code1.cryptage("NSI"))


# ----- 3 ------
# cle = int(input("Saisissez une clé de chiffrement: "))
# cesar = CodeCesar(cle)
# texte = input("Le texte à crypter: ").upper()
# print(cesar.cryptage(texte))


# ----- 4 ------
# print(CodeCesar(10).transforme("PSX"))
# Ça décrypte le message (FIN)
    

# ----- Coplémentaire -----
code = CodeCesar(5)
message = code.cryptage("JE SUIS TRES BEAU")
print(code.transforme(message))