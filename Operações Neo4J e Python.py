# Operações Neo4j e Python

# Operações
def update_student_name(driver, student_id, new_name):
    with driver.session() as session:
        session.run(
            "MATCH (s:Aluno) WHERE id(s) = $student_id SET s.name = $new_name",
            student_id=student_id,
            new_name=new_name
        )


def add_property_to_node(driver, node_id, property_name, property_value):
    with driver.session() as session:
        session.run(
            "MATCH (n) WHERE id(n) = $node_id SET n[$property_name] = $property_value",
            node_id=node_id,
            property_name=property_name,
            property_value=property_value
        )


def delete_node(driver, node_id):
    with driver.session() as session:
        session.run(
            "MATCH (n) WHERE id(n) = $node_id DETACH DELETE n",
            node_id=node_id
        )


def delete_all_nodes_of_type(driver, node_label):
    with driver.session() as session:
        session.run(
            "MATCH (n:{}) DETACH DELETE n".format(node_label)
        )

# Importando Biblioteca Neo4j
from neo4j import GraphDatabase

# Dados de Conexão
uri = "bolt://localhost:7687"
username = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(username, password))

# Exemplo de atualização de dados
update_student_name(driver, 123, "Novo Nome")

# Exemplo de adição de propriedade
add_property_to_node(driver, 456, "nova_propriedade", "valor")

# Exemplo de exclusão de nó
delete_node(driver, 789)

# Exemplo de exclusão de todos os nós de um tipo
delete_all_nodes_of_type(driver, "Aluno")

# Fechando Conexão
driver.close()