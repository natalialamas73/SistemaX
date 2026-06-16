import sqlite3
from html import escape


def buscar_produto(termo_busca):
    if not termo_busca or not termo_busca.strip():
        return "<ul></ul>"

    try:
        with sqlite3.connect("ecommerce.db") as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT nome, preco, descricao
                FROM produtos
                WHERE nome LIKE ?
                """,
                (f"%{termo_busca.strip()}%",)
            )

            resultados = cursor.fetchall()

        itens = [
            f"<li>{escape(nome)} - R${preco}: {escape(descricao or '')}</li>"
            for nome, preco, descricao in resultados
        ]

        return f"<ul>{''.join(itens)}</ul>"

    except sqlite3.Error:
        # Aqui você poderia registrar o erro em log
        return "<p>Erro ao buscar produtos.</p>"
