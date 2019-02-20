import csv

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://luxykokzxogfhs:a55b18e41f1182e2e6acfde3c5d5b593f3e1b582371fee354852ab8dbfe3aa9f@ec2-54-163-246-159.compute-1.amazonaws.com:5432/d7c2uit666hcnj')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader)
    for isbn,title,author,year in reader:
        db.execute("INSERT INTO books (ISBN, Title, Author, year) VALUES (:isbn, :title, :author, :year)",
                   {"isbn": isbn, "title": title, "author": author, "year": year})
        db.commit()
        print(f"Added book with isbn {isbn} title {title} author {author} and year {year}.")



if __name__ == "__main__":
    main()




