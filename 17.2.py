#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Author: Daniel Bon Durant
# Advanced Python Programming
# Due: 12/15/2023
# Description: This program will expirement with SQLite. 
#The goal is to follow chapter 17.2 of the textbook and the example given.
#Additionally, this program will contain exercize 17.1 on page 799 of the textbook.
#The exercise feels like a continuation of 17.2 so I decided to keep it in the same program.


# In[60]:


print('''Author: Daniel Bon Durant
Advanced Python Programming
Due: 12/15/2023
Description: This program will expirement with SQLite. 
The goal is to follow chapter 17.2 of the textbook and the example given. 

Additionally, this program will contain exercize 17.1 on page 799 of the textbook.
The exercise feels like a continuation of 17.2 so I decided to keep it in the same program.
''')


# In[18]:


import sqlite3


# In[19]:


#establish a connection and create an object regarding the database
connection = sqlite3.connect('books.db')


# In[20]:


import pandas as pd

#display 10 columns maximum
pd.options.display.max_columns = 10

#read the Sql authors table from the connection object, index is the id column
# * means get all the columns from authors table
pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])


# In[21]:


#view title tables contents
pd.read_sql('SELECT * FROM titles', connection)


# In[22]:


#view author_ISBN tables contents
df = pd.read_sql('SELECT * FROM titles', connection)

#SHow just the first few lines
df.head()


# In[23]:


#create a select query
pd.read_sql('SELECT first, last FROM authors', connection)


# In[25]:


#select only rows that match criteria using WHERE
pd.read_sql("""SELECT title, edition, copyright
FROM titles
WHERE
copyright > '2016'""", connection)


# In[26]:


#select only authors who's last name starts with d. Provide id, first and last name in results
#id will be index column
pd.read_sql("""SELECT id, first, last
FROM authors
Where last LIKE 'D%'""",
           connection, index_col=['id'])


# In[29]:


#select rows of all authors whos last name start with any character followed by a b, with any more characters being ok
pd.read_sql("""SELECT id, first, last
FROM authors
WHERE first LIKE '_b%'""",
connection, index_col=['id'])


# In[30]:


#sort a query results in  ascending order
pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection )


# In[31]:


#sort by multiple columns
pd.read_sql("""SELECT id, first, last
FROM authors
ORDER BY last, first""",
connection, index_col=['id'])


# In[32]:


#sort by multiple columns in descending order
pd.read_sql("""SELECT id, first last
FROM authors
ORDER BY
last DESC, first ASC""""",
connection, index_col=['id'])


# In[33]:


#combine WHERE and ORDER BY clauses
pd.read_sql("""SELECT isbn, title, edition, copyright
FROM titles
WHERE title LIKE '%How to Program'
ORDER BY title""",
connection)


# In[34]:


#merge data from multiple tables
pd.read_sql("""SELECT first, last, isbn
FROM authors
INNER JOIN author_ISBN
    ON authors.id = author_isbn.id
ORDER BY last, first""""", connection).head()


# In[35]:


#initialize cursor object
cursor = connection. cursor()


# In[37]:


#insert new row to table using cursor execute
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('SUE', 'Red')""")


# In[38]:


#read the authors table contents to check for new values
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[39]:


#see how many rows were modified
cursor.rowcount


# In[40]:


#list author tables content
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[41]:


#DELETE from statement
cursor = cursor.execute('DELETE FROM authors WHERE id=6')


# In[42]:


cursor.rowcount


# In[43]:


#verify deletion from authors table 
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[ ]:


#-----------------------------------------BEGIN EXCERCISE 17.1--------------------------------------------------------------


# In[47]:


#Select from titles table alll tittles and edition numbers in descending order by edition number. show only first three
pd.read_sql("""SELECT last, first FROM authors
ORDER BY last DESC, first""""", connection)
#DESC means descending


# In[50]:


#select all book titles from the titles table in ascending order
pd.read_sql("""SELECT * FROM titles
ORDER BY title""""", connection)


# In[59]:





# In[56]:


#insert new row to table author using cursor execute
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Daniel', 'BonDurant')""")


# In[57]:


#read the authors table contents to check for new values
pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[58]:


connection.close()


# In[ ]:




