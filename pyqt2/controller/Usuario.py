

#interna
from controller.Banco import Banco
banco = Banco()

from controller.middleware.UsuarioMiddleware import UsuarioMiddleware


class Usuario:

    @staticmethod
    def cadastrar(dados = {}):
        if (UsuarioMiddleware.checkEmail(email = dados["email"])
            and
            UsuarioMiddleware.checkTelefone(numero = dados["telefone"])
            and
            UsuarioMiddleware.checkCPF(cpf = dados["cpf"])):

            for values in dados.values():
                values = str(values)

            banco.conectar()
            consulta = "INSERT INTO usuarios(nome, email, telefone, cpf, cep, bairro, rua, numero) VALUES (:nome, :email, :telefone, :cpf, :cep, :bairro, :rua, :numero)"
            banco.cursor.execute(consulta, dados)
            
            banco.conn.commit()
            banco.conn.close()
        else:
            print("ALGO DEU ERRADO")

    @staticmethod
    def getDados():
        banco.conectar()

        consulta = "SELECT * FROM usuarios"
        banco.cursor.execute(consulta)
        data = banco.cursor.fetchall()
        
        banco.conn.close()
        return data

    @staticmethod
    def getDadosById(id = ""):
        banco.conectar()

        #verificando se o id existe
        consulta = "SELECT * FROM usuarios WHERE id = ?"
        banco.cursor.execute(consulta, (id))
        resultado = banco.cursor.fetchone()
        banco.conn.close()
        return resultado   
    
    @staticmethod
    def getDadosByCPF(cpf = ""):
        banco.conectar()

        #verificando se o id existe
        consulta = "SELECT * FROM usuarios WHERE cpf = ?"
        banco.cursor.execute(consulta, (cpf,))
        resultado = banco.cursor.fetchone()
        banco.conn.close()

        return resultado   
        
    @staticmethod
    def deleteById(id = ""):
        banco.conectar()

        #verificando se o id existe
        consulta = "SELECT * FROM usuarios WHERE id = ?"
        banco.cursor.execute(consulta, (id))
        resultado = banco.cursor.fetchone()
        if (resultado):

            consulta = "DELETE FROM usuarios WHERE id = ?"
            banco.cursor.execute(consulta, (id))
            banco.conn.commit()
            banco.conn.close()
            return True
        else:
            banco.conn.close()
            return False

    def update(id = "", dados_update= {}):
        dados = Usuario.getDadosById(id = str(id))
        if (dados):
            for v in dados_update.values():
                v = str(v)

            banco.conectar()
            consulta = "UPDATE usuarios SET nome = ?, email = ?, telefone = ?, cpf = ?, cep = ?, bairro = ?, rua = ?, numero = ?  WHERE id = ?"
            banco.cursor.execute(consulta, (dados_update["nome"], dados_update["email"], dados_update["telefone"], dados_update["cpf"], dados_update["cep"], dados_update["bairro"], dados_update["rua"], dados_update["numero"], str(id)))
            banco.conn.commit()
            banco.conn.close()
            return True

        else:
            return False
             
