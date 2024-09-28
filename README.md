# VulnGuard: Un Escáner de Vulnerabilidades de dependencias con Python

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Uso](#uso)
5. [Cómo Funciona](#cómo-funciona)
6. [Pruebas](#pruebas)
7. [Contribuir](#contribuir)
8. [Licencia](#licencia)

## Introducción

**VulnGuard** es un escáner de vulnerabilidades minimalista diseñado para ayudar a los desarrolladores y profesionales a identificar y mitigar vulnerabilidades de seguridad en sus proyectos. Escanea las dependencias del proyecto en busca de vulnerabilidades conocidas y proporciona un informe detallado. VulnGuard es particularmente útil para proyectos en Python y JavaScript, ya que soporta el escaneo de dependencias listadas en archivos `requirements.txt` y `package.json`.

## Características

- **Identificar Versiones Vulnerables**: Detecta versiones vulnerables de dependencias y sugiere actualizaciones.
- **Proporcionar Enlaces a Información Adicional**: Ofrece enlaces a información adicional sobre vulnerabilidades de la National Vulnerability Database (NVD).
- **Diseño Minimalista**: Mantiene la base de código simple y fácil de entender, haciéndola adecuada tanto para principiantes como para desarrolladores experimentados.
- **Soporte para Múltiples Formatos de Archivo**: Soporta el escaneo de dependencias listadas en archivos `requirements.txt` (Python) y `package.json` (JavaScript).

## Instalación

Para usar VulnGuard, necesitas tener Python 3.12.1 o una versión posterior instalada en tu sistema. Puedes instalar VulnGuard clonando el repositorio e instalando las dependencias requeridas.

### Paso 1: Clonar el Repositorio

```sh
git clone https://github.com/elliotsecops/VulnGuard.git
cd VulnGuard
```

### Paso 2: Instalar Dependencias

VulnGuard depende del comando `searchsploit` para consultar vulnerabilidades. Asegúrate de que `searchsploit` esté instalado y disponible en tu PATH.

### Instalación y Configuración

VulnGuard requiere `searchsploit` para funcionar. `searchsploit` es parte del proyecto ExploitDB. Debido a que el repositorio de ExploitDB es grande y no hay versiones precompiladas, configurar `searchsploit` suele ser la parte más complicada de hacer que VulnGuard funcione. Si encuentras problemas, revisa y sigue cuidadosamente estas instrucciones:

**1. Clonar el Repositorio de ExploitDB (usando depth=1 para evitar clonar archivos muy grandes):**

```bash
git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git
```

**2. Hacer que `searchsploit` esté disponible:**

Hay dos formas principales de hacer que el comando `searchsploit` esté disponible en tu terminal:

**A) Copiar `searchsploit` a un directorio en tu PATH (más fácil):**

```bash
sudo cp exploitdb/searchsploit /usr/local/bin/  # Reemplaza `/usr/local/bin` si no está en tu PATH
sudo chmod +x /usr/local/bin/searchsploit
```

Verifica que `searchsploit` esté ahora en tu PATH usando `which searchsploit`. La salida debería ser `/usr/local/bin/searchsploit` o la ruta a donde decidiste copiar `searchsploit`. Si la salida está vacía, ese directorio no está en tu PATH y debes elegir uno que sí esté, o actualizar la configuración de tu shell para que el directorio que contiene `searchsploit` esté en tu PATH.

**B) Añadir el directorio exploitdb a tu PATH (más robusto):**

Encuentra la ruta completa: Usa el comando `pwd` dentro del directorio exploitdb para encontrar su ruta completa. Por ejemplo: `/home/user/projects/exploitdb`

Edita tu archivo de configuración del shell: (`.bashrc`, `.zshrc`, `.bash_profile`, etc.). Añade la siguiente línea, reemplazando `/path/to/exploitdb` con la ruta real:

```bash
export PATH="$PATH:/path/to/exploitdb"
```

Carga el archivo de configuración: `source ~/.zshrc` (o el equivalente).

Verifica: `echo $PATH` – La ruta a exploitdb debería estar ahora incluida.

**3. Verificar la Instalación de `searchsploit`:**

```sh
searchsploit --version
searchsploit afd windows local  # Ejemplo de búsqueda
```

Si obtienes un error de "comando no encontrado", verifica nuevamente la ruta que añadiste a tu PATH y asegúrate de que no haya errores tipográficos.

**4. Instalar Dependencias de Python de VulnGuard:**

```sh
python3 -m venv .venv   # Crea y activa un entorno virtual
source .venv/bin/activate
pip install -r requirements.txt
```

Ahora puedes ejecutar VulnGuard:

```sh
python vulnerability_scanner.py
```

Si encuentras un error `Could not find: rc_file ~` al ejecutar `searchsploit`, crea un archivo de configuración vacío en tu directorio home:

```sh
touch ~/.searchsploit_rc
```

- Recuerda reemplazar las rutas de marcador de posición con las rutas reales en tu sistema.

### Paso 3: Ejecutar el Script

Puedes ejecutar el script usando el siguiente comando:

```sh
python vulnerability_scanner.py path/to/requirements.txt
```

## Uso

VulnGuard escanea automáticamente los archivos `requirements.txt` y `package.json` en el directorio actual. Identifica versiones vulnerables de dependencias y genera un informe detallado.

### Ejemplo de Salida

```sh
Dependency: requests
 - Vulnerability: CVE-2021-33503
   Description: The requests package before 2.25.1 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the network.

Dependency: flask
 - Vulnerability: CVE-2019-1010083
   Description: The Pallets Project Flask before 1.0 is affected by: unexpected memory usage. The impact is: denial of service. The attack vector is: crafted encoded JSON data. The fixed version is: 1.0.
```

## Cómo Funciona

VulnGuard opera en varios pasos para identificar y reportar vulnerabilidades:

### Paso 1: Leer Dependencias

VulnGuard lee las dependencias de los archivos `requirements.txt` y `package.json` en el directorio actual. Analiza estos archivos para extraer los nombres y versiones de las dependencias.

### Paso 2: Consultar Vulnerabilidades

Usando el comando `searchsploit`, VulnGuard consulta la Base de Datos de Exploits para vulnerabilidades conocidas relacionadas con las dependencias identificadas. Luego, mapea estas vulnerabilidades a los datos simulados proporcionados en el diccionario `MOCK_VULNERABILITIES`.

### Paso 3: Generar Informe

VulnGuard genera un informe detallado que lista las dependencias, sus vulnerabilidades asociadas y descripciones de las vulnerabilidades. El informe se imprime en la consola.

## Pruebas

VulnGuard incluye una suite de pruebas para asegurar que la funcionalidad trabaja como se espera. Puedes ejecutar las pruebas usando `pytest`.

### Ejecutar Pruebas

```sh
cd test
pytest
```

### Cobertura de Pruebas

Las pruebas cubren los siguientes aspectos:

- Leer dependencias de `requirements.txt` y `package.json`.
- Consultar vulnerabilidades usando el comando `searchsploit`.
- Generar un informe detallado sin incluir la versión corregida y la URL.

## Contribuir

¡Las contribuciones a VulnGuard son bienvenidas! Si tienes ideas para mejoras o nuevas características, por favor abre un issue o envía un pull request.

### Directrices

1. **Fork del Repositorio**: Comienza haciendo un fork del repositorio de VulnGuard a tu propia cuenta de GitHub.
2. **Clonar el Repositorio**: Clona tu repositorio forkeado a tu máquina local.
3. **Crear una Nueva Rama**: Crea una nueva rama para tus cambios.
4. **Hacer Cambios**: Implementa tus cambios y asegúrate de que las pruebas pasen.
5. **Enviar un Pull Request**: Envía un pull request al repositorio principal.

## Licencia
 VulnGuard está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
 
---

# 1. VulnGuard: Simplified Dependency Vulnerability Scanner 

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

**VulnGuard** is a minimalist vulnerability scanner designed to help developers identify and mitigate security vulnerabilities in their projects. It scans project dependencies for known vulnerabilities and provides a detailed report. VulnGuard is particularly useful for Python and JavaScript projects, as it supports scanning dependencies listed in `requirements.txt` and `package.json` files.

## Features

- **Identify Vulnerable Versions**: Detects vulnerable versions of dependencies and suggests updates.
- **Provide Links to Additional Information**: Offers links to additional information on vulnerabilities from the National Vulnerability Database (NVD).
- **Minimalist Design**: Keeps the codebase simple and easy to understand, making it suitable for both beginners and experienced developers.
- **Support for Multiple File Formats**: Supports scanning dependencies listed in `requirements.txt` (Python) and `package.json` (JavaScript) files.

## Installation

To use VulnGuard, you need to have Python 3.12.1 or later installed on your system. You can install VulnGuard by cloning the repository and installing the required dependencies.

### Step 1: Clone the Repository

```sh
git clone https://github.com/elliotsecops/VulnGuard.git
cd VulnGuard
```

### Step 2: Install Dependencies

VulnGuard relies on the `searchsploit` command to query vulnerabilities. Ensure that `searchsploit` is installed and available in your PATH.

### Installation and Setup

VulnGuard requires `searchsploit` to function. `searchsploit` is part of the ExploitDB project. Because the ExploitDB repository is large, and there are no pre-built releases, setting up `searchsploit` is often the trickiest part of getting VulnGuard to work. If you encounter issues, carefully review and follow these instructions:

**1. Clone the ExploitDB Repository (using depth=1 to avoid cloning very large files):**

```bash
git clone --depth=1 https://gitlab.com/exploit-database/exploitdb.git
```

**2. Make searchsploit Available:**

There are two main ways to make the `searchsploit` command available in your terminal:

**A) Copy `searchsploit` to a directory on your PATH (easiest):**

```bash
sudo cp exploitdb/searchsploit /usr/local/bin/  # Replace `/usr/local/bin` if it is not on your PATH
sudo chmod +x /usr/local/bin/searchsploit
```

Verify that `searchsploit` is now on your path using `which searchsploit`. The output should be `/usr/local/bin/searchsploit` or the path to wherever you chose to copy `searchsploit` to. If the output is empty, that directory is not on your PATH and you must choose one that is, or update your shell's configuration so that the directory containing `searchsploit` is on your PATH.

**B) Add the exploitdb directory to your PATH (more robust):**

Find the full path: Use the `pwd` command inside the exploitdb directory to find its full path. For example: `/home/user/projects/exploitdb`

Edit your shell configuration file: (`.bashrc`, `.zshrc`, `.bash_profile`, etc.). Add the following line, replacing `/path/to/exploitdb` with the actual path:

```bash
export PATH="$PATH:/path/to/exploitdb"
```

Source the configuration file: `source ~/.zshrc` (or equivalent).

Verify: `echo $PATH` – The path to exploitdb should now be included.

**3. Verify `searchsploit` Installation:**

```sh
searchsploit --version
searchsploit afd windows local  # Example search
```

If you get a "command not found" error, double-check the path you added to your PATH and make sure there are no typos.

**4. Install VulnGuard's Python Dependencies:**

```sh
python3 -m venv .venv   # Create and activate a virtual environment
source .venv/bin/activate
pip install -r requirements.txt
```

Now you can run VulnGuard:

```sh
python vulnerability_scanner.py
```

If you encounter a `Could not find: rc_file ~` error when running `searchsploit`, create an empty configuration file in your home directory:

```sh
touch ~/.searchsploit_rc
```

- Remember to replace placeholder paths with the actual paths on your system!

### Step 3: Run the Script

You can run the script using the following command:

```sh
python vulnerability_scanner.py path/to/requirements.txt
```

## Usage

VulnGuard automatically scans the `requirements.txt` and `package.json` files in the current directory. It identifies vulnerable versions of dependencies and generates a detailed report.

### Example Output

```sh
Dependency: requests
 - Vulnerability: CVE-2021-33503
   Description: The requests package before 2.25.1 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the network.

Dependency: flask
 - Vulnerability: CVE-2019-1010083
   Description: The Pallets Project Flask before 1.0 is affected by: unexpected memory usage. The impact is: denial of service. The attack vector is: crafted encoded JSON data. The fixed version is: 1.0.
```

## How It Works

VulnGuard operates in several steps to identify and report vulnerabilities:

### Step 1: Read Dependencies

VulnGuard reads the dependencies from the `requirements.txt` and `package.json` files in the current directory. It parses these files to extract the names and versions of the dependencies.

### Step 2: Query Vulnerabilities

Using the `searchsploit` command, VulnGuard queries the Exploit Database for known vulnerabilities related to the identified dependencies. It then maps these vulnerabilities to the mock data provided in the `MOCK_VULNERABILITIES` dictionary.

### Step 3: Generate Report

VulnGuard generates a detailed report listing the dependencies, their associated vulnerabilities, and descriptions of the vulnerabilities. The report is printed to the console.

## Testing

VulnGuard includes a suite of tests to ensure that the functionality works as expected. You can run the tests using `pytest`.

### Running Tests

```sh
cd test
pytest
```

### Test Coverage

The tests cover the following aspects:

- Reading dependencies from `requirements.txt` and `package.json`.
- Querying vulnerabilities using the `searchsploit` command.
- Generating a detailed report without including the fixed version and URL.

## Contributing

Contributions to VulnGuard are welcome! If you have ideas for improvements or new features, please open an issue or submit a pull request.

### Guidelines

1. **Fork the Repository**: Start by forking the VulnGuard repository to your own GitHub account.
2. **Clone the Repository**: Clone your forked repository to your local machine.
3. **Create a New Branch**: Create a new branch for your changes.
4. **Make Changes**: Implement your changes and ensure that the tests pass.
5. **Submit a Pull Request**: Submit a pull request to the main repository.

## License

VulnGuard is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
