#CLASSES EXTERNAS
#-----platform------
import platform
#-----os------
import os


class DirectoryController:
    @staticmethod
    def getSO() -> str:
        os_name = platform.system()
        return os_name
    
    @staticmethod
    def createInLinux() -> str:
        user = os.getenv('USER')
        destination_dir = f"/home/{user}/Downloads/"

        if (not os.path.exists(destination_dir)):
            os.makedirs(destination_dir)

        source_file = "todo_dump.sql"
        destination_file = os.path.join(destination_dir, os.path.basename(source_file))
        try:
            os.system(f'mv {source_file} {destination_file}')
            return destination_dir
        except Exception as e:
            raise(f"Erro ao exportar o arquivo: {str(e)}")
        
    @staticmethod
    def createInWindows() -> str:
        user = os.getlogin()
        destination_dir = f"C:\{user}\John\Downloads"

        if (not os.path.exists(destination_dir)):
            os.makedirs(destination_dir)

        source_file = "todo_dump.sql"
        destination_file = os.path.join(destination_dir, os.path.basename(source_file))
        try:
            os.system(f'mv {source_file} {destination_file}')
            return destination_dir
        except Exception as e:
            raise(f"Erro ao exportar o arquivo: {str(e)}")
        
    @staticmethod
    def createInAndroid() -> None:
        pass

    @staticmethod
    def rmDb() -> None:
        file = "todo.db"

        if os.path.exists(file):
            os.unlink(file)
        else:
            raise(f"O arquivo {file} não existe.")
  
    @staticmethod
    def rmDump() -> None:
        file = "todo_dump.sql"

        if os.path.exists(file):
            os.unlink(file)
        else:
            raise(f"O arquivo {file} não existe.")
    
    @staticmethod
    def rewriteDumpFile(file = str) -> None:
        lines_to_remove = [1, 2]

        with open(file, "r") as file:
            sql_content = file.readlines()

        for index in sorted(lines_to_remove, reverse=True):
            del sql_content[index]

        new_sql_content = "".join(sql_content)
        DirectoryController.rmDump()

        with open('todo_dump.sql', 'w') as arquivo:
            print(new_sql_content)
            arquivo.write(str(new_sql_content))
            print(arquivo)




