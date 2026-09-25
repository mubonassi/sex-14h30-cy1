print("| TYPING CLUB DA SHOPEE |")
print("-"*60)

palavras = ["oi","bom","pão","uvas","xbox","playstation","nintendo switch","paralelepípedo","televisão"]

print("**Digite corretamente as palavras abaixo**")

acertos = 0
erros = 0
for palavra in palavras:
    print(f"-- Palavra: {palavra} --")
    tentativa = input("> Digite aqui a palavra: ")
    if tentativa == palavra:
        print("!!Você acertou!!")
        acertos += 1
    else:
        print("!Você errou!")
        erros += 1

print("- CONCLUSÃO -")
print(f">>> Acertos: {acertos}")
print(f">>> Erros: {erros}")

if erros == 0:
    print("VOCÊ ACERTOU TODOS! PARABÉNS!")
elif acertos == 0:
    print("Você acertou nenhum! Pode treinar mais!")
else:
    print("Parabéns! Agora tente não errar nenhuma!")