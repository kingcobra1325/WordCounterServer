# Word Counter with Django and Ninja/Fast API

This is a Word Counter application built with Django and Ninja/Fast API. It counts the occurrences of a word (excluding substrings) inside the HTML source code from a specified URL. Supports translation of Japanese websites to English to be able to parse and read the words on those specific websites via DeepL.

## Modules Used

- Django
- Django Ninja/Fast API
- Requests
- Pytest/Pytest-Django
- Pydantic

## Steps to Run

1. **Clone the repository:**
git clone https://github.com/kingcobra1325/WordCounterServer.git


2. **Copy and rename example.env to .env**
Make sure to add the DeepL API key as RAPIDAPI_KEY


3. **Install the required dependencies:**
pip install -r requirements.txt


4. **Run the Django development server:**
python manage.py runserver


5. **Access the Word Counter API via POST `http://localhost:8000/api/wordcount/`.**
```bash
curl -X POST "http://localhost:8000/api/word-counter/" -H "Content-Type: application/json" -d '{"url": "https://example.com", "word": "domain"}'
```
Upon a successful request, you should receive a response in the following format:

*{
  "status": "ok",
  "count": 4
}*

## Caveats

- Ensure that you have Python and pip installed on your system.
- The application relies on external libraries (`requests` and `pytest-django`), so ensure they are installed.
- This application may not work correctly if the specified URL is invalid or inaccessible.

## Test Cases

- Empty Requests
- No URL in Request Payload
- No Word in Request Payload
- Error while processing request
- Success even when DB error
- Success with no hits
- Success