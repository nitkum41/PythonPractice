import mysql.connector
from mysql.connector import Error

def call_using_select(cursor):
    function_query = """
    select customerName, CustomerLevel(creditLimit) from customers;
    """
    cursor.execute(function_query)
    function_query_data = cursor.fetchall()

    # print results
    print("Printing Status By Country", function_query_data, type(function_query_data))

    test_query = """
                select customerName,
            case 
                when creditLimit > 50000 then "PLATINUM"
                when (creditLimit >= 10000) and (creditLimit <= 50000) then "GOLD"
                when creditLimit < 10000 then "SILVER"
            end as custLevel from customers;
    """

    cursor.execute(test_query)
    test_query_data = cursor.fetchall()

    # print results
    print("Printing Status By Country", test_query_data, type(test_query_data))

    #compare
    print(function_query_data==test_query_data)



def call_using_stored_procedure(cursor):
    ##check procedure exists
    cursor.execute("show procedure status where name ='GetCustomerLevel'")
    result = cursor.fetchone()
    if result[1] == "GetCustomerLevel":
        print("stored procedure exists")
    else:
        print("stored procedure does not exists")

    #call procedure
    data=cursor.callproc('GetCustomerLevel',(103,0))
    print(data)

    ##
    test_query = """select customerName,
            case 
                when creditLimit > 50000 then "PLATINUM"
                when (creditLimit >= 10000) and (creditLimit <= 50000) then "GOLD"
                when creditLimit < 10000 then "SILVER"
            end as custLevel from customers where customerNumber="103";
    """

    # print results
    cursor.execute(test_query)
    test_query_data = cursor.fetchall()
    print("Printing Status By Country", test_query_data, type(test_query_data))


    print(data[1]==test_query_data[0][1])



try:
    connection = mysql.connector.connect(host='localhost',
                                         database='classicmodels',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)

        ##check function exists
        cursor = connection.cursor()
        cursor.execute("show function status where name='CustomerLevel'")
        record = cursor.fetchone()
        if(record[1]=="CustomerLevel"):
            print("stored function exists")
        else:
            print("stored function not exist")

        # call_using_select(cursor)

        call_using_stored_procedure(cursor)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")