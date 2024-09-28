# VulnGuard: A Minimalist Vulnerability Scanner

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
git clone https://github.com/yourusername/VulnGuard.git
cd VulnGuard
```

### Step 2: Install Dependencies

VulnGuard relies on the `searchsploit` command to query vulnerabilities. Ensure that `searchsploit` is installed and available in your PATH.

### Step 3: Run the Script

You can run the script using the following command:

```sh
python vulnerability_scanner.py
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
