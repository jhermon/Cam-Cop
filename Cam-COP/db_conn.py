import psycopg2
from fuzzywuzzy import fuzz

#connect to the db
def get_details(plate_number):
    try:
        connection = psycopg2.connect(user = "postgres",password = "test",host = "127.0.0.1",database = "Camcop")
        cursor = connection.cursor()

        cursor.execute(f"SELECT EXISTS(SELECT * FROM car_details WHERE license_plate ='{plate_number}')") 
        check = cursor.fetchone()
        if check[0]== True:
            cursor.execute(f"SELECT driver_details.firstname, driver_details.lastname,driver_details.gender,driver_details.trn,driver_details.address,driver_details.dob,car_details.car_brand,car_details.car_color,car_details.year_model,car_details.year_of_purchase FROM driver_details INNER JOIN car_details ON driver_details.license_plate = car_details.license_plate WHERE car_details.license_plate = '{plate_number}' ")
            rows = cursor.fetchall()
            for r in rows:
                #print(f"firstname: {r[0]}\nlastname: {r[1]}\nGender: {r[2]}\nTRN: {r[3]}\nAddress: {r[4]}\nDOB: {r[5]}\nCar Brand: {r[6]}\nCar color: {r[7]}\nYear made: {r[8]}\nYear Purchased: {r[9]}")
                get_details.lst=[r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]]
        else:
            cursor.execute('SELECT license_plate FROM car_details')
            lic_num = cursor.fetchall()
            get_details.lst=[]
            for l in lic_num:
                if fuzz.ratio(plate_number,l[0])>= 65:
                    get_details.lst.append((fuzz.ratio(plate_number,l[0]),l[0]))
            get_details.lst = sorted(get_details.lst,reverse=True)
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
    return get_details.lst
#get_details('7145FW')


