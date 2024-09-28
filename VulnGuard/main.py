import os
from vulnerability_scanner import read_requirements_txt, read_package_json, query_vulnerabilities, generate_report

def main():
    dependencies = {}

    # Read requirements.txt
    if os.path.exists('requirements.txt'):
        dependencies.update({dep.split('==')[0]: dep.split('==')[1] for dep in read_requirements_txt('requirements.txt')})

    # Read package.json
    if os.path.exists('package.json'):
        dependencies.update(read_package_json('package.json'))

    # Query vulnerabilities
    vulnerabilities = query_vulnerabilities(dependencies)

    # Generate report
    report = generate_report(vulnerabilities)
    print(report)

if __name__ == "__main__":
    main()