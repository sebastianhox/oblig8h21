
class Rack:
    def __init__(self):
        self._noder = []

    # Er det riktig? Trengs det?
    def leggTilNode(self, node):
        self._noder.append(node)

    def hentNoderListe(self):
        return self._noder
