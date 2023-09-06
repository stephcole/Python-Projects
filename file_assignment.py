import sqlite3
conn = sqlite3.connect('test_file.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_testFile(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName STRING)")
    conn.commit
conn.close()

conn = sqlite3.connect('test_file.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_testFile (col_fileName) VALUES (?)", (x,))
            print(x)
conn.close()
