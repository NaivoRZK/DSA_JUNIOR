def recherche_dichotomique(tableau: list[int], cible: int) -> int:
    debut=0
    fin=len(tableau)-1
    while debut <= fin:
        milieu=(debut + fin) //2
        if cible == tableau[milieu]:
            return milieu
        elif cible < tableau[milieu]:
            fin=milieu -1
        else:
            debut=milieu +1
    
    return -1