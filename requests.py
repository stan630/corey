import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "pR5uwHeZwbc9uARNi9uQ", "isbns": "9780802123459"})
print(res.json())


# Goodreads API Key: pR5uwHeZwbc9uARNi9uQ