
import mysql.connector as mq
import datetime
import pyttsx3 as pt
'''
MySQL is one of the most popular database management systems (DBMSs) on the market today. 
we have used the Mysql in python for backend server for data store int db .it gives many
 functions to  data manage,data organaized step by step
and insert ,delete ,create and update etc


'''
# the program is coded by Chawbasanta


'''
pyttsx3 is a text-to-speech conversion library in Python.
Unlike alternative libraries, it works offline
'''


def Speak(audio):
    engine = pt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


def WishMe(self):  # This method is make for wishing me when we open the program

    self.hour = int(datetime.datetime.now().hour)
    if self.hour >= 0 and self.hour < 12:
        Speak('Goood Morning have a you nice today ')
    elif self.hour >= 12 and self.hour < 18:
        Speak('Good Afternoon')
    elif self.hour >= 18 and self.hour < 20:
        Speak('Good Evening')
    else:
        Speak('Goood night ')

# Student_management_system_database class


class DB_sms:
    # create new database needed by user
    def NEw_CreateDatabase(self):
        try:
            # make the connection
            self.conn = mq.connect(host='localhost', user='root', password='')
            Speak('Enter want you database name')
            self.db_name = str(input('Enter want you database name : '))
            self.cur = self.conn.cursor()
            self.sql = 'create database {0}'.format(self.db_name)
            if(self.conn.is_connected()):  # check the connection is True or False
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    self.sp = 'successfully created your {0} database'.format(
                        self.db_name)
                    Speak(self.sp)
                else:
                    self.sp = 'Unsuccessfully created your {0} database'.format(
                        self.db_name)
                    Speak(self.sp)

            else:
                Speak('Unuccessfully connection')

            self.cur.close()
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass

# use database after created by user in mysql with help of python
    def Use_database(self):
        try:
            Speak('Enter want you use database name')
            self.db_use = str(input('Enter want you use database name : '))
            self.conn = mq.connect(host='localhost', user='root', password='')
            self.cur = self.conn.cursor()
            self.sql = 'use {0}'.format(self.db_use)
            if(self.conn.is_connected()):
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    Speak('Successfully used '+self.db_use+' database')
                else:
                    Speak('Unsuccessfully used  '+self.db_use+' database')
            self.cur.close()
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass


# create new table after used database by user


    def createNew_table(self):
        try:
            Speak('enter want you create table name')
            self.table_name = str(input('enter want you table name :'))
            self.conn = mq.connect(
                host='localhost', user='root', password='', database=self.db_use)
            self.cur = self.conn.cursor()
            self.sql = ('''create table {0} (fname varchar(50) not null,lname varchar(50) not null,email varchar(50) not null,sex varchar(10) not null,passwords varchar(50) not null,conf_passwords varchar(50) not null,address varchar(70) not null,contact int(20) not null)''').format(self.table_name)
            if(self.conn.is_connected()):
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    self.conn.commit()
                    Speak('Successfully created  '+self.table_name + 'table')
                else:
                    Speak('unuccessfully created  '+self.table_name + 'table')
            self.cur.close()  # close the connection of databas
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass

    def drop_database(self):
        try:
            Speak('Enter want you drop database name')
            self.drop_db = str(input('Enter want you drop database name : '))
            self.conn = mq.connect(
                host='localhost', user='root', password='', database=self.drop_db)
            self.cur = self.conn.cursor()
            self.sql = 'drop database {0}'.format(self.drop_db)
            if(self.conn.is_connected()):
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    Speak('Successfully droped '+self.drop_db+' database')
                else:
                    Speak('Unsuccessfully used  '+self.drop_db+' database')
            self.cur.close()
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass

    def drop_table(self):
        try:
            Speak('Enter want you drop database name')
            self.drop_db = str(input('Enter want you drop database name : '))
            self.conn = mq.connect(
                host='localhost', user='root', password='', database=self.drop_db)
            self.cur = self.conn.cursor()
            self.sql = 'drop database {0}'.format(self.drop_db)
            if(self.conn.is_connected()):
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    Speak('Successfully droped '+self.drop_db+' table')
                else:
                    Speak('Unsuccessfully used  '+self.drop_db+' table')
            self.cur.close()
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass

    def show_databases(self):
        try:
            Speak(' you  can show databases')

            self.conn = mq.connect(host='localhost', user='root', password='')
            self.cur = self.conn.cursor()
            self.sql = 'show databases;'
            if(self.conn.is_connected()):
                if(self.conn.is_connected() != 0):
                    self.cur.execute(self.sql)
                    Speak('Successfully databases here available')
                else:
                    Speak('unsuccessfully databases are not available here')
            self.cur.close()
            self.conn.close()
        except:
            Speak('Unuccessfully connection please try again')
            pass


# WishMe()  # ,alert me every time

db = DB_sms()

while True:
    print()
    print('------------------- ! ! DATABASE Of SMS!!---------------------')
    print()
    print('------------------  [1] Create Database  --------------------')
    print('------------------  [2]   Use Database   --------------------')
    print('------------------  [3]   Create Table   --------------------')
    print('------------------  [4]   Drop Database  --------------------')
    print('------------------  [5]    Drop Table    --------------------')
    print('------------------  [6]   Show Database  --------------------')
    print('------------------  [7] Do you want exit --------------------')
    num = int(input('-------------------------------------------- : '))
    print()
    if num == 1:
        db.NEw_CreateDatabase()
    elif num == 2:
        db.Use_database()
    elif num == 3:
        db.createNew_table()
    elif num == 4:
        db.drop_database()
    elif num == 5:
        db.drop_table()
    elif num == 6:
        db.show_databases()
    elif num == 7:
        break
