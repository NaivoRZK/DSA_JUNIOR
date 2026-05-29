# 704. Recherche Dichotomique (Binary Search)

## Énoncé
Étant donné un tableau d'entiers `tableau` trié par ordre croissant et un entier `cible`, écris une fonction pour chercher `cible` dans `tableau`. Si `cible` existe, retourne son index. Sinon, retourne `-1`.

Tu dois écrire un algorithme avec une complexité temporelle de $O(\log n)$.

---

## Exemples

### Exemple 1
**Entrée :** `tableau = [-1, 0, 3, 5, 9, 12]`, `cible = 9`  
**Sortie :** `4`  
**Explication :** 9 existe dans le tableau et son index est 4.

### Exemple 2
**Entrée :** `tableau = [-1, 0, 3, 5, 9, 12]`, `cible = 2`  
**Sortie :** `-1`  
**Explication :** 2 n'existe pas dans le tableau, donc on retourne -1.

---

## Contraintes
* `1 <= len(tableau) <= 10^4`
* `-10^4 < tableau[i], cible < 10^4`
* Tous les entiers dans `tableau` sont uniques.
* `tableau` est trié par ordre croissant.

---

## Prototype de la fonction
```python
def recherche_dichotomique(tableau: list[int], cible: int) -> int:
    # Écris ton code ici
    pass