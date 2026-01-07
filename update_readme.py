import random
import yaml
from pathlib import Path

QUOTE_START = "<!-- DAILY_QUOTE -->"
QUOTE_END = "<!-- /DAILY_QUOTE -->"

def get_daily_quote():
    with open("quotes.yaml") as f:
        quotes = yaml.safe_load(f)["quotes"]
    return random.choice(quotes)

def update_readme(quote):
    readme = Path("README.md")
    content = readme.read_text()

    new_section = f"""{QUOTE_START}
> "{quote['text']}"
>
> — {quote['author']}
{QUOTE_END}"""

    if QUOTE_START in content:
        start = content.find(QUOTE_START)
        end = content.find(QUOTE_END) + len(QUOTE_END)
        new_content = content[:start] + new_section + content[end:]
    else:
        new_content = content + "\n\n" + new_section

    readme.write_text(new_content)

if __name__ == "__main__":
    quote = get_daily_quote()
    update_readme(quote)
