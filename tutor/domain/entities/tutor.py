class Tutor:
    def __init__(self, nombres, primer_apellido, segundo_apellido=None):
        self.nombres = nombres
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido

    def generar_identificador(self):
        identificador = self.nombres.lower().split()[0] + '-' + self.primer_apellido.lower()
        return identificador
