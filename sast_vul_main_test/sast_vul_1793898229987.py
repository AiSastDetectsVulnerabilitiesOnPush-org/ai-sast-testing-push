"""
SAST TEST FILE - FOR SECURITY SCANNING VALIDATION ONLY
This file contains intentional vulnerabilities to trigger SAST rules.
DO NOT use in production code.
Created with Claude
"""

def read_file(filename):
    base_path = "/var/app/data/"
    full_path = base_path + filename 
    with open(full_path, "r") as f:
        return f.read()