'''Unit tests for the SQL portion of the final assessment part 1'''
import unittest2 as unittest
from submissions import sql as s
import numpy as np
import psycopg2

# from code import assessment as a


def run_sql_query(command, dbname='applications', username='emily'):
    '''
    Copied from tests.py
    '''
    if not command:
        return []
    con = psycopg2.connect(dbname=dbname, user=username, host='/tmp')
    c = con.cursor()
    data = c.execute(command)
    return [d for d in data]
    # con.commit()
    con.close()

def read_sql(sqlfile='sql_questions.sql'):
    '''
    Read sql queries
    Assuming semicolon at the end of each command
    '''
    with open(sqlfile) as f:
        'read commands, split on ;'
        commands = f.read()
        commandslist = commands.split(';')
    sql_commands = []
    for item in commandslist:
        if not item.isspace():
            # account for trailing newlines
            sql_commands.append(item + ';')
    return sql_commands


class Test_Sql(unittest.TestCase):


    def test_sql_queries_1(self):
    '''Did not replace with solution yet
    query 1 = index 0
    '''

    query = sql_commands[0]
    result = run_sql_query(query)
    # need to figure out test results

    self.assertEqual(len(result), 177)
    sf, portland = None, None
    for line in result:
        if line[0] == 'San Francisco':
            sf = int(line[2])
        elif line[0] == 'Portland' and line[1] == 'ME':
            portland = int(line[2])
    self.assertEqual(sf, 62)
    self.assertEqual(portland, 13)


def test_sql_queries_2(self):
    query = sql_commands[0]
    result = run_sql_query(query)
    # need to figure out test results
    


if __name__ == "__main__":
    sql_commands = read_sql()
    unittest.main()


#
# ### 2. SQL (10 minutes)
#
# You have a SQL database which contains information about what jobs students have applied to. You have three tables with this structure:
#
#     companies: id, name
#     students: id, name
#     applications: comp_id, stud_id, date
#
# The data is stored the SQL dump `applications.sql`. Recall that the steps for loading the database into postgres:
#
# * Make sure the Postgres server is running (open Postgres.app)
# * In the command line, run `psql` to open postgres command line.
# * In postgres run: `CREATE DATABASE applications;`
# * Exit postgres and in the command line run: `psql applications < applications.sql`
# * Open the postgres database: `psql applications`
#
# Don't read too much into the "data". It was created randomly.
#
# Put the SQL for the following queries in `sql_queries.sql`.
#
#
# 1. Write a SQL query which gives all of the students who applied to a job before June 1 (dates are in the form "2014-06-01"). Your result should have these columns: `id, name`.
#
# 2. Write a SQL query which gives a count of how many students applied to each company. Your result should contain three columns: `id, name, cnt`. You should include companies in your result which have 0 applicants.
#     <br />
