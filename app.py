
from api.helloworldapi import HelloWorld
from logging import root
from flask import Flask, app
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
mysql= MySQL(app)
api = Api(app)

#parametros de conexion
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD'] = 'a3ACUARELA*'
app.config['MYSQL_DB']= 'myblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


class ProductosCategoriaAPI(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute ('''SELECT p.titulo, c.nombre as categoria 
        FROM myblog.post as p LEFT JOIN myblog.categoria as c 
        ON p.idcategoria = c.idcategoria WHERE p.idcategoria ='''+id )
        result = cur.fetchall()
        return str(result)
class CategoriaAPI(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute ("SELECT * FROM categoria")
        result = cur.fetchall()
        return str(result)
class PostAPI(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute ("SELECT * FROM post")
        result = cur.fetchall()
        return str(result)




api.add_resource(HelloWorld, '/hello')
api.add_resource(CategoriaAPI, '/categoria')
api.add_resource(PostAPI, '/post')
api.add_resource(ProductosCategoriaAPI, '/categoria/<id>/posts')