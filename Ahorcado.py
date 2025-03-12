import random

def seleccionar_palabra(): 
    palabras = ["python", "programacion", "computadora", "teclado", "raton", "monitor", "desarrollo"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas): 
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)

def ahorcado(): 
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos = 6
    
    print("\n¡Bienvenido al Juego del Ahorcado!\n")
    
    while intentos > 0:
        print(f"\nIntentos restantes: {intentos}")
        print(mostrar_progreso(palabra, letras_adivinadas))
        
        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya intentaste con esa letra. Intenta otra.")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos -= 1
            print("Incorrecto. Pierdes un intento.")
        
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}\n")
            break
    else:
        print(f"\n¡Has perdido! La palabra era: {palabra}\n")

if __name__ == "__main__":
    ahorcado()
