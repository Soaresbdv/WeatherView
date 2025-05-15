import sqlite3

def listar_tabelas(caminho_bd):
    print(f"\n--- Verificando banco: {caminho_bd} ---")
    try:
        conn = sqlite3.connect(caminho_bd)
        cursor = conn.cursor()

        # Lista tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        print("Tabelas encontradas:", tabelas)

        # Se tiver tabela de usuários, tenta listar os dados
        for tabela in tabelas:
            nome = tabela[0]
            if "user" in nome.lower() or "usuarios" in nome.lower():
                print(f"\nDados da tabela '{nome}':")
                cursor.execute(f"SELECT * FROM {nome}")
                linhas = cursor.fetchall()
                for linha in linhas:
                    print(linha)

        conn.close()
    except Exception as e:
        print("Erro:", e)

# Caminhos dos 3 bancos
bancos = [
    "instance/database.db",
    "instance/site.db",
    "instance/weatherview.sqlite"
]

for caminho in bancos:
    listar_tabelas(caminho)
