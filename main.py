from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

if __name__ == "__main__":
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
else:
    app.config['MYSQL_HOST'] = 'iyappangs.mysql.pythonanywhere-services.com'
    app.config['MYSQL_USER'] = 'iyappangs'
    app.config['MYSQL_PASSWORD'] = 'supersecuredbpassword'

app.config['MYSQL_DB'] = 'spotifybackend'
mysql = MySQL(app)
app.app_context().push()
conn = mysql.connection

# creating tables

cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS albums (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    releaseYear VARCHAR(4) NOT NULL
  );
  """)

cursor.execute("""
  CREATE TABLE IF NOT EXISTS songs (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR NOT NULL,
    album_id VARCHAR(36),
    FOREIGN KEY (album_id) REFERENCES albums(id)
  );
  """)
conn.commit()
cursor.close()


@app.route('/')
def index():
    return 'hi mom'


if __name__ == "__main__":
    app.run()
