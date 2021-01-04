"""
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:
1, 1, 2, 3, 5, 8, 13 (...)
Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.
"""

def serieFibonacci(num):
    if (num == 0):
        return 0 #returno 0 perché la somma dei due numeri prima è 0
    else:
        if(num == 1):
            return 1 #returno 1 perché la somma dei due numeri prima (0+1)=1
        else:
            return (serieFibonacci(num - 1) + serieFibonacci(num - 2)


#x = input ("Test:")

x = int(input("Inserisci un numero che mostri fino a quel numero la serie (il numero deve essere >=0)\nNumero: "))      #mi dà come errore invalid syntax nonostante sia tutto giusto

for cnt in range (x):
    print(serieFibonacci(cnt))