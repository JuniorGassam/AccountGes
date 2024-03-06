class Utilisateur:

    def __init__(self,prenom,nom,compte):
        self.prenom= prenom
        self.nom= nom
        self.compte = compte


    def getPrenom(self):
        return self.prenom


    def getNom(self):
        return self.nom


    def getCompte(self):
        return self.compte