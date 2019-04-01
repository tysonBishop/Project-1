import psycopg2


def query_db(query):
    db = psycopg2.connect(database="news")
    cursor = db.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data
    print results


def most_read_articles():
        articles = query_db("SELECT * FROM most_read;")

    print("Most Popular articles:")
    for article, views in articles:
    print(u"%s — %d views" % (article, views))


def most_popular_authors():
    authors = query_db("SELECT * FROM most_popular;")

    print("\nMost Popular Authors:")
    for author, views in authors:
    print(u"%s — %d views" % (author, views))


def most_error_days():
        days = query_db("SELECT * FROM most_error_days;")

    print("\nDays where more than 1% of total requests resulted in errors")
    for day, percentage in days:
    print(u"%s — %.1f%%" % (day, percentage))



