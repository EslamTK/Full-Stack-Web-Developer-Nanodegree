#! /usr/bin/env python3

""" This module is to connect to the news database & perform queries to it """

import psycopg2

# Connect to the database
connect = psycopg2.connect('dbname=news')
cursor = connect.cursor()


def get_top_articles():
    """ Function to get the top 3 articles in view """
    sql = '''SELECT title, views
             FROM articles, articles_views
             WHERE articles.slug = articles_views.id
             ORDER BY views DESC
             LIMIT 3;'''
    cursor.execute(sql)
    return cursor.fetchall()


def get_top_authors():
    """ Function to get the authors ordered by the view of their articles """
    sql = '''SELECT authors.name, SUM(views) AS views
             FROM articles_views, authors
             LEFT JOIN articles ON authors.id = articles.author
             WHERE articles.slug = articles_views.id
             GROUP BY author,authors.name
             ORDER BY views DESC;'''
    cursor.execute(sql)
    return cursor.fetchall()


def get_requests_fail_days():
    """ Function to get the days on which the requests
    lead to more than 1% errors """
    sql = '''SELECT to_char(DATE(time),'FMMonth DD, YYYY'),
             ROUND(
             (COUNT(CASE WHEN status LIKE '4%' THEN 1 ELSE NULL END)::NUMERIC /
             COUNT(*)::NUMERIC)*100,
             2) AS percentage
             FROM log
             GROUP BY DATE(time)
             HAVING percentage > 1;'''
    cursor.execute(sql)
    return cursor.fetchall()


def close_conn():
    """ Function to close the connection to the database """
    if cursor:
        cursor.close()
    if connect:
        connect.close()


def print_table(fun):
    """ Function to format the query result table that takes the function
    which do the query as a parameter """
    if fun == get_top_articles:
        count_type = ' views'
        print('Top 3 Articles:')
    elif fun == get_top_authors:
        count_type = ' views'
        print('Top Authors:')
    else:
        count_type = '% errors'
        print('Days With More Than 1% Errors:')
    rows = fun()
    for row in rows:
        print("%s - %s%s" % (str(row[0]), str(row[1]), count_type))
    print()


# Run the queries & Print the result tables if the module run as the main point
# & not imported
if __name__ == '__main__':
    print_table(get_top_articles)
    print_table(get_top_authors)
    print_table(get_requests_fail_days)
    close_conn()
