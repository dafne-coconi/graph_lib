from datetime import datetime
import random
import math

class Nodo:
   """
   Clase Nodo
   :param value: number of nodes
   """
   def __init__(self):
      self.name = str
      self.node_list = list()

   def get_name(self, name):
      self.name = f'N{name}'
      return self.name
      
   def get_node_list(self, m = 1, n = 1):
      list_of_lists = [[0 for i in range(1, n + 1)] for _ in range(m)]
      #print(list_of_lists)
      
      num_nodos = 0
      for i in range(m):
         for j in range(n):
            #print(list_of_lists[i][j])
            num_nodos += 1
            node = self.get_name(f'{num_nodos}')
            list_of_lists[i][j] = node
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
         

   #def add_edges(self, edge):
    #  self.edges_to_node.append(edge)


class Arista_undirected:
   """
   Clase Arista
   :param value: number of nodes
   """
   def __init__(self, n1, n2, weight = 1):
      self.n1 = n1
      self.n2 = n2
      self.lista_arista = list()
      self.weight = weight
        
   def get_n1(self):
      return self.n1

   def get_n2(self):
      return self.n2
   
   def create_list_arista(self):
      self.lista_arista = [self.n1, self.n2, self.weight]
      return self.lista_arista
   
   def __str__(self):
      return self.n1.get_name() + " -> " + self.n2.get_name()
   
   def __cmp__(self, other):
      return (self.lista_arista[0] == other.lista_arista[0] and self.lista_arista[1] == other.lista_arista[1]) or (self.lista_arista[0] == other.lista_arista[1] and self.lista_arista[1] == other.lista_arista[0])

   
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
    
   def new_edge(self, n1, n2, weight = 1):
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
       
       new_arista = edge.create_list_arista()
       if edge not in self.edges_list: 
         self.edges_list.append(edge.create_list_arista())
       #print(self.edges_list)
       #print(self.nodes_list)

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
         
      for node in self.nodes_list:
         self.graph_dict[node] = []

      #print(self.graph_dict)
      #print(self.edges_list)
      for edge in self.edges_list:
         list_value = list()
         #print(f'edge {edge}')
         for node in self.nodes_list:
            if (node in [edge[0]]) and (edge[1] not in self.graph_dict[node]):
               list_value = self.graph_dict[node]
               list_value.append(edge[1])
               #self.graph_dict[node]
               #self.graph_dict.setdefault(node, []).append(edge[1])
            #print(list_value)
         self.graph_dict[node] = list_value
      #print(f'Nodes {self.nodes_list}')
      #print(f'Edges {self.edges_list}')
      #print(f'Graph {self.graph_dict}')

   def save_graph(self):
      current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
      filename = f"{self.name}_{len(self.nodes_list)}_{current_datetime}.dot"    
      filepath = f"archivos/{filename}"

      list_v = []
      with open(filepath, "w", encoding="UTF") as file:
         file.write(f"graph {self.name}" + "{\n")
         count = 0
         line = str
         for key in self.graph_dict:
            value = self.graph_dict[key]
            if (len(value) > 0):
        
               for single_value in value:
                  if key == single_value:
                     continue
                  #print(single_value)
                  #line = f'{key} ->' + '{' + f'{value_as_string}' + '}\n'
                  line = f'{key} -> ' + f'{single_value}' + ';\n'
                  file.write(line)

            else:
               line = f'{key}'+ '\n'
               file.write(line)
            
            
         file.write("\n}")

      print(f"Graph saved to {filepath} ")