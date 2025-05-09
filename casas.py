import os

class Casa:
    def __init__(self, ventanas, puertas, techo, bano):
        self.__ventanas = ventanas
        self.__puertas = puertas
        self.__techo = techo
        self.__bano = bano

    @property
    def _ventanas(self):
        return self.__ventanas

    @_ventanas.setter
    def _ventanas(self, value):
        self.__ventanas = value

    @property
    def _puertas(self):
        return self.__puertas

    @_puertas.setter
    def _puertas(self, value):
        self.__puertas = value

    @property
    def _techo(self):
        return self.__techo

    @_techo.setter
    def _techo(self, value):
        self.__techo = value

    @property
    def _bano(self):
        return self.__bano

    @_bano.setter
    def _bano(self, value):
        self.__bano = value

        
class ViviendaFamiliar(Casa):
    def __init__(self, ventanas, puertas, techo, bano, sala_de_estar, piscina, segundo_piso):
        super().__init__(ventanas, puertas, techo, bano)
        self.__sala_de_estar = sala_de_estar
        self.__piscina = piscina
        self.__segundo_piso = segundo_piso

    @property
    def _sala_de_estar(self):
        return self.__sala_de_estar

    @_sala_de_estar.setter
    def _sala_de_estar(self, value):
        self.__sala_de_estar = value

    @property
    def _piscina(self):
        return self.__piscina

    @_piscina.setter
    def _piscina(self, value):
        self.__piscina = value

    @property
    def _segundo_piso(self):
        return self.__segundo_piso

    @_segundo_piso.setter
    def _segundo_piso(self, value):
        self.__segundo_piso = value

class Bungalows(Casa):
    def __init__(self, ventanas, puertas, techo, bano, piscina, cuartos):
        super().__init__(ventanas, puertas, techo, bano)
        self.__piscina = piscina
        self.__cuartos = cuartos
        

    @property
    def _piscina(self):
        return self.__piscina

    @_piscina.setter
    def _piscina(self, value):
        self.__piscina = value

    @property
    def _cuartos(self):
        return self.__cuartos

    @_cuartos.setter
    def _cuartos(self, value):
        self.__cuartos = value


class Apartamento(Casa):
    def __init__(self, ventanas, puertas, techo, bano, piso, cuartos, cocina):
        super().__init__(ventanas, puertas, techo, bano)
        self.__piso = piso
        self.__cuartos = cuartos
        self.__cocina = cocina

    def get_piso(self):
        return self.piso

    def set_piso(self, value):
        self.piso = value

    def get_cuartos(self):
        return self.cuartos

    def set_cuartos(self, value):
        self.cuartos = value

    def get_cocina(self):
        return self.cocina

    def set_cocina(self, value):
        self.cocina = value
