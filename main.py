a = int(input())

if a < 0:
    print("impossível!")
elif a < 18 and a != 0:
    print("não precisa se alistar.")
elif a >= 18 and a < 65:
    print("Não esqueça de votar na próxima eleição.")
elif a >= 65:
    print("Vá descançar.")
else:
    print("eita!")
