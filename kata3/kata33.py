velocAst = int(input("Velocidad del asteroide en Km/s: "))
TamanoAst = int(input("Tamaño del asteroide en metros: "))

if velocAst > 25 and TamanoAst > 25:
    print("El asteroide es peligroso, enviar advertencia")
elif velocAst > 20:
    print("Luz en el cielo")
elif velocAst < 25:
    print("El asteroide no es peligroso")
else:
    print("El asteroide no es peligroso")