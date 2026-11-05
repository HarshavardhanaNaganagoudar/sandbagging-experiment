import ollama
from pathlib import Path


MODEL = "gemma4:12b"

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def read_file(file_path):
    """Read and return the contents of a text file."""
    return Path(file_path).read_text(encoding="utf-8")


def ask_model(prompt):
    """Send a prompt to the local Ollama model."""
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        think=True
    )

    thinking = response.message.thinking or ""
    content = response.message.content or ""

    return thinking, content


def save_file(file_name, content):
    """Save content to the outputs directory."""
    file_path = OUTPUT_DIR / file_name
    file_path.write_text(content, encoding="utf-8")
