from ninja import NinjaAPI
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError
from apis.models import WordCount as WordCountModel
from apis.req import WordCount
from apis.utils import get_word_count
import traceback

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
        print(traceback.format_exc())
        return HttpResponseServerError("Internal Server Error")

    result = {"status": "ok", "count": count}

    try:
        WordCountModel.objects.create(
            word=word,
            url=url,
            count=count,
        )
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())

    return result
