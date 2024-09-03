from CalificacionesNumericasLiterales import EvaluadorDeCalificacion


def main():
    calificacion = float(input("Dame la calificación: "))
    evaluador = EvaluadorDeCalificacion(calificacion)
    evaluador.mostrar_resultado()

if __name__ == "__main__":
    main()