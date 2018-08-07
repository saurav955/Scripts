from lxml import etree
import MySQLdb

with open('test.html', 'r') as content_file:
    s = content_file.read()

table = etree.HTML(s).find("body/table")
rows = iter(table)
headers = [col.text for col in next(rows)]

conn = MySQLdb.connect('localhost', 'root', 'passwd', 'db_name')
cur = conn.cursor()
for row in rows:
    row_values = [col.text for col in row]
    query_string = 'insert into table_name(Event_ID, Project_Name, Event_Details, Start_Date, End_Date) values (%s, %s, %s, %s, %s);'
    cur.execute(query_string, row_values)
    conn.commit()
