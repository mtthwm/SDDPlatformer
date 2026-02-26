import re
import sys
from pathlib import Path


def expand_placeholders(input_path: str) -> None:
    source = Path(input_path)
    if not source.exists():
        print(f"Error: File '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    text = source.read_text()
    cwd = Path.cwd()

    def replace_match(match):
        ref_path = cwd / match.group(1)
        if not ref_path.exists():
            print(f"Warning: Referenced file '{ref_path}' not found. Leaving placeholder.", file=sys.stderr)
            return match.group(0)
        return ref_path.read_text().strip()

    result = re.sub(r'%([^%]+)%', replace_match, text)
    print(result, end="")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gen-prompt.py <file_path>")
        sys.exit(1)

    expand_placeholders(sys.argv[1])