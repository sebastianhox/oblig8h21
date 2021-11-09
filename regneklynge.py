from rack import Rack

class Regneklynge:
    def __init__(self, navn, maksNoderPerRack):
        self._navn = navn
        self._maksNoderPerRack = maksNoderPerRack
        self._racks = []
        self._antallNoder = 0

    def __str__(self):
        return self._navn

    def leggNodeTilRack(self,node):
        # Sjekker om det er plass i siste rack i _racks lista
        if self._maksNoderPerRack > len(self._racks[-1].hentNoderListe()):
            self._racks[-1].leggTilNode(node)
        # Når siste rack er fylt opp, opprettes det en ny rack objekt og legges til i _racks lista
        else:
            nyRack = Rack()
            self.leggTilRack(nyRack)
            self._racks[-1].leggTilNode(node)
        self._antallNoder += 1

    def hentRackListe(self):
        return self._racks

    def leggTilRack(self, rack):
        self._racks.append(rack)

    def hentAntallNoder(self):
        return self._antallNoder

    def antProsessorer(self):
        prosessorerTotalt = 0

        for rack in self._racks:
            noderListe = rack.hentNoderListe()

            for node in noderListe:
                prosessorer = node.hentAntallProsessorer()

                prosessorerTotalt += prosessorer

        return prosessorerTotalt

    def noderMedNokMinne(self, paakrevdMinne):
        antallNoder = 0

        for rack in self._racks:
            noderListe = rack.hentNoderListe()

            for node in noderListe:
                minne = node.hentMinneStr()

                if minne >= paakrevdMinne:
                    antallNoder += 1

        return antallNoder

    def hentAntRacks(self):
        return len(self._racks)
