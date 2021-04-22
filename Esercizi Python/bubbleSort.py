"""
void bubble_sort(int list[], int n)
{
  int j, k, t;

  for (j = 0 ; j < n - 1; j++) {
    for (k = 0 ; k < n - j - 1; k++) {
      if (list[k] > list[k+1]) {
        /* Cambio */
        t = list[k];
        list[k] = list[k+1];
        list[k+1] = t;
      }
    }
  }
}
"""

lista = [5, 9, 2, 6, 1, 55, 74, 4, 8, 45]
print (lista)

for indice1,elemento1 in enumerate(lista):
  for indice2,elemento2 in enumerate(lista[:len(lista)-indice1]):
    if elemento1 > elemento2:
      #lista[indice1], lista[indice2] = lista[indice2], lista[indice1]
      """
      elemento1, elemento2 = elemento2, elemento1
      lista1[indice1] = elemento1
      lista1[indice2] = elemento2
      """
      #lista[k], lista[k+1] = lista[k+1], lista[k]   #scambio

print (lista)

"""
lista = [5, 9, 2, 6.6, 1, 55.5, 74, 4, 8, 45]
print (lista)
n = len(lista)
for j in range(n-1):            #parto da 0 e vado fino a n-1 (escluso)
    for k in range(n-j-1):      #parto da 0 e vado fino a n-j-1 (escluso)
        if lista[k] > lista[k+1]:
            lista[k], lista[k+1] = lista[k+1], lista[k]   #scambio

print (lista) 
"""
