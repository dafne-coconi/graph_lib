from utils import Nodo, Arista_undirected, Grafo
import random

def get_node_list(m = 1, n = 1, simple = 0):

      if simple == 0:
         list_of_lists = [[0 for i in range(1, n + 1)] for _ in range(m)]
         #print(list_of_lists)
         num_nodos = 0
         for i in range(m):
            for j in range(n):
               #print(list_of_lists[i][j])
               num_nodos += 1
               node = Nodo(f'{num_nodos}')
               list_of_lists[i][j] = node
               #print(list_of_lists)
      elif simple == 1:
         list_of_lists = [0] * n
         for i in range(n):
            node = Nodo(f'{i+1}')
            list_of_lists[i] = node
            #print(list_of_lists)
      #print(list_of_lists)

      return list_of_lists

def mesh_graph(m, n, dirigido = False):
   """
   Genera grafo de malla
   :param m: número de columnas (> 1)
   :param n: número de filas (> 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """

   list_nodos = get_node_list(m, n, simple = 0)
   #print(f'nodos {list_nodos}')

   grafo = Grafo("mesh", list_nodos, directed = dirigido)
   for i in range(m):
      for j in range(n):
         if i < m - 1:
            grafo.new_edge(list_nodos[i][j], list_nodos[i + 1][j], random.randint(2,50))
         if j < n - 1:
            grafo.new_edge(list_nodos[i][j], list_nodos[i][j + 1], random.randint(2,50))

   grafo.simplify_list_node()

   grafo.create_graph_notation()
   
   grafo.not_explored_nodes()
   grafo.save_graph_edges(type_graph = grafo.name, new_edges_list = grafo.edges_list)
   
   nodo = grafo.nodes_list[5]
   """
   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()

   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")

   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")
   """
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")

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
   
   #nodo = Nodo()
   list_nodos = get_node_list(n = n, simple = 1)
   #list_nodos = nodo.get_node_list(n = n, simple = 1)

   grafo = Grafo("erdos_renyi", list_nodos, directed = dirigido)
   #grafo.simplify_list_node()
   
   for _ in range(m):
      #rand_sample_list = random.sample(grafo.nodes_list, 2)
      rand_sample_list = random.sample(list_nodos, 2)

      if (rand_sample_list[0] != rand_sample_list[1]):
         grafo.new_edge(rand_sample_list[0], rand_sample_list[1], random.randint(2,50))
   
   grafo.create_graph_notation()
   
   grafo.not_explored_nodes()
   grafo.save_graph_edges(type_graph = grafo.name, new_edges_list = grafo.edges_list)
   """
   nodo = grafo.nodes_list[5]
   
   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()
   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")
   """
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")


