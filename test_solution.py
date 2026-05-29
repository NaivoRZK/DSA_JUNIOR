from solution import recherche_dichotomique 

def executer_tests_leetcode():
    cas_de_tests = [
        ([1, 3, 5, 7, 9, 11], 5, 2),
        ([1, 3, 5, 7, 9, 11], 1, 0),
        ([1, 3, 5, 7, 9, 11], 11, 5),
        ([1, 3, 5, 7, 9, 11], 4, -1),
        ([42], 42, 0),
        ([42], 7, -1),
        ([], 10, -1),
        ([-20, -10, 0, 5, 15], -10, 1)
    ]
    
    succes = 0
    print("=== LANCEMENT DES TESTS ===")
    
    for i, (tableau, cible, attendu) in enumerate(cas_de_tests, 1):
        resultat = recherche_dichotomique(tableau, cible)
        
        if resultat == attendu:
            print(f"SUCCES - Test {i} : Chercher {cible} dans {tableau} -> Recu {resultat}")
            succes += 1
        else:
            print(f"ECHEC - Test {i} !")
            print(f"   Tableau : {tableau}")
            print(f"   Cible cherchee : {cible}")
            print(f"   Attendu : {attendu} | Recu : {resultat}")
            print("-" * 40)
            
    print("\n=== RESULTAT FINAL ===")
    print(f"{succes}/{len(cas_de_tests)} tests reussis.")
    
    if succes == len(cas_de_tests):
        print("Bravo ! Ta solution est valide et robuste.")
    else:
        print("Attention : Il y a des erreurs. Modifie le fichier 'solution.py' et relance le test.")

if __name__ == "__main__":
    executer_tests_leetcode()