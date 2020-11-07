"""
void bubble_sort(int list[], long n)
{
  long j, k, t;

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
"""
lista = [5, 9, 2, 6, 1, 55, 74, 4, 8, 45]
print (lista)
t = k = j = 0

for j,k in enumerate(lista):
    if lista[k] > lista[k+1]:
        #cambio
        t = lista[k]
        lista[k] = lista[k+1]
        lista[k+1] = t

print (lista)
"""

lista = [5, 9, 2, 6, 1, 55, 74, 4, 8, 45]
print (lista)
t = k = j = 0
n = len(lista)
for j in range(n-1):
    for k in range(n-j-1):
        if lista[k] > lista[k+1]:
            #cambio
            t = lista[k]
            lista[k] = lista[k+1]
            lista[k+1] = t

print (lista)