def gilbert_graph(n, p, dirigido=False):
   """
   Genera grafo aleatorio con el modelo Gilbert
   :param n: número de nodos (> 0)
   :param p: probabilidad de crear una arista (0, 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   #nodo = Nodo()
   list_nodos = get_node_list(n = n, simple = 1)
   #list_nodos = nodo.get_node_list(n = n, simple = 1)

   grafo = Grafo("gilbert", list_nodos, directed = dirigido)
   #grafo.simplify_list_node()

   for i in grafo.nodes_list:
      for j in grafo.nodes_list:
         if p < random.random() and i != j:
            grafo.new_edge(i, j, random.randint(2,50))
   
   grafo.create_graph_notation()
   
   grafo.not_explored_nodes()
   grafo.save_graph_edges(type_graph = grafo.name, new_edges_list = grafo.edges_list)
   
   """
   nodo = grafo.nodes_list[5]

   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()
   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")

   #grafo.save_graph_edges(type_graph = grafo.name)
   """
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")


def geografico_simple_graph(n, r, dirigido = False):
   """
   Genera grafo aleatorio con el modelo geográfico simple
   :param n: número de nodos (> 0)
   :param r: distancia máxima para crear un nodo (0, 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """

   list_nodos = [0] * n
   list_nodos_distancia = [[0 for i in range(1, 4)] for _ in range(n)]
      #print(list_of_lists)
   for i in range(n):
      node = Nodo(f'{i+1}')
      list_nodos_distancia[i][0] = node
      list_nodos_distancia[i][1] = random.random()
      list_nodos_distancia[i][2] = random.random()
      list_nodos[i] = node

   #nodo = Nodo()
   #print(list_nodos_distancia)
   #list_nodos = nodo.nodo_list_geo(n = n)
   
   grafo = Grafo("geografico_simple", list_nodos, directed = dirigido)

   for nodo_1 in list_nodos_distancia:
      for nodo_2 in list_nodos_distancia:
         #print(f'nodo 1 {nodo_1} nodo 2 {nodo_2}')
         if nodo_1 != nodo_2:
            distance = grafo.distance_nodes(nodo_1, nodo_2)
            #print(f'nodo 1 {nodo_1} nodo 2 {nodo_2}')
            #print(f'distance: {distance}')
            if distance < r:
               grafo.new_edge(nodo_1[0], nodo_2[0], random.randint(2,50))
   
   #grafo.nodes_list = get_node_list(n = n, simple = 1)
   #list_nodos = get_node_list(n = n, simple = 1)
   #grafo.simplify_list_node()
   grafo.create_graph_notation()
   grafo.not_explored_nodes()
   grafo.save_graph_edges(type_graph = grafo.name, new_edges_list = grafo.edges_list)
   """
   nodo = grafo.nodes_list[0]

   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()
   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")
 
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")
   """
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")


def barabasi_albert_graph(n, degree, dirigido = False):
   """
   Genera grafo aleatorio con el modelo Barabasi-Albert
   :param n: número de nodos (> 0)
   :param d: grado máximo esperado por cada nodo (> 1)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """

   #nodo = Nodo()
   list_nodos = get_node_list(n = n, simple = 1)
   
   grafo = Grafo("barabasi_albert", list_nodos, directed = dirigido)
   #grafo.simplify_list_node()

   for nodo_1 in grafo.nodes_list:
        for nodo_2 in grafo.nodes_list:
           #print(f'{nodo_2.name}')
           #print(f'nodos ad {len(nodo_1.nodos_adyacentes)}')
           connect = 1 - (len(nodo_1.nodos_adyacentes) / degree)
           #print(f'connect {connect}')
           if (random.random() < connect) and nodo_1 != nodo_2:
              #print("Se conecta!")
              grafo.new_edge(nodo_1, nodo_2, random.randint(2,50))

   grafo.create_graph_notation()
   grafo.not_explored_nodes()
   grafo.save_graph(type_graph = grafo.name)
   """
   nodo = grafo.nodes_list[0]
   
   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()
   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")
   """
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")

def dorogovtsev_mendes_graph(n, dirigido = False):
   """
   Genera grafo aleatorio con el modelo Barabasi-Albert
   :param n: número de nodos (≥ 3)
   :param dirigido: el grafo es dirigido?
   :return: grafo generado
   """
   if n < 3:
      return "La cantidad de nodos debe ser > 3"
   
   #nodo = Nodo()
   list_nodos = get_node_list(n = n, simple = 1)
   #list_nodos = nodo.get_node_list(n = n, simple = 1)

   grafo = Grafo("dorogovtsev_mendes", list_nodos, directed = dirigido)
   #grafo.simplify_list_node()
   
   sample_list = grafo.nodes_list[0:3]
   new_list_nodes = grafo.nodes_list[3:]

   for i in range(3):
      grafo.new_edge(sample_list[i-1], sample_list[i], random.randint(2,50))
   #print("fin de primera cración")
   for node in new_list_nodes:
      edge = random.choice(grafo.edges_list)
      grafo.new_edge(edge.n1, node, random.randint(2,50))
      grafo.new_edge(edge.n2, node, random.randint(2,50))
   
   grafo.create_graph_notation()
   grafo.not_explored_nodes()
   grafo.save_graph_edges(type_graph = grafo.name, new_edges_list = grafo.edges_list)
   
   nodo = grafo.nodes_list[0]
   """
   grafo.not_explored_nodes()
   grafo.BFS(nodo)
   grafo.save_graph(type_graph = "BFS")

   grafo.not_explored_nodes()
   grafo.DFS_I(nodo)
   grafo.save_graph(type_graph = "DFS_I")

   grafo.not_explored_nodes()
   grafo.DFS_R(nodo)
   grafo.save_graph(type_graph = "DFS_R")
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Dijkstra(random_node)
   grafo.save_graph(type_graph = "DIJKSTRA")
   
   new_edges_list = grafo.KruskalD(grafo)
   grafo.save_graph_edges(type_graph = "KrustalD", new_edges_list = new_edges_list)
   new_edges_list = grafo.KruskalI(grafo)
   grafo.save_graph_edges(type_graph = "KrustalI", new_edges_list = new_edges_list)
   
   random_node = random.choice(grafo.nodes_list)
   print(f' random_node: {random_node}')
   grafo.Prim(grafo, random_node)
   grafo.save_graph(type_graph = "PRIM")
   """

   grafo.draw_graph_eades()