class Noeud:
    def __init__(self,donne):
        self.donne=donne
        self.suivant=None
#   ma_neoud=Noeud(10)

class ListeChaine:
    def __init__(self):
        self.tete=None

    #Ajouter un élément dans le chaine
    def ajouterElementFin(self, donne):
        nouveau_noeud = Noeud(donne)
        if self.tete is None:
            self.tete = nouveau_noeud
            return

        courant = self.tete
        while courant.suivant is not None:
            courant=courant.suivant
        courant.suivant=nouveau_noeud
        

        """
        ad 30
         courant = 12
         suivant=None ----> 30  20,30 ----> 30,None
        
        """
    
     #Afficher les éléments du liste chainéés
    def afficher_elements(self):
            courant=self.tete
            while courant is not None:
                print(courant.donne,end="-->")
                courant=courant.suivant
            print("None")

    #Ajouter un élément aux début de la liste chainée
    def ajouterElementDebut(self,donne):
        nouveau_noeud = Noeud(donne)
        nouveau_noeud.suivant= self.tete
        self.tete=nouveau_noeud

    #Supprimer un élément de la liste chainée
    def supprimerElementListe(self,donne):
        if self.tete is None:
            return
        if self.tete.donne == donne:
            self.tete=self.tete.suivant
        
        courant=self.tete
        while courant.donne is not None:
            if  courant.suivant.donne == donne:
                courant.suivant=courant.suivant.suivant
                return
            courant=courant.suivant

        

        

        




#Utilisation de la classe
ma_liste=ListeChaine()
ma_liste.ajouterElementFin(10)
ma_liste.ajouterElementFin(20)
ma_liste.ajouterElementFin(30)

ma_liste.afficher_elements()

ma_liste.ajouterElementDebut(5)
ma_liste.ajouterElementDebut(6)
ma_liste.ajouterElementDebut(2)
ma_liste.afficher_elements()

ma_liste.supprimerElementListe(20)
ma_liste.afficher_elements()


"""
      Supprimer un nœud de la liste (par exemple, enlever le 20).

      Ajter un nœud au tout début de la liste (insérer avant la tete).
"""


 



        

        
