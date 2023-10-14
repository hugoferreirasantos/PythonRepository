import pyforms
from pyforms.controls import ControlText, ControlButton
from pyforms import BaseWidget


class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples, self).__init__('ExemploSimples')
        # Definition of the forms fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


# Execute the application
if __name__ == "__main__":
    from pyforms import start_app

    start_app(ExemploSimples)
