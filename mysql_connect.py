import mysql
def get_connection() :
    connection = mysql.connector.connect(
        host = 'database-1.cibdadxvyc3i.us-east-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '2105'
    )
    return connection