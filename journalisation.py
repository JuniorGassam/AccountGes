def logsVirement(func):
    def function(self, montant, compteDestinataire):
        etat = func(self, montant, compteDestinataire)
        fichier = open("logs.txt", "w")
        log_message = f"Transaction - {'Réussie' if etat else 'Échouée'}: {montant} vers {compteDestinataire.getutilisateur()}\n"
        fichier.write(log_message)
        return etat
    return function