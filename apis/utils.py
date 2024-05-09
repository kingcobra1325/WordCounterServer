from commons.helpers import (
    get_site_content,
    find_word_instances,
    translate_jp_to_en,
    divide_string,
)


def get_word_count(word: str, url: str):

    content = get_site_content(url=url)

    divided_content = divide_string(content)

    translated_text = translate_jp_to_en(divided_content)

    instances = find_word_instances(word=word, text=translated_text)

    return len(instances)
