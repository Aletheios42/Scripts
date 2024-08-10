from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


def setup_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Descomentar si quieres que el navegador no se muestre
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def main():
    url = input("Introduce la URL del problema de LeetCode: ").strip()

    driver = setup_browser()
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 10)

        # Depuración: verificar la carga de la página
        print("Esperando a que la página se cargue...")

        # Depuración: captura del título del problema
        problem_title_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-cy="question-title"]')
            )
        )
        problem_title = problem_title_element.text.strip()
        print(f"Título del problema encontrado: {problem_title}")

        # Depuración: captura de la dificultad
        difficulty_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[diff=""]'))
        )
        difficulty = difficulty_element.text.strip()
        print(f"Dificultad encontrada: {difficulty}")

        # Depuración: captura de la descripción
        description_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-key="description-content"]')
            )
        )
        description = description_element.text.strip()
        print("Descripción del problema capturada.")

        # Creación del directorio
        problem_number = url.split("/")[-2]
        folder_name = f"{problem_number}.{problem_title.replace(' ', '_')}"
        os.makedirs(folder_name, exist_ok=True)
        print(f"Directorio creado: {folder_name}")

        # Guardar la descripción en un archivo
        with open(os.path.join(folder_name, "Subject.txt"), "w") as file:
            file.write(description)
        print("Descripción guardada en Subject.txt")

        # Crear carpeta para la solución
        os.makedirs(os.path.join(folder_name, "Solution"), exist_ok=True)
        with open(
            os.path.join(folder_name, "Solution", "Solution_v1.cpp"), "w"
        ) as file:
            file.write("// Solution goes here\n")
        print("Archivo Solution_v1.cpp creado en la carpeta Solution")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        driver.save_screenshot(
            "error_screenshot.png"
        )  # Guardar captura de pantalla en caso de error
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
