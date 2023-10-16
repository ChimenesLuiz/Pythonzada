
#interna
from controller.Banco import Banco
banco = Banco()
from controller.Usuario import Usuario
from controller.Veiculo import Veiculo

class Relacao:



    @staticmethod
    def cadastrar(dados = {}):
        #verifica se cliente existe
        resultado_usuario = Usuario.getDadosByCPF(cpf = dados["id_usuario"])
        resultado_veiculo = Veiculo.getDadosByPlaca(placa = dados["id_veiculo"])
        dados["id_usuario"] = resultado_usuario[0]
        dados["id_veiculo"] = resultado_veiculo[0]

        if (resultado_usuario and resultado_veiculo):
            for values in dados.values():
                values = str(values)

            banco.conectar()
            consulta = "INSERT INTO relacoes(id_usuario, id_veiculo, data_limite, tipo) VALUES (:id_usuario, :id_veiculo, :data_limite, :tipo)"
            banco.cursor.execute(consulta, dados)
            
            banco.conn.commit()
            banco.conn.close()
            return True
        else:
            return False





    @staticmethod
    def getDados():
        banco.conectar()

        consulta = """
        SELECT relacoes.id, usuarios.nome, usuarios.email, usuarios.telefone, usuarios.cpf, usuarios.cep, veiculos.ano, veiculos.km, veiculos.cambio, veiculos.carroceria, veiculos.combustivel, veiculos.placa, veiculos.preco FROM relacoes
        INNER JOIN usuarios ON usuarios.id = relacoes.id_usuario
        INNER JOIN veiculos ON veiculos.id = relacoes.id_veiculo
"""

        banco.cursor.execute(consulta)
        data = banco.cursor.fetchall()
        banco.conn.close()
        return data

    # @staticmethod
    # def getDadosById(id = ""):
    #     banco.conectar()

    #     #verificando se o id existe
    #     consulta = "SELECT * FROM veiculos WHERE id = ?"
    #     banco.cursor.execute(consulta, (id))
    #     resultado = banco.cursor.fetchone()
    #     banco.conn.close()
    #     return resultado   
    
    # @staticmethod
    # def getDadosByChassi(chassi = ""):
    #     banco.conectar()
    #     #verificando se o id existe
    #     consulta = "SELECT * FROM veiculos WHERE chassi = ?"
    #     banco.cursor.execute(consulta, (chassi,))
    #     resultado = banco.cursor.fetchone()
    #     banco.conn.close()

    #     return resultado   
        
    # @staticmethod
    # def deleteById(id = ""):
    #     banco.conectar()

    #     #verificando se o id existe
    #     consulta = "SELECT * FROM veiculos WHERE id = ?"
    #     banco.cursor.execute(consulta, (id))
    #     resultado = banco.cursor.fetchone()
    #     if (resultado):

    #         consulta = "DELETE FROM veiculos WHERE id = ?"
    #         banco.cursor.execute(consulta, (id))
    #         banco.conn.commit()
    #         banco.conn.close()
    #         return True
    #     else:
    #         banco.conn.close()
    #         return False

    # def update(id = "", dados_update= {}):
    #     dados = Veiculo.getDadosById(id = str(id))
    #     print(dados)
    #     if (dados):
    #         for v in dados_update.values():
    #             v = str(v)

    #         banco.conectar()
    #         consulta = "UPDATE veiculos SET ano = ?, km = ?, cambio = ?, carroceria = ?, combustivel = ?, placa = ?, cor = ?, chassi = ?  WHERE id = ?"
    #         banco.cursor.execute(consulta, (dados_update["ano"], dados_update["cambio"], dados_update["carroceria"], dados_update["combustivel"], dados_update["placa"], dados_update["placa"], dados_update["cor"], dados_update["chassi"], str(id)))
    #         banco.conn.commit()
    #         banco.conn.close()
    #         return True

    #     else:
    #         return False
             
