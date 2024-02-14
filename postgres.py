import keygen 
import psycopg2

def postgres_connect(query,commit=0):
        postgres= keygen.postgres_auth()
        res=[]
        err=""
        try:
            connection = psycopg2.connect(user=postgres[0],
                            password=postgres[1],
                            host=postgres[2],
                            database=postgres[3])
            cursor = connection.cursor()
            cursor.execute(query)
            #print(query)
            if commit==1:
                connection.commit()
            else:
                res=cursor.fetchall()
                #print(res)
            if connection:
                        cursor.close()
                        connection.close()
        except (Exception, psycopg2.Error) as error:
                print(error)
                err= str(error)
                
        if commit ==1 and len(err)<1:
            return 1
        elif commit ==1 and len(err)>0:
            return 0 
        return res,err
