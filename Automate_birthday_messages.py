from telethon import TelegramClient
from datetime import datetime
import mysql.connector

class Automate_birthday_messages:

    def __init__(self, app_id, app_hash, session_file_name, username_receiver, msg):
        self.app_id = app_id
        self.app_hash = app_hash
        self.session_file_name = session_file_name
        self.username_receiver = username_receiver
        self.msg = msg


    def send_msg(self, username_receiver, msg):
        try:
            with TelegramClient(self.session_file_name, self.app_id, self.app_hash) as client:
                client.loop.run_until_complete(client.send_message(username_receiver,msg))
        except Exception as e:
            #print(e)
            return f"Error sending message to: {username_receiver}, error: {e}"
        return "Success" # enviar também no texto o user name
    

    #criar metodo para iteracao

    dic_birthdays = {"mamy":"1961-10-26", 
                "Alexandre":"2023-09-23",
                "test":"2024-05-06" }

    def check_dates_and_send_message(self, dic):
        
        todays_date = datetime.today().strftime('%Y-%m-%d')
        print("Today's date:", todays_date)
           
        for contact_entry in dic:
            contact_entry,dic[contact_entry]

        #testing that is working
        if dic[contact_entry] == todays_date:
            #print("you are amazing")
            #print(self.send_msg(value, "Parabens"))
            return self.send_msg(contact_entry, "Parabens")

#criar metedo para coneccao bd

    def connect_to_mysql_and_get_cursor(self,host,port,user,password,db):
        try:
            # Establish connection to the database
            connection = mysql.connector.connect(
                host="172.17.0.1",
                port=33060,
                user="root",
                password="your_password",
                database="birthday_db"
            )
            print("Connected to MySQL database successfully!")
            
            # Create a cursor
            cursor = connection.cursor()
            
            # Return both the connection and the cursor
            return connection, cursor
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None, None

# Example usage:
# connection, cursor = connect_to_mysql_and_get_cursor()


       
