from datasenter import Datasenter

def hovedprogram():
    datasenter = Datasenter()

    datasenter.lesFraFil("abel.txt")
    datasenter.skrivUtInfro("abel")

    datasenter.lesFraFil("saga.txt")
    datasenter.skrivUtInfro("saga")


hovedprogram()
