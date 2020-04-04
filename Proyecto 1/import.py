import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://rrjkyrln:ts_1CbU630y1vqHWrDyKTSiEkP6Go6GH@drona.db.elephantsql.com:5432/rrjkyrln')

db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        if(isbn != 'isbn'):
            db.execute("INSERT INTO registro_libro (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()

if __name__ == "__main__":
    main()
