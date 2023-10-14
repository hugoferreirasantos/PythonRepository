from flexx import flx, app


class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text="Olá")
        flx.Button(text="Mundo")


if __name__ == "__main__":
    a = flx.App(Exemplo, title="Flexx Demonstração")
    m = a.launch()
    flx.run()
