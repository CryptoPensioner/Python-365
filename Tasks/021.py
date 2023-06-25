import json

book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "publication_year": 1937
}

with open("book.json", "w") as f:
    json.dump(book, f)

with open("book.json", "r") as f:
    book = json.load(f)

print(book["title"])
print(book["author"])
print(book["publication_year"])
