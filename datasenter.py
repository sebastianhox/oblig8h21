from node import Node
from rack import Rack
from regneklynge import Regneklynge

class Datasenter:
    def __init__(self):
        self._regneklynger = {}

    def lesFraFil(self, filnavn):
        fil = open(filnavn)
        # Leser inn maks antall noder per rack far første linje i filen
        maksNoderPerRack = int(fil.readline().strip())

        regneklyngeNavn = filnavn.split(".")[0]

        nyRegneklynge = Regneklynge(regneklyngeNavn, maksNoderPerRack)
        self._regneklynger[regneklyngeNavn] = nyRegneklynge
        # Setter opp en variabel for å holde oversikt over antall noder som skal legges til
        noderTotalt = 0

        for linje in fil:
            biter = linje.strip().split()
            antallNoder = int(biter[0])
            minnePerNode = int(biter[1])
            prosessorerPerNode = int(biter[2])
            noderTotalt += antallNoder

            # While-løkken stopper når ønsket antall noder er lagt til
            while nyRegneklynge.hentAntallNoder() < noderTotalt:
                # Denne if setningen kjører kun første gang while-løkken kjører.
                # Metoden .hentRackListe() returnerer false kun dersom rack lista er tom
                if not nyRegneklynge.hentRackListe():
                    nyRack = Rack()
                    nyRegneklynge.leggTilRack(nyRack)

                nyNode = Node(minnePerNode,prosessorerPerNode)

                nyRegneklynge.leggNodeTilRack(nyNode)

        fil.close()

    def skrivUtInfro(self, navn):
        print(f"Informasjon om {self._regneklynger[navn]}")
        print(f"Antall rack: {(self._regneklynger[navn].hentAntRacks())}")
        print(f"Antall prosessorer: {self._regneklynger[navn].antProsessorer()}")
        print(f"Noder med minst 32GB: {self._regneklynger[navn].noderMedNokMinne(32)}")
        print(f"Noder med minst 64GB: {self._regneklynger[navn].noderMedNokMinne(64)}")
        print(f"Noder med minst 128GB: {self._regneklynger[navn].noderMedNokMinne(128)}")
