from datetime import datetime
import random
import math

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
   def __init__(self, n1: Nodo, n2: Nodo, weight = 1):
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
      self.weight = random.randint(2,50)
      #self.lista_arista = [self.n1, self.n2, self.weight]
      self.lista_arista = [self.n1, self.n2]
      self.n1.add_nodos_adyacentes(self.n2)
      self.n2.add_nodos_adyacentes(self.n1)
      return self.lista_arista
   
   def explored(self):
      self.is_explored = 1
   
   def __repr__(self):
        #return f'[{self.n1}, {self.n2}, {self.weight}]'
        return f'[{self.n1}, {self.n2}]'
        
   
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
      self.dict_distance_node = {}
      #for node in self.nodes_list:
       #  self.dfs_r_dict[node] = []
    
   def new_edge(self, n1: Nodo, n2: Nodo, weight = 1):
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
            if (len(value) > 0):
        
               for single_value in value:
                  if key == single_value:
                     continue
                  #print(single_value)
                  #line = f'{key} ->' + '{' + f'{value_as_string}' + '}\n'
                  if type_graph == "DIJKSTRA":
                     line = f'{single_value}_{self.dict_distance_node[single_value]} -> ' + f'{key}_{self.dict_distance_node[key]}' + ';\n'
                     file.write(line)
                  else:
                     line = f'{key} -> ' + f'{single_value}' + ';\n'
                     file.write(line)

            else:
               if type_graph == "DIJKSTRA":
                  line = f'{key}_0'+ '\n'
               else:
                  line = f'{key}'+ '\n'
               file.write(line)
            
            
         file.write("\n}")

      #print(self.edges_list)
      print(f"Graph saved to {filepath} ")

   def save_graph_edges(self, type_graph: str ):
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
      else:
         graph = self.graph_dict
         #print(f'grafo regular {self.graph_dict}')
         filename = f"{self.name}_edges_{len(self.nodes_list)}_{current_datetime}.dot"
   
      
          
      filepath = f"archivos/{filename}"

      list_v = []
      with open(filepath, "w", encoding="UTF") as file:
         file.write(f"graph {self.name}" + "{\n")
         count = 0
         line = str
         for edge in self.edges_list:
            
            line = f'{edge.n1} -> ' + f'{edge.n2}[Label={edge.weight}]' + ';\n'
            file.write(line)
            
         file.write("\n}")

      #print(self.edges_list)
      print(f"Graph saved to {filepath}")

   def not_explored_nodes(self):
      for node in self.nodes_list:
         node.not_explored()

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
         new_edge = Arista_undirected(nodo_1, nodo_2, weight = 1)

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
         print(f'No tiene nodos adyacentes, intenta con otro')
         return
      list_Q = [nodo_inicial]
      
      list_S = []
      self.dict_distance_node[nodo_inicial] = 0

      for node in self.nodes_list:
         self.dijkstra_dict[node] = []
         if node != nodo_inicial:
            list_Q.append(node)
            self.dict_distance_node[node] = 10000

      #print(f'lista Q {list_Q}')
      while len(list_Q) > 0:
         list_S.append(list_Q[0])
         #print(f'lista S {list_S}')
         list_Q.pop(0)
         nodo_u = list_S[-1]

         for nodo_adyacente in nodo_u.nodos_adyacentes:
            if nodo_adyacente not in list_S:
               #print(f'Nodo adyacente {nodo_adyacente}')
               arista_adyacente =  Arista_undirected(nodo_u, nodo_adyacente)
               #print(f'le arista adyacente {arista_adyacente}')
               #print(f'dict {self.dict_distance_node}')
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
      
                        
                           
                      