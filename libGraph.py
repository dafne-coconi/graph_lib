from utils import Nodo, Arista_undirected, Grafo
import random

def mesh_graph(m, n, dirigido = False):
   """
   Genera grafo de malla
   :param m: número de columnas (> 1)
   :param n: número de filas (> 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   nodo = Nodo()
   list_nodos = nodo.get_node_list(m, n)
   print(f'nodos {list_nodos}')

   grafo = Grafo("mesh", list_nodos, directed = dirigido)
   for i in range(m):
      for j in range(n):
         if i < m - 1:
            grafo.new_edge(list_nodos[i][j], list_nodos[i + 1][j])
         if j < n - 1:
            grafo.new_edge(list_nodos[i][j], list_nodos[i][j + 1])

   grafo.simplify_list_node()

   grafo.create_graph_notation()

   grafo.save_graph()

def erdos_renyi_graph(n, m, dirigido = False):
   """
   Genera grafo aleatorio con el modelo Erdos-Renyi
   :param n: número de nodos (> 0)
   :param m: número de aristas (>= n-1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   if m < n - 1:
      return "m debe ser mayor a n"
   
   nodo = Nodo()
   list_nodos = nodo.get_node_list(n = n)

   grafo = Grafo("erdos_renyi", list_nodos, directed = dirigido)
   grafo.simplify_list_node()
   
   for _ in range(m):
      rand_sample_list = random.sample(grafo.nodes_list, 2)

      if (rand_sample_list[0] != rand_sample_list[1]):
         grafo.new_edge(rand_sample_list[0], rand_sample_list[1])

   grafo.create_graph_notation()
   grafo.save_graph()

def gilbert_graph(n, p, dirigido=False):
   """
   Genera grafo aleatorio con el modelo Gilbert
   :param n: número de nodos (> 0)
   :param p: probabilidad de crear una arista (0, 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   nodo = Nodo()
   list_nodos = nodo.get_node_list(n = n)

   grafo = Grafo("gilbert", list_nodos, directed = dirigido)
   grafo.simplify_list_node()

   for i in grafo.nodes_list:
      for j in grafo.nodes_list:
         if p < random.random() and i != j:
            grafo.new_edge(i, j)
   
   grafo.create_graph_notation()
   grafo.save_graph()

def geografico_simple_graph(n, r, dirigido = False):
   """
   Genera grafo aleatorio con el modelo geográfico simple
   :param n: número de nodos (> 0)
   :param r: distancia máxima para crear un nodo (0, 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   nodo = Nodo()
   list_nodos = nodo.nodo_list_geo(n = n)
   
   grafo = Grafo("geografico_simple", list_nodos, directed = dirigido)

   for nodo_1 in grafo.nodes_list:
      for nodo_2 in grafo.nodes_list:
         #print(f'nodo 1 {nodo_1} nodo 2 {nodo_2}')
         if nodo_1 != nodo_2:
            distance = grafo.distance_nodes(nodo_1, nodo_2)
            #print(f'distance: {distance}')
            if distance < r:
               grafo.new_edge(nodo_1[0], nodo_2[0])
   
   grafo.nodes_list = nodo.get_node_list(n = n)
   grafo.simplify_list_node()
   grafo.create_graph_notation()
   grafo.save_graph()



def barabasi_albert_graph(n, degree, dirigido = False):
   """
   Genera grafo aleatorio con el modelo Barabasi-Albert
   :param n: número de nodos (> 0)
   :param d: grado máximo esperado por cada nodo (> 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   nodo = Nodo()
   list_nodos = nodo.get_node_list(n = n)
   
   grafo = Grafo("barabasi_albert", list_nodos, directed = dirigido)
   grafo.simplify_list_node()

   for nodo_1 in grafo.nodes_list:
        for nodo_2 in grafo.nodes_list:
           connect = 1 - (len(grafo.node_in_out(nodo_2)) / degree)
           #print(f'connect {connect}')
           if random.random() < connect:
              grafo.new_edge(nodo_1, nodo_2)

   grafo.create_graph_notation()
   grafo.save_graph()

def dorogovtsev_mendes_graph(n, dirigido = False):
   """
   Genera grafo aleatorio con el modelo Barabasi-Albert
   :param n: número de nodos (≥ 3)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   if n < 3:
      return "La cantidad de nodos debe ser > 3"
   
   nodo = Nodo()
   list_nodos = nodo.get_node_list(n = n)

   grafo = Grafo("dorogovtsev_mendes", list_nodos, directed = dirigido)
   grafo.simplify_list_node()
   
   sample_list = grafo.nodes_list[0:3]
   new_list_nodes = grafo.nodes_list[3:]

   for i in range(3):
      grafo.new_edge(sample_list[i-1], sample_list[i])
   #print("fin de primera cración")
   for node in new_list_nodes:
      edge = random.choice(grafo.edges_list)
      grafo.new_edge(edge[0], node)
      grafo.new_edge(edge[1], node)
   
   grafo.create_graph_notation()
   grafo.save_graph()