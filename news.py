import psycopg2 #import psycopg2 library

def db_machine(query):
    #this is method will excute all the query we add in this program
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

def most_viewer_articles():
    # here we collect the most Viewer articles
    mostViewer = db_machine("""
        select title,count(*) as number
        from articles,log
        where articles.slug = substr(log.path, 10)
        group by articles.title
        order by number desc limit 3; """)

    # here will print the result of the query
    print("The most popular three articles:")
    i = 0
    while i < len(mostViewer):
        title = mostViewer[i][0]
        views = ": "+str(mostViewer[i][1])+" views"
        number = str(i+1)+" - "
        print(number+title+views)
        i = i+1

def most_popular_author():
    # here we collect the most popular author
    mostPopular = db_machine("""
        select authors.name, count(*) as number
        from authors,articles,log
        where (authors.id = articles.author) and (articles.slug = substr(log.path, 10))
        group by authors.name
        order by number desc; """)

    #print the result of this query
    print("\nThe most popular author:")
    i = 0
    while i < len(mostPopular):
        author = mostPopular[i][0]
        views = ": "+str(mostPopular[i][1])+" views"
        number = str(i+1)+" - "
        print(number+author+views)
        i = i+1

def requests_errors():
    # check and collect the error request that ocurre in site
    errors = db_machine("""
        select total_status.date,round(((error_status.error * 100.0)/total_status.status), 1) as percent
        from error_status,total_status
        where error_status.date=total_status.date
        order by percent desc; """)
        
    #print the result of the query
    print("\nOn which days did more than 1% of requests lead to error: ")
    i = 0
    while i < len(errors):
        if errors[i][1] >= 1: #check if the rate greater than 1 percent or not
            date = errors[0][0].strftime("%B %d,%Y")
            errorRate = ": "+str(errors[i][1])+"% errors"
            print(date+errorRate)
        i = i+1

if __name__ == '__main__':
    #main
    most_viewer_articles()
    most_popular_author()
    requests_errors()
