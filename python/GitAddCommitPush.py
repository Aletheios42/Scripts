import subprocess
import readline

def main():
    # Solicita el mensaje del commit
    commit_message = input("Introduce el mensaje del commit: ")

    # Ejecuta los comandos de git
    try:
        # Añade todos los archivos al índice
        subprocess.run(["git", "add", "."], check=True)
        
        # Realiza el commit con el mensaje proporcionado
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Empuja los cambios al repositorio remoto
        subprocess.run(["git", "push"], check=True)
        
        print("Cambios añadidos, commit realizado y push ejecutado con éxito.")

    except subprocess.CalledProcessError as e:
        print(f"Ocurrió un error durante la ejecución del comando: {e}")

if __name__ == "__main__":
    main()

