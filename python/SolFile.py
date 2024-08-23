import os
import sys
import subprocess


# Función para obtener la versión del compilador adecuada
def getCompilerVersion():
    try:
        output = subprocess.check_output(["solc", "--version"], text=True)
        for line in output.splitlines():
            if "Version:" in line:
                version = line.split("Version:")[1].split("+")[0].strip()
                return version
    except Exception as e:
        print(f"Error al obtener la versión del compilador: {e}")
        sys.exit(1)


# Función para crear el archivo src
def createSrcFile(filepath):
    absolute_path = os.path.abspath(filepath)
    filename = os.path.basename(filepath)
    filename_without_extension = os.path.splitext(
        os.path.splitext(filename)[0])[0]
    compiler_version = getCompilerVersion()

    content = f"""// Layout of Contract:
// version
// imports
// errors
// interfaces, libraries, contracts
// Type declarations
// State variables
// Events
// Modifiers
// Functions

// Layout of Functions:
// constructor
// receive function (if exists)
// fallback function (if exists)
// external
// public
// internal
// private
// internal & private view & pure functions
// external & public view & pure functions

// SPDX-License-Identifier: MIT

pragma solidity ^{compiler_version};

/**
 * @title {filename_without_extension}
 * @author Aletheios42
 *
 */
contract {filename_without_extension} {{
}}
"""

    full_file_path = os.path.join(
        os.path.dirname(absolute_path), filename_without_extension + ".sol"
    )
    with open(full_file_path, "w") as file:
        file.write(content)

    print(f"Archivo {full_file_path} creado con éxito.")


# Función para crear el archivo script
def createScriptFile(filepath):
    absolute_path = os.path.abspath(filepath)
    filename = os.path.basename(filepath)
    filename_without_extension = os.path.splitext(
        os.path.splitext(filename)[0])[0]
    compiler_version = getCompilerVersion()

    # Obtener la ruta del directorio src
    project_root = os.path.dirname(os.path.dirname(absolute_path))
    src_dir = os.path.join(project_root, "src")

    # Recopilar los imports desde la carpeta src
    imports = []
    if os.path.isdir(src_dir):
        for file in os.listdir(src_dir):
            if file.endswith(".sol"):
                contract_name = os.path.splitext(file)[0]
                import_statement = f'import {{ {
                    contract_name} }} from "src/{file}";'
                imports.append(import_statement)

    # Crear el contenido del archivo .s.sol
    content = f"""// SPDX-License-Identifier: MIT

pragma solidity ^{compiler_version};

import {{ Script }} from "forge-std/Script.sol";
{"\n".join(imports)}

/**
 * @title {filename_without_extension}
 * @author Aletheios42
 *
 */
contract {filename_without_extension} is Script {{
}}
"""

    full_file_path = os.path.join(
        os.path.dirname(absolute_path), filename_without_extension + ".s.sol"
    )
    with open(full_file_path, "w") as file:
        file.write(content)

    print(f"Archivo {full_file_path} creado con éxito.")


# Función principal
def main():
    if len(sys.argv) != 2:
        print("Uso: python3 SolFile.py <ruta_al_archivo>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Comprobar si el archivo termina en .s.sol primero
    if filepath.endswith(".s.sol"):
        createScriptFile(filepath)
    # Si no, comprobar si termina en .sol
    elif filepath.endswith(".sol"):
        createSrcFile(filepath)
    else:
        print(f"Extensión no soportada: {filepath}")
        sys.exit(1)


if __name__ == "__main__":
    main()

