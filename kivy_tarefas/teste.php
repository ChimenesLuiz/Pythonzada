<?php
namespace App\Db;
use PDO;
use PDOException;
//die('banco'); 
class Banco{
  
    //Variaveis referentes a conexao com o banco de dados
    const HOST = '192.168.22.9';
  
    const DB_NAME = 'etg';
    const USER = 'fabrica';
    const PASS = 'fabrica@2022';
    private $table;//variavel que vai falar sobre qual tabela do banco esta sendo tratada
    private $conexao;
    public function __construct($table = null)
    { 
        $this -> table = $table; 
    }
    private function conectar(){
        try
        {
            $this -> conexao = new PDO('mysql:host='.self::HOST.';dbname='.self::DB_NAME, self::USER, self::PASS);
        }
        catch(PDOException $e)
        {
            die("ERRO: " . $e -> getMessage());
        }
    }

    private function executarQuery($query, $valores = [])
    {
        try
        {
            //abrindo conexao
            $this -> conectar();
            //criando statement e preparando a query que foi passada como argumento
            $statement = $this -> conexao -> prepare($query);
            $statement -> execute($valores);
        
            //fechando conexao
            $this -> conexao = null;
            //var_dump($statement); exit;
            //retornando o resultado da query
            return $statement;
        }
        catch (PDOException $e)
        {
            echo('Erro3: ' . $e -> getMessage());
            return false;
        }
    }

    private function executeLastId($query, $valores = [])
    {
        try
        {
            //abrindo conexao
            $this -> conectar();

            //criando statement e preparando a query que foi passada como argumento
            $statement = $this -> conexao -> prepare($query);
            $statement -> execute($valores);
            $id = $this->conexao->lastInsertId();
    
            //fechando conexao
            $this -> conexao = null;
            //var_dump($statement); exit;
            //retornando o resultado da query
            return $id;
        }
        catch (PDOException $e)
        {
            echo('Erro3: ' . $e -> getMessage());
            return false;
        }
    }


    public function insert($dados = [])
    {
        /*
        recebendo as chaves da array $dados
        ATENCAO!!
        OS PARAMETROS PASSADOS PARA ESTA ARRAY $DADOS COMO CHAVE,
        DEVEM SER REFERENTES AOS NOMES DAS COLUNAS DA TABELA NO BANCO, IDENTICOS.
        !!ATENCAO
        */
        $chaves = array_keys($dados);

        /*atribuindo uma lista a variavel $valores,
        do tamanho da array $chaves,
        preenchida por `?`.
        */
        $valores = array_pad([], count($chaves), '?');

        /*Montando a $query, substituindo o nome da tabela,
        substituindo as chaves usando a funcao implode(),
        substituindo os valores por `?` usando a funcao implode
        */ 
        
        $query = 'INSERT INTO '.$this -> table.'('.implode(', ', $chaves).') VALUES('.implode(', ', $valores).')';

        
        //echo $query; var_dump(array_values($dados));exit;
        //Chamando o metodo `executarQuery` e passando a $query montada e APENAS OS VALORES de `$dados`
        $this -> executarQuery($query, array_values($dados));

        return true;
    }

    public function insertRecoverId($dados = [])
    {
        $chaves = array_keys($dados);

        /*atribuindo uma lista a variavel $valores,
        do tamanho da array $chaves,
        preenchida por `?`.
        */
        $valores = array_pad([], count($chaves), '?');

        /*Montando a $query, substituindo o nome da tabela,
        substituindo as chaves usando a funcao implode(),
        substituindo os valores por `?` usando a funcao implode
        */ 
        
        $query = 'INSERT INTO '.$this -> table.'('.implode(', ', $chaves).') VALUES('.implode(', ', $valores).')';
        echo $query;var_dump($dados); exit;
        //Chamando o metodo `executarQuery` e passando a $query montada e APENAS OS VALORES de `$dados`
        $id = $this -> executeLastId ($query, array_values($dados));
        return $id;
    }

    public function delete($valor, $coluna)
    {
        $query = 'DELETE FROM '.$this->table.' WHERE ' . $coluna . ' = '. $valor;
        return $this->executarQuery($query);
    }

    public function update($where = '',$dados = [])
    {
        //lista chave valor($dados) 
        //obs: chaves tem que ser o mesmo nome que o nome da coluna
        $setter = "";
        $chaves = array_keys($dados);
        $valores = array_values($dados);

        for ($i=0; $i < count($chaves); $i++) { 
            
            if($i == (count($chaves) - 1)){

                $setter .= $chaves[$i] . " = '". $valores[$i]."'";

            }else{

                $setter .= $chaves[$i] . " = '". $valores[$i]."', ";
            }
        }

        $query = 'UPDATE '.$this->table.'
                  SET '. $setter . '
                  WHERE '. $where;
        //echo $query;exit;
        return $this->executarQuery($query);
        // terminar............ 
    }

    //Metodo criado pra executar o comando SQL -> `SELECT`
    public function select($where = null, $order = null, $limit = null, $campos = '*')
    {
        /*Usando OPERADOR TERNARIO para concatenar ou nao
        Se o parametro $where tiver mais que uma string, sera concatenado com uma
        string `WHERE`
        Senao $where = ''
        */ 
        //echo $where;exit;
        $where = strlen($where) ? ' WHERE '.$where: '';
        //Mesma logica
        $order = strlen($order) ? ' ORDER BY '.$order: '';
        //Mesma logica
        $limit = strlen($limit) ? ' LIMIT '.$limit: '';
        
        /*Montando a query do `SELECT`,
        concatenando o nome da tabela,
        concatenando os parametros por ALGO ou por ''
        */
        $query = 'SELECT '.$campos.' FROM '.$this->table.''.$where.''.$order.''.$limit.'';
        //echo $query;exit;
        
        //preciso usar o fetch all aqui, ainda nao terminei!
        return $this ->  executarQuery($query);
    }
}
?>
