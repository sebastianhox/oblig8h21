
class Node:
    def __init__(self, minneStr, antProsessorer):
        self._minneStr = minneStr
        self._antProsessorer = antProsessorer

    def hentAntallProsessorer(self):
        return self._antProsessorer

    def hentMinneStr(self):
        return self._minneStr
