import sqlite3
from sqlite3.dbapi2 import Cursor

def deletar_aluno(ida):
    try:
        con = sqlite3.connect("alunos.db")
        con.execute("DELETE FROM alunos WHERE id = ?",[ida])
        con.commit()
    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
    except Exception as e:
        print("Erro: ", e)
    else:
        print("Aluno Excluido Com Sucesso")
    finally:
        con.close()

def criar_tabela():
    try:
        con = sqlite3.connect("alunos.db")
        con.execute('''CREATE TABLE IF NOT EXISTS 'alunos' (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "Nome" TEXT NULL DEFAULT NULL,
        "Email" TEXT NULL DEFAULT NULL,
        "Endereco" TEXT NULL DEFAULT NULL,
        "Campus" TEXT NULL DEFAULT NULL,
        "Matricula" TEXT NULL DEFAULT NULL,
        "Periodo" INTEGER NULL DEFAULT 1,
        "av1" REAL NULL DEFAULT 0,
        "av2" REAL NULL DEFAULT 0,
        "av3" REAL NULL DEFAULT 0,
        "avd" REAL NULL DEFAULT 0,
        "avds" REAL NULL DEFAULT 0
        )''')
    except sqlite3.Error as e:
        print("Erro ao criar tabela, ", e)
    except Exception as e:
        print("Erro: ", e)
    finally:
        con.close()

def incluir_aluno(aluno):
    if len(aluno) == 6:
        try:
            con = sqlite3.connect("alunos.db")
            con.execute("INSERT INTO 'alunos' (Nome,Matricula,Email,Endereco,Campus,Periodo) VALUES (?,?,?,?,?,?)", aluno)
            con.commit()
        except sqlite3.Error as e:
            print("Erro: erro ao inserir aluno, ",e)
        except Exception as e:
            print("Erro: ", e)
        else:
            print("Aluno ", aluno[0], " Inserido com sucesso")
        finally:
            con.close()

def get_notas(id):
    try:
        con = sqlite3.connect("alunos.db")
        cur = con.cursor()
        cur.execute("SELECT av1,av2,av3,avd,avds FROM alunos WHERE id = ?",[id])
        row = cur.fetchone()
    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
        return None
    except Exception as e:
        print("Erro: ", e)
        return None
    else:
        return row
    finally:
        con.close()

def atualizar_notas(ida,notas):
    try:
        con = sqlite3.connect("alunos.db")
        query = "UPDATE alunos SET av1=?, av2=?, av3=?, avd=?, avds=? WHERE id = ?"
        con.execute(query,notas + (ida,))
        con.commit()
    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
    except Exception as e:
        print("Erro: ", e)
    else:
        print("Aluno Atualizado Com Sucesso")
    finally:
        con.close()

def atualizar_aluno(ida,aluno):
    try:
        con = sqlite3.connect("alunos.db")
        query = "UPDATE alunos SET Nome=?, Email=?, Endereco=?, Campus=?, Matricula=?,Periodo=? WHERE id = ?"
        con.execute(query,aluno + (ida,))
        con.commit()
    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
    except Exception as e:
        print("Erro: ", e)
    else:
        print("Aluno Atualizado Com Sucesso")
    finally:
        con.close()

def pegar_alunos(limite=20,hasLimit=True):
    try:
        con = sqlite3.connect("alunos.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos")
        row = ""
        if hasLimit:
            row = cur.fetchmany(size=limite)
        else:
            row = cur.fetchall()

    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
        return None
    except Exception as e:
        print("Erro: ", e)
        return None
    else:
        return row
    finally:
        con.close()

def pegar_aluno(id):
    try:
        con = sqlite3.connect("alunos.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM alunos WHERE id = ?",[id])
        row = cur.fetchone()
    except sqlite3.Error as e:
        print("Erro: erro ao inserir aluno, ",e)
        return None
    except Exception as e:
        print("Erro: ", e)
        return None
    else:
        return row
    finally:
        con.close()