# Gerenciador Escolar - Neo4j

# Importando Biblioteca Neo4j
from neo4j import GraphDatabase

# Criando Gerenciador
class SchoolManagementSystem:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_sample_data(self):
        with self._driver.session() as session:
            # Criar professores
            session.run("CREATE (:Professor {name: 'Professor 1'})")
            session.run("CREATE (:Professor {name: 'Professor 2'})")
            print("Professores Criados!!")

            # Criar cursos
            session.run("CREATE (:Curso {name: 'Curso 1'})")
            session.run("CREATE (:Curso {name: 'Curso 2'})")
            print("Professores Cursos!!")

            # Criar turmas
            session.run("CREATE (:Turma {name: 'Turma 1'})")
            session.run("CREATE (:Turma {name: 'Turma 2'})")
            print("Professores Turma!!")

            # Criar alunos
            session.run("CREATE (:Aluno {name: 'Aluno 1'})")
            session.run("CREATE (:Aluno {name: 'Aluno 2'})")
            print("Professores Aluno!!")

            # Criar relações entre professores e cursos
            session.run("""
                MATCH (prof:Professor {name: 'Professor 1'})
                MATCH (curso:Curso {name: 'Curso 1'})
                CREATE (prof)-[:ENSINA]->(curso)
            """)
            print("Relações criadas primeira parte!!")
            session.run("""
                MATCH (prof:Professor {name: 'Professor 2'})
                MATCH (curso:Curso {name: 'Curso 2'})
                CREATE (prof)-[:ENSINA]->(curso)
            """)
            print("Relações criadas segunda parte!!")

            # Criar relações entre turmas e cursos
            session.run("""
                MATCH (turma:Turma {name: 'Turma 1'})
                MATCH (curso:Curso {name: 'Curso 1'})
                CREATE (turma)-[:PERTENCE_A]->(curso)
            """)
            session.run("""
                MATCH (turma:Turma {name: 'Turma 2'})
                MATCH (curso:Curso {name: 'Curso 2'})
                CREATE (turma)-[:PERTENCE_A]->(curso)
            """)

            # Criar relações entre alunos e turmas
            session.run("""
                MATCH (aluno:Aluno {name: 'Aluno 1'})
                MATCH (turma:Turma {name: 'Turma 1'})
                CREATE (aluno)-[:FAZ_PARTE]->(turma)
            """)
            session.run("""
                MATCH (aluno:Aluno {name: 'Aluno 2'})
                MATCH (turma:Turma {name: 'Turma 2'})
                CREATE (aluno)-[:FAZ_PARTE]->(turma)
            """)

if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # Altere para o URI do seu banco de dados Neo4j
    user = "neo4j"  # Altere para o nome de usuário do seu banco de dados Neo4j
    password = "password"  # Altere para a senha do seu banco de dados Neo4j

    system = SchoolManagementSystem(uri, user, password)
    system.create_sample_data()
    system.close()
