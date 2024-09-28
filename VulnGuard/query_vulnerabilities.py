import re

def query_vulnerabilities(dependencies, searchsploit_output):
    vulnerabilities = {}
    for dependency, version in dependencies.items():
        vulnerabilities[dependency] = []
        matches = re.findall(r"^(.*?)\s*\|\s*(.*?)$", searchsploit_output, re.MULTILINE)
        for match in matches:
            if match[0] and match[1] and "Exploit Title" not in match[0]:
                if dependency in match[0]:  # Ensure the vulnerability is for the correct dependency
                    vulnerabilities[dependency].append({"id": match[0].strip(), "description": match[1].strip()})
    return vulnerabilities