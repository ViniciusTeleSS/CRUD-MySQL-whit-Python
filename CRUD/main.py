from mysql.connector import errorcode
import mysql.connector
import defs as de

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='cadastro', 
    )
    print('Conectado')
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Algo errado com o usuario ou senha.')
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe')
    else:
        print(e)

cursor = conexao.cursor()

#CABEÇALHO
de.linha()
print('TABELA DE PESSOAS'.center(30))
de.linha()

#MENU DE OPÇÕES
while True:
    opcao = input(
'''Qual operação deseja realizar?

1 - Visualizar registros

2 - Inserir novo registro

3 - Atualizar registro

4 - Deletar registro

0 - Sair
''')
    de.linha()
    #READ
    if opcao == '1':
        comando = f'SELECT * FROM pessoas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)
        de.linha()
    #INSERT
    elif opcao == '2':
        nome = str(input('Nome: ')).capitalize()
        sexo = str(input('Sexo: [M/F]')).upper()[0]
        while sexo not in 'MF':
            print('Opção inválida')
            sexo = str(input('Sexo: [M/F]')).upper()[0]
        nacio = str(input('País: ')).upper()
        comando = f'INSERT INTO pessoas (ID, NOME, SEXO, PAÍS) VALUES (DEFAULT, "{nome}", "{sexo}", "{nacio}")'
        cursor.execute(comando)
        conexao.commit()
        print('Registro adicionado com sucesso')
        de.linha()
    #UPDATE
    elif opcao == '3':
        id_update = int(input('Digite o ID do registro que deseja atualizar: '))
        update = input('''Qual informação deseja atualizar?
1 - NOME
2 - SEXO
3 - PAÍS''')
        while update not in '0123':
            print('Opção inválida.')
            update = input('''Qual informação deseja atualizar?
1 - NOME
2 - SEXO
3 - PAÍS
4 - VOLTAR AO MENU PRINCIPAL ''')            
        if update == '1':
            up_nome = str(input('Nome: '))
            comando = f'UPDATE pessoas SET NOME = "{up_nome}" WHERE ID = {id_update}'
            cursor.execute(comando)
            conexao.commit()
            print('Nome atualizado com sucesso')
            de.linha()
        elif update == '2':
            up_sexo = str(input('Sexo: [M/F] ')).upper()[0]
            while up_sexo not in 'MF':
                print('Opção inválida')
                up_sexo = str(input('Sexo: [M/F]')).upper()[0]
            sexo = str(input('Sexo: [M/F]')).upper()
            comando = f'UPDATE pessoas SET SEXO = "{up_sexo}" WHERE ID = {id_update}'
            cursor.execute(comando)
            conexao.commit()
            print('Sexo atualizado com sucesso')
            de.linha()
        elif update == '3':
            up_país = str(input('País: ')).upper()
            comando = f'UPDATE pessoas SET PAÍS = "{up_país}" WHERE ID = {id_update}'
            cursor.execute(comando)
            conexao.commit()
            print('País atualizado com sucesso')
        elif update == '0':
            break            
        else:
            print('Opção inválida')
        comando = f'UPDATE pessoas SET SEXO = "F" WHERE ID = 2'
        cursor.execute(comando)
        conexao.commit()
        print('Registro atualizado com sucesso')
        de.linha()
    #DELETE
    elif opcao == '4':
        id_delete = int(input('Digite o ID do registro que deseja deletar: '))
        confirm = str(input(f'Certeza que deseja deletar o registro {id_delete}? [S/N] ')).upper()

        while confirm not in 'SN':
                print('Opção inválida')
                confirm = str(input(f'Certeza que deseja deletar o registro {id_delete}? [S/N]')).upper()[0]
        
        if confirm == 'S':
            comando = f'DELETE FROM pessoas WHERE ID = {id_delete}'
            cursor.execute(comando)
            conexao.commit()
            print('Registro deletado com sucesso')
            de.linha()
        else:
            print('Retornando ao menu')
    #EXIT
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')

cursor.close()
conexao.close()