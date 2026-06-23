from database import conectar

def criar_marca(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO marca(nome) VALUES (%s)",
        (nome,)
    )

    conn.commit()
    conn.close()


def listar_marcas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome
        FROM marca
    """)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados



#def atualizar_marca(id, nome):



#def excluir_marca(id):
