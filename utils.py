from datetime import datetime
import random
import math
import copy
import pygame
import numpy

class Nodo:
   """
   Clase Nodo
   :param value: number of nodes
   """
   def __init__(self, name):
      self.name = f'N{name}'
      #self.node_list = list()
      self.nodos_adyacentes = list()
      self.nodo_explored = 0

   #def get_name(self, name):
      #self.name = f'N{name}'
      #return self.name
      
   def get_node_list(self, m = 1, n = 1, simple = 0):

      if simple == 0:
         list_of_lists = [[0 for i in range(1, n + 1)] for _ in range(m)]
         num_nodos = 0
         for i in range(m):
            for j in range(n):
               #print(list_of_lists[i][j])
               num_nodos += 1
               node = self.get_name(f'{num_nodos}')
               list_of_lists[i][j] = node
               #print(list_of_lists)
      elif simple == 1:
         list_of_lists = [0] * n
         for i in range(n):
            node = self.get_name(f'{i+1}')
            list_of_lists[i] = node
            #print(list_of_lists)
      #print(list_of_lists)
 
      self.node_list = list_of_lists

      return self.node_list
   
   def nodo_list_geo(self, n = 1):
      list_of_lists = [[0 for i in range(1, 4)] for _ in range(n)]
      #print(list_of_lists)
      for i in range(len(list_of_lists)):
         node = self.get_name(f'{i+1}')
         list_of_lists[i][0] = node
         list_of_lists[i][1] = random.random()
         list_of_lists[i][2] = random.random()

      #self.node_list = 
      return list_of_lists
   
   def add_nodos_adyacentes(self, nodo):
      self.nodos_adyacentes.append(nodo)

   def remove_nodo_adyacente(self, nodo_ad):
      self.nodos_adyacentes.remove(nodo_ad)
   
   def explored(self):
      self.nodo_explored = 1

   def not_explored(self):
      self.nodo_explored = 0
      
   def __repr__(self):
      return f'{self.name}'
   """
   def __cmp__(self, other):
      return self.name == other.name
   
   def __eq__(self, other):
      return self.name == other.name
   """
   #def add_edges(self, edge):
    #  self.edges_to_node.append(edge)


class Arista_undirected:
   """
   Clase Arista
   :param value: number of nodes
   """
   def __init__(self, n1: Nodo, n2: Nodo, weight = random.randint(2,50)):
      self.n1 = n1
      self.n2 = n2
      self.lista_arista = list()
      self.weight = weight
      self.is_explored = 0
        
   def get_n1(self):
      return self.n1

   def get_n2(self):
      return self.n2
   
   def create_list_arista(self):
      #self.lista_arista = [self.n1, self.n2, self.weight]
      self.lista_arista = [self.n1, self.n2]
      self.n1.add_nodos_adyacentes(self.n2)
      self.n2.add_nodos_adyacentes(self.n1)
      return self.lista_arista
   
   def explored(self):
      self.is_explored = 1
   
   def __repr__(self):
        return f'[{self.n1}, {self.n2}]'
        #return f'({self.n1}, {self.n2})
        # 
   def __key(self):
      return (self.n1.name, self.n2.name)

   def __hash__(self):
      return hash(self.__key())
        
   
   #def __str__(self):
        #return f'[{self.n1}, {self.n2}, {self.weight}]'
        #return f'[{self.n1}, {self.n2}, {self.weight}]'
   
   def __cmp__(self, other):
      return (self.n1.name == other.n1.name and self.n2.name == other.n2.name) or (self.n1.name == other.n2.name and self.n2.name == other.n1.name)

   def __eq__(self, other):
      return (self.n1.name == other.n1.name and self.n2.name == other.n2.name) or (self.n1.name == other.n2.name and self.n2.name == other.n1.name)

   
class Arista_directed:
   """
   Clase Arista
   :param value: number of nodes
   """
   def __init__(self, weight):
      self.weight = weight
      self.edges_list = list()
        
   def get_n1(self):
      return self.n1

   def get_n2(self):
      return self.n2

   def __str__(self):
      return self.n1.get_name() + " -> " + self.n2.get_name()
   
   

