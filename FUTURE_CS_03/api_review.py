#!/usr/bin/env python3
"""Offline review of a JSON sample for potentially sensitive response fields."""
import json
import sys
from pathlib import Path

SENSITIVE_KEYS = {
    "password", "password_hash", "access_token", "refresh_token",
    "api_key", "secret", "ssn", "debug_internal_note"
}

def walk(value, path="$"):
    findings = []
    if isinstance(value, dict):
        for key, child in value.items():
            current = f"{path}.{key}"
            if key.lower() in SENSITIVE_KEYS:
                findings.append((current, "Potentially sensitive or internal field is present"))
            findings.extend(walk(child, current))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(walk(child, f"{path}[{index}]"))
    return findings

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python api_review.py <sample.json>")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    findings = walk(data)
    if findings:
        print("Potential response-data exposure indicators:")
        for path, note in findings:
            print(f"- {path}: {note}")
    else:
        print("No configured sensitive field names found. This does NOT prove the response is secure.")
    print("\nThis is an offline heuristic. Confirm necessity and authorization with the API owner.")

if __name__ == "__main__":
    main()
