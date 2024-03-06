from Compte import Compte

class CompteEpargne(Compte):
    def __init__(self, utilisateur, bank, plan):
        Compte.__init__(self, utilisateur, bank)
        self.plan = plan