class Grafo:
   """
   Clase Grafo
   """
   def __init__(self, name, nodes_list, directed):
      self.name = name
      self.nodes_list = nodes_list
      self.directed = directed
      self.edges_list = []
      self.graph_dict = dict()
      self.capas = dict()
      self.bfs_dict = dict()
      self.dfs_i_dict = dict()
      self.dfs_r_dict = dict()
      self.dijkstra_dict = dict()
      self.prim_dict = dict()
      self.dict_distance_node = {}
      #for node in self.nodes_list:
       #  self.dfs_r_dict[node] = []
    
   def new_edge(self, n1: Nodo, n2: Nodo, weight = random.randint(2,50)):
      self.n1 = n1
      self.n2 = n2
      """
      Insert an edge to the list of edges in the graph
      :param n1: starting node of the edge
      :param n2: ending node of the edge
      """
      if self.directed:
         edge = Arista_directed(n1, n2, weight)
      else:
         edge = Arista_undirected(n1, n2, weight)
      
      #print(edge)
      if edge not in self.edges_list: 
         self.edges_list.append(edge)
         edge.create_list_arista()
      #print(self.edges_list)

   def simplify_list_node(self):
      new_node_list = list()
      for i in range(len(self.nodes_list)):
         if (len(self.nodes_list[i]) > 1):
            for j in self.nodes_list[i]:
               new_node_list.append(j)
         else:
            new_node_list.append(self.nodes_list[i])
      
      self.nodes_list = new_node_list
      #print(new_node_list)
      
      return self.nodes_list
   
   def distance_nodes(self, node_1, node_2):
      distance_nodes = math.sqrt((node_1[1] - node_2[1])**2 + (node_1[2] - node_2[2])**2)
      return distance_nodes
   
   def node_in_out(self, node):
      list_node_in_out = list()
      for nodes in self.edges_list:
         if (node in nodes):
            if (nodes.index(node) == 0):
               if (nodes[1] not in list_node_in_out):
                  list_node_in_out.append(nodes[1])
            else:
               if (nodes[1] not in list_node_in_out):
                  list_node_in_out.append(nodes[0])
      return list_node_in_out
   
   def create_graph_notation(self):
      """
      if (self.name == "geografico_simple"):
         new_list_node =  []
         for node in self.nodes_list:
            new_list_node.append(node[0])
         self.nodes_list = new_list_node
         """
      #print(f'Node in node list {type(self.nodes_list[0])}')
      for node in self.nodes_list:
         self.graph_dict[node] = []

      changing_edges_list = self.edges_list
      for node in self.nodes_list:
         list_value = list()
         #print(node.name)
         for edge in changing_edges_list: 
            #if (node.name == str(edge).split(",",2)[0].split("[")[1]):
            if (node == edge.n1):
               #print("true dat")
               #list_value.append(str(edge).split(",",2)[1].strip())
               list_value.append(edge.n2)
               #changing_edges_list.remove(edge)
            
         self.graph_dict[node] = list_value
      #print(f'Nodes {self.nodes_list}')
      #print(f'Edges {self.edges_list}')
      #print(f'Graph {self.graph_dict}')

   def save_graph(self, type_graph: str ):
      current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
      if type_graph == "BFS":
         graph = self.bfs_dict
         #print(f'Imprimir {graph}')
         filename = f"{self.name}_BFS_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DFS_R":
         graph = self.dfs_r_dict
         #print(f'Imprimir {graph}')
         filename = f"{self.name}_DFS_R_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DFS_I":
         graph = self.dfs_i_dict
         #print(f'Imprimir {graph}')
         filename = f"{self.name}_DFS_I_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DIJKSTRA":
         graph = self.dijkstra_dict
         filename = f"{self.name}_DIJKSTRA_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "PRIM":
         graph = self.prim_dict
         filename = f"{self.name}_PRIM_{len(self.nodes_list)}_{current_datetime}.dot"
      else:
         graph = self.graph_dict
         #print(f'grafo regular {self.graph_dict}')
         filename = f"{self.name}_{len(self.nodes_list)}_{current_datetime}.dot"
   
      
          
      filepath = f"archivos/{filename}"

      list_v = []
      with open(filepath, "w", encoding="UTF") as file:
         file.write(f"graph {self.name}" + "{\n")
         count = 0
         line = str
         for key in graph:
            value = graph[key]
            #print(value)
            if (len(value) > 0):
        
               for single_value in value:
                  if key == single_value:
                     continue
                  #print(single_value)
                  #line = f'{key} ->' + '{' + f'{value_as_string}' + '}\n'
                  if type_graph == "DIJKSTRA" or type_graph == "PRIM":
                     line = f'{single_value}_{self.dict_distance_node[single_value]} -> ' + f'{key}_{self.dict_distance_node[key]}' + ';\n'
                     file.write(line)
                  else:
                     line = f'{key} -> ' + f'{single_value}' + ';\n'
                     file.write(line)

            else:
               if type_graph == "DIJKSTRA" or type_graph == "PRIM":
                  line = f'{key}_0'+ '\n'
               else:
                  line = f'{key}'+ '\n'
               file.write(line)
            
            
         file.write("\n}")

      #print(self.edges_list)
      print(f"Graph saved to {filepath} ")

   def save_graph_edges(self, type_graph: str,  new_edges_list):
      current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
      if type_graph == "BFS":
         filename = f"{self.name}_BFS_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DFS_R":
         filename = f"{self.name}_DFS_R_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DFS_I":
         filename = f"{self.name}_DFS_I_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "DIJKSTRA":
         filename = f"{self.name}_DIJKSTRA_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "KrustalD":
         filename = f"{self.name}_KrustalD_{len(self.nodes_list)}_{current_datetime}.dot"
      elif type_graph == "KrustalI":
         filename = f"{self.name}_KrustalI_{len(self.nodes_list)}_{current_datetime}.dot"
      else:
         filename = f"{self.name}_edges_{len(self.nodes_list)}_{current_datetime}.dot"
   
      
          
      filepath = f"archivos/{filename}"

      list_v = []
      with open(filepath, "w", encoding="UTF") as file:
         file.write(f"graph {self.name}" + "{\n")
         count = 0
         line = str
         for edge in new_edges_list:
            
            line = f'{edge.n1} -> ' + f'{edge.n2}[Label={edge.weight}]' + ';\n'
            file.write(line)
            
         file.write("\n}")

      #print(self.edges_list)
      print(f"Graph saved to {filepath}")

   def not_explored_nodes(self):
      for node in self.nodes_list:
         node.not_explored()

   def sort_edges(self, vector_list: list, ascendent = True)->list:
      if len(vector_list) <= 1:
         return vector_list
      else:
         weight_edge = vector_list[0].weight
         left = []
         right = []
         for x in vector_list[1:]:
            if x.weight < weight_edge:
               left.append(x)
         
         for x in vector_list[1:]:
            if x.weight >= weight_edge:
               right.append(x)
         if ascendent == True:
            return self.sort_edges(left) + [vector_list[0]] + self.sort_edges(right)
         elif ascendent == False:
            return self.sort_edges(right, False) + [vector_list[0]] + self.sort_edges(left, False)
      
   def get_root(self, root, node):
      if root[node] != node:
         root[node] = self.get_root(root, root[node])

      return root[node]
   
   def merge_graphs(self, root, conj, u, v):
      # Merge the bigger graph to the smaller
      if (conj[u] < conj[u]):
         root[u] = v
      elif (conj[v] > conj[u]):
         root[v] = u
      # conj are the same, one nodes needs to be the root
      else:
         root[u] = v
         conj[v] += 1
      
      return root, conj

   def sort_priority_queue(self, list_Q, distance_values, new_distance_value):
      low = 0
      high = len(list_Q) - 1
      mid = 0
      value_found = 0
      while low <= high and value_found == 0:
         mid = (high + low) // 2
         nodo_mid = list_Q[mid]
         
         searched_value = new_distance_value
         compared_value = distance_values[nodo_mid]
         #print(f'searched {searched_value}, compared {compared_value}')
         
         # Buscar si el valor es menor es mayor a la mitad de la lista
         if compared_value < searched_value:
            #print(f'value is bigger than the mid')
            low = mid + 1
               
            if low < len(list_Q) - 1:
               nodo_next_mid = list_Q[mid + 1]
               # buscar si su siguiente nodo en la lista tiene una longitud menor, 
               # entonces pertenece en medio de esos valores
               if distance_values[nodo_next_mid] > searched_value:
                  #print(f'but value lower than the next one')      
                  value_found = 1
                  mid = mid + 1
            
         
         elif compared_value > searched_value:
            #print(f'Valor de nodo {nodo_mid} es mayor a {searched_value}')
            high = mid - 1
            #print(f'new value of high {high}')
            #print(f'value is less than the mid')
               
            if high > 0:
               nodo_prev_mid = list_Q[mid - 1]
               # buscar si su anterior nodo en la lista tiene una longitud mayor, 
               # entonces pertenece en medio de esos valores
               if distance_values[nodo_prev_mid] < searched_value:
                  #print(f'but value grater than the previous one')   
                  value_found = 1
                  mid = mid - 1
            
         else:
            value_found = 1
      return mid
   
   def BFS(self, nodo_inicial: Nodo):
      discovered_nodes = list()
      discovered_nodes.append(nodo_inicial)
      nodo_inicial.explored()
      self.capas[1] = [nodo_inicial]
      num_capa = 1
      if (nodo_inicial not in self.nodes_list):
         return
      
      for node in self.nodes_list:
         self.bfs_dict[node] = []

      #print(f'Nodo incial {nodo_inicial} with id {id(nodo_inicial)}')
      while len(self.capas[num_capa]) > 0:
         num_capa += 1
         self.capas[num_capa] = list()
         list_nodos_adyacentes = list()
         #print(f'capa {num_capa-1}')

         for nodo in self.capas[num_capa-1]:
            #print(f'Nodos ad {nodo.nodos_adyacentes}')
            list_nodo_dict = list()

            for nodo_adyacente in nodo.nodos_adyacentes:
               #print(f'Nodo ad {nodo_adyacente} with id {id(nodo_adyacente)}')
               #print(f'Nodo ad Type {type(nodo_adyacente)}')

               if nodo_adyacente.nodo_explored == 0:
                  list_nodos_adyacentes.append(nodo_adyacente)
                  list_nodo_dict.append(nodo_adyacente)
                  nodo_adyacente.explored()
                  discovered_nodes.append(nodo_adyacente)
               #print(f' Discovered {discovered_nodes}')
            #print(f'for nodo {nodo} add {list_nodo_dict}')
            self.bfs_dict[nodo] = list_nodo_dict
         self.capas[num_capa] = list_nodos_adyacentes
      
      return len(discovered_nodes)

   def DFS_I(self, s: Nodo):
      nodo_1 = s
      if len(s.nodos_adyacentes) < 1:
         raise Exception("Choose a different node with ")
      else:
         nodo_2 = s.nodos_adyacentes[0]
      nodos_explorados = [nodo_1]
      nodos_lista_cambiante = [nodo_1]

      for node in self.nodes_list:
         self.dfs_i_dict[node] = []

      #num = 0
      while len(nodos_lista_cambiante) > 0:# and num < 10:
         new_edge = Arista_undirected(nodo_1, nodo_2)

         if (new_edge in self.edges_list) and nodo_2.nodo_explored == 0:
            #print("existe en las edges")
            nodo_2.explored()
            nodos_explorados.append(nodo_2)
            nodos_lista_cambiante.append(nodo_2)
            self.dfs_i_dict[nodo_1].append(nodo_2)

         if len(nodo_2.nodos_adyacentes) == 0:
            nodos_lista_cambiante.pop()
         
         nodo_aceptado = 0
         while (len(nodos_lista_cambiante) > 0 and nodo_aceptado == 0):# and num < 10):
            #num += 1
            for nodo_ad in nodos_lista_cambiante[-1].nodos_adyacentes:
               if nodo_ad not in nodos_explorados:
                  nodo_1 = nodos_lista_cambiante[-1]
                  nodo_2 = nodo_ad
                  nodo_aceptado = 1
                  #print(f'N1 {nodo_1} y N2 {nodo_2}')
                  break
            
            if nodo_aceptado == 0:
               nodos_lista_cambiante.pop()
               #print(f'Ahora la lista es {len(nodos_lista_cambiante)}')

      return True

   def DFS_R(self, nodo_1: Nodo):
      #print(f'Es el nodo: {s}')
      for nodo in nodo_1.nodos_adyacentes:
        # print(f'La arista {arista}')
         if nodo.nodo_explored == 0:

            if nodo_1 in self.dfs_r_dict:
               self.dfs_r_dict[nodo_1].append(nodo)
            else:
               self.dfs_r_dict[nodo_1] = [nodo]
         
            nodo_1.explored()
            nodo.explored()
            #print(f'arista is explored {arista.is_explored}')
            self.DFS_R(nodo)
      
   
   def Dijkstra(self, nodo_inicial: Nodo):
      """
      Algoritmo de camino mínimo
      """
      if len(nodo_inicial.nodos_adyacentes) < 1:
         #print(f'No tiene nodos adyacentes, intenta con otro')
         return
      
      # Set initial lists
      list_Q = [nodo_inicial]   # Priority queue
      list_S = []               # List of visited nodes 
      self.dict_distance_node[nodo_inicial] = 0    # Dictionary for distance to each node

      for node in self.nodes_list:
         self.dijkstra_dict[node] = []
         if node != nodo_inicial:
            list_Q.append(node)                          
            self.dict_distance_node[node] = 10000        # Create node with superior lenght

      #print(f'lista Q {list_Q}')
      while len(list_Q) > 0:
         list_S.append(list_Q[0])
         #print(f'lista S {list_S}')
         list_Q.pop(0)
         nodo_u = list_S[-1]

         for nodo_adyacente in nodo_u.nodos_adyacentes:
            if nodo_adyacente not in list_S:

               arista_adyacente =  Arista_undirected(nodo_u, nodo_adyacente)
               index_list_edges = self.edges_list.index(arista_adyacente)
               l_e = self.edges_list[index_list_edges].weight
               #print(f'le real arista {self.edges_list[index_list_edges]} con peso {l_e}')
               if self.dict_distance_node[nodo_adyacente] > self.dict_distance_node[nodo_u] + l_e: # or dict_distance_node[nodo_adyacente] == "INF":      
                  new_distance_value = self.dict_distance_node[nodo_u] + l_e
                   
                  #print(f'New distancia a {nodo_adyacente} es {new_distance_value}')
                  low = 0
                  high = len(list_Q) - 1
                  mid = 0
                  value_found = 0
                  while low <= high and value_found == 0:
                     mid = (high + low) // 2
                     nodo_mid = list_Q[mid]
                     
                     searched_value = new_distance_value
                     compared_value = self.dict_distance_node[nodo_mid]
                     
                     if compared_value < searched_value:
                        #print(f'Valor de nodo {nodo_mid} es menor a {searched_value}')
                        low = mid + 1
                        #print(f'new value of low {low}')
                         
                        if low < len(list_Q) - 1:
                           nodo_next_mid = list_Q[mid + 1]
                           #print(f'distancia del siguiente nodo es {self.dict_distance_node[nodo_next_mid]}')
                           if self.dict_distance_node[nodo_next_mid] > searched_value:
                               
                              value_found = 1
                              mid = mid + 1
                        
                     
                     elif compared_value > searched_value:
                        #print(f'Valor de nodo {nodo_mid} es mayor a {searched_value}')
                        high = mid - 1
                        #print(f'new value of high {high}')
                         
                        if high > 0:
                           nodo_prev_mid = list_Q[mid - 1]
                           #print(f'distancia del nodo anterior es {self.dict_distance_node[nodo_prev_mid]}')
                           if self.dict_distance_node[nodo_prev_mid] < searched_value:
                              value_found = 1
                              mid = mid - 1
                       
  
                     else:
                        value_found = 1
                  self.dict_distance_node[nodo_adyacente] = new_distance_value
                  #print(f'Posicion a insertar {mid}')
                  list_Q.pop(list_Q.index(nodo_adyacente))   # Remove from the list
                  list_Q.insert(mid, nodo_adyacente)         # Insert in new position
                  #print(f' New list Q: {list_Q}')
                  self.dijkstra_dict[nodo_adyacente] = [nodo_u] 
                  #print(f'{nodo_u} a nodo ad {nodo_adyacente}')
      #print(f'distancia de nodos {self.dict_distance_node}')
      #print(f'Grafo formado: {self.dijkstra_dict}')
   
   def KruskalD(self, grafo):
      """
      Algoritmo de expansión mínima
      """
      #print(self.edges_list)
      edges_list_KruskalD = self.sort_edges(self.edges_list)

      T_exp_min = []
      total_cost = 0
      
      root = dict()
      conj = dict()
      for node in self.nodes_list:
         root[node] = node
         conj[node] = 0
      
      for edge in edges_list_KruskalD:
         #print(f'edge {edge} and weight {edge.weight}')
         
         root_u = self.get_root(root, edge.n1)
         root_v = self.get_root(root, edge.n2)
         
         #print(f'node {edge.n1} root {root_u}')
         #print(f'node {edge.n2} root {root_v}')

         if root_u != root_v:
            #print("Es expansión mínima y se añade")
            T_exp_min.append(edge)
            root, conj = self.merge_graphs(root, conj, root_u, root_v)

            #print(f'new root {root}')
            #print(f'new conj {conj}')

      #print(f'edges exp min {T_exp_min}')
      return T_exp_min

   def KruskalI(self, grafo):
     
      edges_list_KrustalI = self.sort_edges(self.edges_list, False)
      modified_edges_list_KrustalI = copy.deepcopy(edges_list_KrustalI)
      num_nodos = len(self.nodes_list)
      #print(f'edges {edges_list_KrustalI}')
      for edge in edges_list_KrustalI:
         #print(f'peso del edge {edge.n1}-{edge.n2} es {edge.weight}')
         #print(f'Nodos ad de {edge.n1} son {edge.n1.nodos_adyacentes}')
         #print(f'Nodos ad de {edge.n2} son {edge.n2.nodos_adyacentes}')
         edge.n1.remove_nodo_adyacente(edge.n2)
         edge.n2.remove_nodo_adyacente(edge.n1)
         #print(f'Ahora nodos ad de {edge.n1} son {edge.n1.nodos_adyacentes}')

         self.not_explored_nodes()
         num_disc_nodes_1 = self.BFS(edge.n1)

         self.not_explored_nodes()
         num_disc_nodes_2 = self.BFS(edge.n2)
         
         #print(f'num nodos en n1 {num_disc_nodes_1} num nodos en n2 {num_disc_nodes_2}')
         if num_disc_nodes_1 == num_nodos and num_disc_nodes_2 == num_nodos:
            modified_edges_list_KrustalI.remove(edge)
         else:
            edge.n1.add_nodos_adyacentes(edge.n2)
            edge.n2.add_nodos_adyacentes(edge.n1)

         #print(f'Krustal edges {modified_edges_list_KrustalI}')
         #print(f'Orig Krustal edges {edges_list_KrustalI}')
      return modified_edges_list_KrustalI

   def Prim(self, grafo, nodo_incial): 
      """
      Para cálculo de árbol de expansión masiva, se escoge un nodo aleatorio 
      """
      #print(f'Grafo original {grafo.graph_dict}')
      
      dict_distancias = dict()
      list_Q = [nodo_incial]
      list_S = []

      for nodo in self.nodes_list:
         #print(f'edge add distance {nodo}')
         dict_distancias[nodo] = 1000000
         
         if nodo != nodo_incial:
            list_Q.append(nodo)
         
      #print(f'Lista Q {list_Q}')

      nodo_u = nodo_incial
      while len(list_Q) > 0:
         nodo_u = list_Q[0]
         list_Q.pop(0)
         list_S.append(nodo_u)

         for nodo_ad in nodo_u.nodos_adyacentes:
            arista_adyacente =  Arista_undirected(nodo_u, nodo_ad)
            index_list_edges = self.edges_list.index(arista_adyacente)
            l_e = self.edges_list[index_list_edges].weight
            arista_adyacente = self.edges_list[index_list_edges]

            #print(f'Arista {nodo_u} - {nodo_ad} con peso {l_e}')

            if ((nodo_ad not in list_S) and (l_e < dict_distancias[nodo_ad])):
               
               list_Q.pop(list_Q.index(nodo_ad))    # Remove from the list
               new_place_Q = self.sort_priority_queue(list_Q, dict_distancias, l_e)
               dict_distancias[nodo_ad] = l_e
               list_Q.insert(new_place_Q, nodo_ad)  # Actualizar lista de prioridades Q

               #print(f'Lista Q actualizada {list_Q}')
               #Actualizar diccionario de árbol de Prim
               self.prim_dict[nodo_ad] = [nodo_u]
         
         self.dict_distance_node = dict_distancias
   
   def draw_graph_eades(self, M = 2, c1 = 2, c2 = 1, c3 = 1, c4 = 0.1):
      def draw_node(pos_x, pos_y):
         nodo_pos = (pos_x*750, pos_y*750)
         return pygame.draw.circle(win, (255, 255, 255), nodo_pos, 3)
      
      def nodo_update(nodo):
         x = int((nodos_drawed_dict[nodo].center[0] * 750) / 750)
         y = int((nodos_drawed_dict[nodo].center[1] * 750) / 750)
         return draw_node(x,y)

      def draw_edge(nodo1, nodo2):
         pos_n1 = nodos_drawed_dict[nodo1].center
         pos_n2 = nodos_drawed_dict[nodo2].center

         pygame.draw.line(win, (255, 0, 0), pos_n1, pos_n2, 2)

      #def update_edge(nodo1, nodo2):
       #  pos_n1 = nodos_drawed_dict[nodo1].center
        # pos_n2 = nodos_drawed_dict[nodo2].center
         
      def distance_ang(pos_1, pos_2):
         x_n1 = pos_1[0]
         y_n1 = pos_1[1]
         x_n2 = pos_2[0]
         y_n2 = pos_2[1]
         d = math.sqrt((x_n1 - x_n2)**2 + (y_n1 - y_n2)**2)
         ang = math.atan2(x_n1 - x_n2, y_n1 - y_n2)
         return d, ang
      
      def suma_vectores(f1, ang1, nodo_fuerza):
         co_x_1 = f1 * math.cos(ang1)
         co_y_1 = f1 * math.sin(ang1)
         co_x_2 = nodo_fuerza[0] * math.cos(nodo_fuerza[1])
         co_y_2 = nodo_fuerza[0] * math.sin(nodo_fuerza[1])
         p1 = (co_x_1 + co_x_2, co_y_1 + co_y_2)
         f, ang = distance_ang(p1 , (0 ,0))
         return f,ang

      nodos_drawed_dict = dict()
      vec_fuerzas = dict()

      pygame.init()

      win = pygame.display.set_mode((750,750))

      pygame.display.set_caption("Graph disposition Eades")

      run = True

      while run:
         pygame.time.delay(100)

         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  run = False

         for nodo in self.nodes_list:
            x = random.random()
            y = random.random()
            nodos_drawed_dict[nodo] = draw_node(x,y)
            nodos_drawed_dict[nodo] = nodo_update(nodo)
            vec_fuerzas[nodo] = (0,0)


         for edge in self.edges_list:
            draw_edge(edge.n1, edge.n2)
         
         pygame.display.update()
         pygame.time.delay(1000)
         for i in range(1, M):
            for nodo_1 in self.nodes_list:
               for nodo_2 in self.nodes_list:
                  edge_created = Arista_undirected(nodo_1, nodo_2)
                  if nodo_1 != nodo_2:
                     pos1 = nodos_drawed_dict[nodo_1].center
                     pos2 = nodos_drawed_dict[nodo_2].center
                     distance, ang = distance_ang(pos1, pos2)
                     if edge_created in self.edges_list:
                        fuerza = c1 * numpy.log(distance/c2) 
                     elif distance == 0:
                        fuerza = 0
                     else:
                        fuerza = c3 / math.sqrt(distance)
                     print(f'fuerza {fuerza}')
                     #sumamos fuerzas
                     fue_f1, ang_f1 = suma_vectores(fuerza, ang, vec_fuerzas[nodo_1])
                     vec_fuerzas[nodo_1] = (fue_f1, ang_f1)
                     print(f'Fuerza y angulo ({fue_f1}, {ang_f1})')

                     fue_f2, ang_f2 = suma_vectores(fuerza, ang, vec_fuerzas[nodo_2])
                     vec_fuerzas[nodo_2] = (fue_f2, ang_f2)

                     co_x_1 = c4 * vec_fuerzas[nodo_1][0] * math.cos(vec_fuerzas[nodo_1][1])
                     co_y_1 = c4 * vec_fuerzas[nodo_1][0] * math.sin(vec_fuerzas[nodo_1][1])

                     co_x_2 = c4 * vec_fuerzas[nodo_2][0] * math.cos(vec_fuerzas[nodo_2][1])
                     co_y_2 = c4 * vec_fuerzas[nodo_2][0] * math.sin(vec_fuerzas[nodo_2][1])

                     nodos_drawed_dict[nodo_1] = draw_node(pos1[0]+co_x_1, pos1[1]+co_y_1)
                     nodos_drawed_dict[nodo_2] = draw_node(pos2[0]+co_x_2, pos2[1]+co_y_2)

                     print(f'x {nodos_drawed_dict[nodo_1].center[0]}, y {nodos_drawed_dict[nodo_1].center[1]}')

                     pygame.display.update()

         pygame.time.delay(1000)
         run = False
         #minor change

      pygame.quit()

   