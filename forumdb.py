# "Database code" for the DB Forum.

import datetime

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""
  psycopg2.connect("dbname=forum") 
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  return c.fetchall()
  db.close()
  # return reversed(POSTS)

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  # POSTS.append((content, datetime.datetime.now()))
  psycopg2.connect("dbname=forum") 
  c = db.cursor()
  # c.execute("insert into posts values('%s')" % content)
  c.execute("insert into posts values('%s')" ,(content,))
  db.commit()
  db.close()

