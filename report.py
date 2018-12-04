#!/usr/bin/env python3
import psycopg2


if __name__ == '__main__':
    query1 = """select title, count(title) as views
                from articles
                join log on log.path like concat('/article/',articles.slug)
                group by title
                order by views desc
                limit 3;"""

    query2 = """select name,
                    sum(views) total_views
                from (select
                        name,
                        count(title) as views
                    from articles
                    join
                        log on log.path like concat('/article/',articles.slug)
                    join authors on authors.id = articles.author
                    group by name,title
                    order by views desc) as AuthorsViews
                group by name
                order by total_views desc;"""

    query3 = """select *
                from   (select time::date as day,
                            count(case when status not like '200%'
                                         then 1
                                         else null end)::float
                                         * 100
                                         / count(status) as error_percentage
                        from log
                        group by day)
                        as final_result
                where error_percentage > 1
                order by error_percentage desc;"""

    news_db = psycopg2.connect(database='news')
    cursor = news_db.cursor()

# ------------------------- first report -----------------
    print('1- The most popular three articles of all time')
    cursor.execute(query1)
    data = cursor.fetchall()

    for row in data:
        result = "\"%s\" - %d views"
        print(result % (row[0], row[1]))

    print('--------------- end of report -----------------\n\n')

# ------------------------- second report -----------------
    print('2- The most popular article authors of all time')
    cursor.execute(query2)
    data = cursor.fetchall()

    for row in data:
        result = "%s - %d views"
        print(result % (row[0], row[1]))

    print('--------------- end of report -----------------\n\n')

# ------------------------- third report -----------------
    print('3- The days with more than 1% of errors requests')
    cursor.execute(query3)
    data = cursor.fetchall()

    for row in data:
        result = "%s - %.2f%% errors"
        print(result % (row[0], round(row[1], 2)))

    print('--------------- end of report -----------------')
