#!/usr/bin/python3                                                                                                              
import psycopg2 
import keyring
import sys 

try:                                                                                                                             
        dbpass=sys.argv[1]                                                                                                       
except IndexError:                                                                                                               
        print ("UNKNOWN - no pass to db given") 
        sys.exit(3)                                                                                                                               
                                                                                                                         
try:                                                                                                                             
        conn = psycopg2.connect(host='192.168.0.103',user='centreon',password=dbpass,dbname='cyberstarter')         
except:                                                                                                                          
        print("UNKNOWN - Can't connect to database")                                                                     
        sys.exit(3)                                                                                                              
                                                                                                            
cur=conn.cursor()                                                                                                                
cur.execute("SELECT extract(epoch from(now() at time zone ('utc') - datein)) as diff FROM public.cs order by datein desc limit 1")                                             
row=cur.fetchone()                                                                                                               
if row is not None:                                                                                                              
        if row[0]:                                                                                                               
                dbtime=int(row[0])                                                                                                                                                                                
                if dbtime>1800:                                                                                          
                        print("CRITICAL - last update is older than 30'")                                                      
                        sys.exit(2)                                                                                              
                elif dbtime>900:                                                                                         
                        print ("WARNING - last update is older than 15'")                                                        
                        sys.exit(1)                                                                                              
                else:                                                                                                            
                        print ("OK - everything seems to be all right")                                                            
                        sys.exit(0)                                                                                              
        else:                                                                                                                    
                print("UNKNOWN - no value was return")                                                   
                sys.exit(3)                                                                                                      
else:                                                                                                                            
        print ("UNKNOWN - can't find this ID in db")                                                                          
        sys.exit(3)
