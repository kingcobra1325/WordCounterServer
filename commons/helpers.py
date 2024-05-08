import re
import requests

from bs4 import BeautifulSoup

def get_site_content(url: str):
    response = requests.get(url)

    code = response.status_code

    if code == 200:
        # return BeautifulSoup(response.text, "html.parser")
        return response.text
    else:
        msg = f"Response Error [{response.code}]"
        print(msg)
        raise Exception(msg)

def find_word_instances(word: str, text: str,):
    word_regex = re.compile(r'\b[\.,>]?{}[<\.,]?\b'.format(re.escape(word)), re.IGNORECASE)
    return word_regex.findall(text)
