import sqlite3
#import necesary module for database manipulation


#connecting to the database
def connect_to_db():

    global connection
    connection = sqlite3.connect('DINERS.db')
    print ("connected to database DINERS")


#creates tables provider and canteen
def create_table():
    connection.execute('''CREATE TABLE PROVIDER
             (ID INT PRIMARY KEY     NOT NULL,
             PROVIDERNAME          VARCHAR(30))''')


    connection.execute('''CREATE TABLE CANTEEN
             (ID INT PRIMARY KEY     NOT NULL,
             PROVIDER_ID INT,
             NAME INT,
             LOCATION TEXT,
             TIME_OPEN   TIME,
             TIME_CLOSED TIME,
             FOREIGN KEY(PROVIDER_ID) REFERENCES PROVIDER(ID))''')

    print ("TABLES provider and canteen created")
    

#insert the data into the 2 above created tables
def insert_data():
   
    connection.execute("""INSERT INTO PROVIDER (ID,PROVIDERNAME) \
                 VALUES (1, 'Bitstop Kohvik OÜ')""");
    
    connection.execute("""INSERT INTO PROVIDER (ID,PROVIDERNAME) \
                 VALUES (2, 'Rahva Toit'),
                        (3, 'Baltic Restaurants Estonia AS'),
                        (4, 'TTÜ Sport')""");
    

    connection.execute("INSERT INTO CANTEEN (ID,PROVIDER_ID,NAME,LOCATION,TIME_OPEN,TIME_CLOSED) \
                VALUES (1,1,'bitStop CAFE','IT College','09:30','16:00')");
    
    connection.execute("""INSERT INTO CANTEEN  (ID,PROVIDER_ID,NAME,LOCATION,TIME_OPEN,TIME_CLOSED) \
                VALUES (2,2,'SOC canteen','SOC- building','08:30','18:30'),
                    (3,2,'Library canteen','Library Building','08:30','19:00'),
                    (4,3,'Main building Deli cafe','U01 Building','09:00','16:30'),
                    (5,3,'Main building Daily lunch restaurant','U01 Building','09:00','16:30'),
                    (6,2,'U06 building canteen','U06 Building','09:00','16:00'),
                    (7,3,'Natural Science building canteen','SCI building','09:00','16:00'),
                    (8,3,'ICT building canteen','ICT Building','09:00','16:00'),
                    (9,4,'Sports building canteen','S01 building','11:00','20:00')""");
    

    connection.commit()
    print ("Diners registered")


#query for canteens which close after 18:00 and open before 16:15 and print them
def showopen():
    cursor = connection.execute("""SELECT ID,PROVIDER_ID,NAME,LOCATION,TIME_OPEN,TIME_CLOSED
                     from CANTEEN where TIME_CLOSED >='18:00' and TIME_OPEN <='16:15'""")
    for row in cursor:
       for i in row:
           print(i,end=' ')
       print()


#query for canteens that are provided by rahva toit and print them
def showrahva():
    cursor = connection.execute("""SELECT ID,PROVIDER_ID,NAME,LOCATION,TIME_OPEN,TIME_CLOSED
                     from CANTEEN where PROVIDER_ID=2""")
    for row in cursor:
       for i in row:
           print(i,end=' ')
       print()
    
#closes the connection to the database
def closeconn():
    
    connection.close()
    print ("disconnected from db")
    
#if imported doesnt run tests
if __name__ == "__main__":
    connect_to_db()
    #create_table()
    #insert_data()
    print('------------open close interval query---------')
    showopen()
    print('---------------rahva toit query--------------')
    showrahva()
    
    closeconn()