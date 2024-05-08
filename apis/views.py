from ninja import NinjaAPI
from django.views.decorators.csrf import csrf_exempt

from apis.req import WordCount
from apis.utils import get_word_count

api = NinjaAPI()


@csrf_exempt
@api.post("/wordcount")
def word_count(request, data: WordCount):
    word = data.word
    url = data.url

    try:
        count = get_word_count(word=word, url=url)
    except Exception as e:
        print(f"Error: {e}")
        return HTTPException(status_code=500, detail="Internal Server Error")

    result = {"status": "ok", "count": count}
    print(result)
    return result
