import mysql.connector
def DataUpdate(name,mobile,email):
    mydb = mysql.connector.connect( host="localhost", user="root", passwd="root", database="Rasa_data")
    mycursor = mydb.cursor()
    sql='INSERT INTO rasa_data (Name, Mobile, Email) VALUES ("{0}","{1}", "{2}");'.format(name,mobile,email)
    mycursor.execute(sql)
    mydb.commit()
