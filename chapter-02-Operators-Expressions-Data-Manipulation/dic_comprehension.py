# dict comprehension
# 3. Book information
books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "pages": 281,
        "genres": ["Fiction", "Classic", "Drama"]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "pages": 328,
        "genres": ["Fiction", "Dystopian", "Political"]
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "pages": 180,
        "genres": ["Fiction", "Classic", "Romance"]
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "pages": 310,
        "genres": ["Fantasy", "Adventure", "Classic"]
    }
]

# we can collect all names 
title = [s['title'] for s in books]
print(title)
# we can collect books that have more than 200 pages 
more200 = [ s['author'] for s in books if s['pages'] > 200]
print(more200)
"""All variable used in inside a list comprenhension are private
and we dont have to worruy about such variable overwritting other variable with the same name

"""
x = 42
squares = [x*x for x in [1,2,3]]
print(squares)
print(x)
