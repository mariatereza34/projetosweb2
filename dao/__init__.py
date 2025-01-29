import psycopg2

#Conexão do banco
def conectardb():

    con = psycopg2.connect(
        dbname="projetosweb2",
        user="projetosweb2_user",
        password="OO1zrV3xzD8kRbvtZGsFMKZJYAilEsqr",
        host="dpg-cud39eogph6c738kpesg-a.oregon-postgres.render.com",
        port="5432"
    )
    return con

def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * from usuario where login='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(nome,login, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (nome,login,senha) VALUES ('{nome}','{login}','{senha}')"
        cur.execute(sql)


    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_produtos():
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT  * from produtos"
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_produto(tipo,cor,gb):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO produtos (tipo,cor,gb) VALUES ('{tipo}','{cor}','{gb}')"
        cur.execute(sql)


    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito