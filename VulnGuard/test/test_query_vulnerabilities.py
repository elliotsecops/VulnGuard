import sys
import os
import pytest
import json
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vulnerability_scanner import query_vulnerabilities

# Mock data for vulnerabilities
MOCK_SEARCHSPLOIT_OUTPUT = """
-------------------------------------------------------------------------------------------------------------- ---------------------------------
Exploit Title | Path
-------------------------------------------------------------------------------------------------------------- ---------------------------------
requests - HTTP Authorization Header Redirection | python/webapps/49772.txt
flask - Unexpected Memory Usage | python/webapps/12345.txt
-------------------------------------------------------------------------------------------------------------- ---------------------------------
"""

# Test querying vulnerabilities
def test_query_vulnerabilities(mocker):
    mocker.patch('subprocess.run', return_value=mocker.Mock(stdout=MOCK_SEARCHSPLOIT_OUTPUT))
    dependencies = {
        "requests": "2.24.0",
        "flask": "1.0.2"
    }
    vulnerabilities = query_vulnerabilities(dependencies)
    assert vulnerabilities == {
        "requests": [
            {
                "id": "requests - HTTP Authorization Header Redirection",
                "description": "python/webapps/49772.txt",
                "fixed_version": "2.25.1",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-33503"
            }
        ],
        "flask": [
            {
                "id": "flask - Unexpected Memory Usage",
                "description": "python/webapps/12345.txt",
                "fixed_version": "1.0",
                "url": "https://nvd.nist.gov/vuln/detail/CVE-2019-1010083"
            }
        ]
    }