class EvaluadorDeCalificacion:
    def __init__(self, calificacion):
        self.calificacion = calificacion

    def determinar_calificacion(self):
        if self.calificacion > 9.0:
            return "A"
        elif self.calificacion > 8.0:
            return "B"
        elif self.calificacion >= 7.5:
            return "C"
        else:
            return "R"

    def mostrar_resultado(self):
        resultado = self.determinar_calificacion()
        print(f"La calificación es {resultado}.")