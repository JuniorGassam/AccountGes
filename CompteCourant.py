from Compte import Compte

class CompteCourant(Compte):
    def __init__(self,utilisateur, bank, carte):
        Compte.__init__(self,utilisateur,bank)
        self.carte = carte
