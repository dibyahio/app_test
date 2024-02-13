import flask
import json
import requests 
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

app = flask.Flask(__name__, template_folder="Templates")
@app.route('/postgres', methods =['POST', 'GET'])
def postgres_sql():
    if flask.request.method == 'POST':
        res,err=postgres_connect("select * from therapy_db.bookings where id = 45445",commit=0)
        print(res)
        return flask.jsonify({'msg':"working"}),200
    else:
        return flask.jsonify({'msg':"error"}),400
if __name__ == '__main__':
    app.run(debug = True)
