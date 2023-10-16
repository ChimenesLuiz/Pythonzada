

#interna
from controller.Banco import Banco
banco = Banco()

class Veiculo:

    @staticmethod
    def cadastrar(dados = {}):
        for values in dados.values():
            values = str(values)

        banco.conectar()
        consulta = "INSERT INTO veiculos(ano, km, cambio, carroceria, combustivel, placa, cor, chassi) VALUES (:ano, :km, :cambio, :carroceria, :combustivel, :placa, :cor, :chassi)"
        banco.cursor.execute(consulta, dados)
        
        banco.conn.commit()
        banco.conn.close()


    @staticmethod
    def getDados():
        banco.conectar()

        consulta = "SELECT * FROM veiculos"
        banco.cursor.execute(consulta)
        data = banco.cursor.fetchall()
        
        banco.conn.close()
        return data

    @staticmethod
    def getDadosById(id = ""):
        banco.conectar()

        #verificando se o id existe
        consulta = "SELECT * FROM veiculos WHERE id = ?"
        banco.cursor.execute(consulta, (id))
        resultado = banco.cursor.fetchone()
        banco.conn.close()
        return resultado   
    
    @staticmethod
    def getDadosByChassi(chassi = ""):
        banco.conectar()
        #verificando se o id existe
        consulta = "SELECT * FROM veiculos WHERE chassi = ?"
        banco.cursor.execute(consulta, (chassi,))
        resultado = banco.cursor.fetchone()
        banco.conn.close()

        return resultado   
        
    @staticmethod
    def deleteById(id = ""):
        banco.conectar()

        #verificando se o id existe
        consulta = "SELECT * FROM veiculos WHERE id = ?"
        banco.cursor.execute(consulta, (id))
        resultado = banco.cursor.fetchone()
        if (resultado):

            consulta = "DELETE FROM veiculos WHERE id = ?"
            banco.cursor.execute(consulta, (id))
            banco.conn.commit()
            banco.conn.close()
            return True
        else:
            banco.conn.close()
            return False

    def update(id = "", dados_update= {}):
        dados = Veiculo.getDadosById(id = str(id))
        print(dados)
        if (dados):
            for v in dados_update.values():
                v = str(v)

            banco.conectar()
            consulta = "UPDATE veiculos SET ano = ?, km = ?, cambio = ?, carroceria = ?, combustivel = ?, placa = ?, cor = ?, chassi = ?  WHERE id = ?"
            banco.cursor.execute(consulta, (dados_update["ano"], dados_update["cambio"], dados_update["carroceria"], dados_update["combustivel"], dados_update["placa"], dados_update["placa"], dados_update["cor"], dados_update["chassi"], str(id)))
            banco.conn.commit()
            banco.conn.close()
            return True

        else:
            return False
             
        
    @staticmethod
    def getDadosByPlaca(placa = ""):
        banco.conectar()
        #verificando se o id existe
        consulta = "SELECT * FROM veiculos WHERE placa = ?"
        banco.cursor.execute(consulta, (placa,))
        resultado = banco.cursor.fetchone()
        banco.conn.close()

        return resultado   
