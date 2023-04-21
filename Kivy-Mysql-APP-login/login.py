from kivy.app import App 
import configparser
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.toast import toast
from datetime import datetime
import mysql.connector

class Login(Screen):
    pass
    def connect(self):
        app= App.get_running_app()
        input_email = app.manager.get_screen('login').ids['input_email'].text
        input_password = app.manager.get_screen('login').ids['input_password'].text
        config = configparser.ConfigParser()
        config.read('config.ini')

        user = 'sql5524925'
        host = 'sql5.freesqldatabase.com'
        password = 'IQ5b1P8ejY'
        dbname = 'sql5524925'
        db = mysql.connector.connect(host = str(host), user = str(user), password = str(password), database = str(dbname))
        #db = mysql.connect.connect
        cursor = db.cursor()

        query="SELECT count(*) FROM users where email='"+str(input_email)+"' and password = '"+str(input_password)+"'"
        cursor.execute(query)
        data= cursor.fetchone()
        count =data[0]
        if count == 0:
            toast('Password Invalido')
        else:
            toast('Login y password son correctos')
            now = datetime.now()
            query = "update users set last_login='"+str(input_email)+"' and password = '"+str(input_password)+"'"
            cursor.execute(query)
            db.commit()
        db.close()
        pass 
