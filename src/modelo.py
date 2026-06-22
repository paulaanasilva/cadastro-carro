from database import conectar

#Alteração de Teste

#def criar_modelo(nome, id_marca):
#Fazendo uma alteração aleatória para testar o commit


def listar_modelos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            modelo.id,
            modelo.nome,
            marca.nome
        FROM modelo
        INNER JOIN marca
            ON modelo.id_marca = marca.id
    """)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados


def atualizar_modelo(id, nome, id_marca):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE modelo
        SET nome = %s,
            id_marca = %s
        WHERE id = %s
        """,
        (nome, id_marca, id)
    )

    conn.commit()

    cursor.close()
    conn.close()


#def excluir_modelo(id):
