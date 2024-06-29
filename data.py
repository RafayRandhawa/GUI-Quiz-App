import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=15&type=boolean")
response.raise_for_status()
API_data = response.json()["results"]
question_data = [{"question": data["question"], "correct_answer": data["correct_answer"]} for
                 data in API_data]

