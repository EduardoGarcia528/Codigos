"""
Ejercicios finales
Eduardo Garcia Castrejón
Fisica 1A
Programa 1
PALINDROMO
"""
n = 1
while n == 1:
    punctuation = "#$%&'()*+, ´'-./°¬:;<!=>?@[\]“”^_`{|}~\""
    tildes = "áéíóú"
    vocales = "aeiou"
    b = list(punctuation)
    a = input("Itroduce una frase: ")
    c = a.lower()
    f = list(c)
    for x in range(0,len(b)):
        while b[x] in f:
            f.remove(b[x])
    final = "".join(f)

    for x in range(0,5):
        final = final.replace(tildes[x],vocales[x])


    l = list(final)
    l.reverse()
    p = "".join(l)

    if p == final:
        print("Es palindromo")
    else:
        print("No es palindromo")
    m = input("ENTER para volver a analizar\n'1' para finalizar\n")
    if m == "1":
        n = 2