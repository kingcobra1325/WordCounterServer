from commons.helpers import get_site_content, find_word_instances

def get_word_count(word: str, url: str):
    
    site = get_site_content(url=url)

    print(site)
    # print(site.get_text())
    # print(f"{word} is in {url}: {word in site.get_text(separator=' ')}")

    instances = find_word_instances(word=word, text=site)
    
    print(instances)

    return len(instances)
