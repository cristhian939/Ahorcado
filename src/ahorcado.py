import random
import os

def cargar_palabras(ruta_archivo):
    """Lee el archivo de texto y retorna una lista de palabras."""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Lee las líneas, quita espacios y saltos de línea y filtra líneas vacías
            palabras = [linea.strip().lower() for linea in archivo if linea.strip()]
        return palabras
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_archivo}")
        return ["error"]

def limpiar_pantalla():
    """Limpia la consola para una mejor experiencia visual."""
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar():
    # 1. Configuración Inicial
    ruta_datos = os.path.join(os.path.dirname(__file__), '..', 'data', 'palabras.txt')
    palabras_disponibles = cargar_palabras(ruta_datos)
    
    palabra_secreta = random.choice(palabras_disponibles)
    letras_adivinadas = []
    vidas = 6
    
    limpiar_pantalla()
    print("========================================")
    print("       ¡BIENVENIDO AL AHORCADO!         ")
    print("========================================")
    
    # 2. Bucle Principal
    while vidas > 0:
        print("\n" + "="*40)
        
        # Mostrar progreso de la palabra
        progreso = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
                
        print(f"Palabra: {progreso}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras usadas: {', '.join(letras_adivinadas) if letras_adivinadas else 'Ninguna'}")
        
        # 3. Condicionales - Condición de Victoria
        if "_" not in progreso:
            print("\n¡FELICIDADES! Has adivinado la palabra exacta.")
            break
            
        intento = input("\nIngresa una letra (o escribe 'pista' por el costo de 2 vidas): ").lower().strip()
        limpiar_pantalla()
        
        # Innovación solicitada: Sistema de pistas
        if intento == "pista":
            if vidas > 2:
                vidas -= 2
                print(" PISTA UTILIZADA (-2 vidas): La palabra está relacionada con la carrera de sistemas.")
            else:
                print(" No tienes suficientes vidas para pedir una pista. ¡Te arriesgas a perder!")
            continue

        # Validaciones de entrada de usuario
        if len(intento) != 1 or not intento.isalpha():
            print(" Entrada inválida. Por favor, ingresa solo una letra.")
            continue
            
        if intento in letras_adivinadas:
            print(" Ya intentaste con esa letra. Prueba con otra.")
            continue
            
        # Registrar el intento válido
        letras_adivinadas.append(intento)
        
        # Verificar si acertó o falló
        if intento in palabra_secreta:
            print(" ¡Correcto! La letra está en la palabra.")
        else:
            vidas -= 1
            print(" Letra incorrecta. Pierdes una vida.")
            
    # Fin del bucle - Condición de Derrota
    if vidas == 0:
        print("\n" + "="*40)
        print(" ¡FIN DEL JUEGO! Te has quedado sin vidas.")
        print(f"La palabra correcta era: {palabra_secreta.upper()}")
        print("="*40)

# Punto de entrada del programa
if __name__ == "__main__":
    jugar()