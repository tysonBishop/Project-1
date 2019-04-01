import psycopg2
import argparse


def query_db(query):
    db = psycopg2.connect(database="news")
    cursor = db.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


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


def analyze():
    parser = argparse.ArgumentParser(
        description="Data analysis from the log database."
    )
    parser.add_argument(
        "-Most_Read_Articles",
        help="Display articles with the most read on top.",
        action='store_true',
    )
    parser.add_argument(
        "-Most_Read_Authors",
        help="Display popular authors, those with the"
             "most article reads on top.",
        action='store_true',
    )
    parser.add_argument(
        "-errors",
        help="Display dates where more than 1%% of requests were errors.",
        action='store_true',
    )

    args = parser.parse_args()
    if args.reads:
        most_read_articles()
    if args.authors:
        most_popular_authors()
    if args.errors:
        most_error_days()
    else:
        parser.error("Please specify an argument :/")


if __name__ == "__main__":
    analyze()
