import psycopg2
import psycopg2.extras as ext


def run_sql(sql, values=None):
    conn = None
    results = []
    try:
        # connect creates a db connection
        conn = psycopg2.connect("dbname='task_manager'")
        # conn.cursor() creates a cursor responsible for executing our queries, in this case we are using a dictionary, use RealDictCursor for dictionary view. I.E. cur = conn.cursor(cursor_factory=ext.RealDictCursor)
        # Zsolt has said we can use DictCursor even tho it doesn't always work well with psycopg2
        # If you don't tell the cursor_factory was data type to return, it will return a list of truples as standard
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        # execute will run the sql query with appropriate values
        cur.execute(sql, values)
        # commit will finalise our transaction created above
        conn.commit()
        # fetchall will return all results from our sql query above
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results

######################################################################################################################

# My code - error somewhere so copied Zsolt's instead. Will review later... maybe.

# import psycopg2
# import psycopg2.extras as ext

# # run_sql.py established a connection to the SQL database

# # This does not need a class, as we are not generating objects here, just running a function to connect to the database

# # conn is a psycopg convention word (can be anything if you like) to represent a connection. We set it to None so the conn.close at the end of this function can work better

# # results[] is for returns from the database. It is always a list as we may want multiple returns.

# # psycopg has a function .connect(). for connections to SQL, note the datebase must be in a string... and then the database name must be in a second string. "''" basically. Looks kind of ugly but it is how SQL works.

# # cur (cursor) creates a cursor responsible for executing our queries & returns the data as a dictionary (key value pairs)

# # cur.execute is like a git add, prepares info for commiting

# # conn.commit() commits info to database

# # cur.fetchall() will return all results from our queries

# # cur.close() closes the cursor as if it was left open, memory issues would soon occur

# # We add a try: and except () so if anything goes wrong, we will be told in the terminal and can fix it easily

# # conn.close() is used again here (in finally) to close the database if an error occurs

# # return the list which hopefully now contains the results of the sql query

# def run_sql(sql, values = None):
#     # INSERT INTO tasks (description, assignee, duration, completed)
#     # VALUES ('Buy milk', 'Zsolt', '5 mins' True)
#     conn = None
#     results = []

#     try:
#         conn = psycopg2.connect("dbname='task_manager'")
#         cur = conn.cursor(cursor_factory=ext.DictCursor)
#         cur.execute(sql, values)
#         conn.commit()
#         results = cur.fetchcall()
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#     return results
