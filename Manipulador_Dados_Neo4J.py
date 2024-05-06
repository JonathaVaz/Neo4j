from neo4j import GraphDatabase

class Neo4jDataManipulation:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def run_query(self, query):
        with self._driver.session() as session:
            result = session.run(query)
            return result

if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # Altere para o URI do seu banco de dados Neo4j
    user = "neo4j"  # Altere para o nome de usuário do seu banco de dados Neo4j
    password = "password"  # Altere para a senha do seu banco de dados Neo4j

    data_manipulator = Neo4jDataManipulation(uri, user, password)

    # Exemplo de consultas com a linguagem Cypher
    queries = [
        "MATCH (p:Professor) RETURN p",
        "MATCH (a:Aluno)-[:FAZ_PARTE]->(t:Turma) RETURN a, t",
        "MATCH (prof:Professor)-[:ENSINA]->(curso:Curso)<-[:PERTENCE_A]-(turma:Turma) RETURN prof, curso, turma"
    ]

    for query in queries:
        print(f"Running query: {query}")
        result = data_manipulator.run_query(query)
        for record in result:
            print(record)

    data_manipulator.close()
