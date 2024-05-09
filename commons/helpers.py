import re
import requests
import json

from django.conf import settings


def get_site_content(url: str):
    response = requests.get(url)
    response.encoding = "utf-8"

    code = response.status_code

    if code == 200:
        # return BeautifulSoup(response.text, "html.parser")
        return response.text
    else:
        msg = f"Response Error [{response.code}]"
        print(msg)
        raise Exception(msg)


def divide_string(text, chunk_size=50000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])
    return chunks


def translate_jp_to_en(text_ls: list):

    translated_ls = []

    url = "https://api-free.deepl.com/v2/translate"

    data = {"auth_key": settings.RAPIDAPI_KEY, "source_lang": "JA", "target_lang": "EN"}

    for text in text_ls:
        data["text"] = text
        response = requests.post(url, data=data)

        if response.status_code == 200:
            translation = response.json()["translations"][0]["text"]
            translated_ls.append(translation)

    return "".join(translated_ls)


def find_word_instances(
    word: str,
    text: str,
):
    word_regex = re.compile(r"\b{}\b".format(re.escape(word)), re.IGNORECASE)
    return word_regex.findall(text)
