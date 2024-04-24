from libGraph import mesh_graph, erdos_renyi_graph, gilbert_graph, geografico_simple_graph, barabasi_albert_graph, dorogovtsev_mendes_graph

#mesh_graph(m = 3, n = 10, dirigido = False)
#mesh_graph(10,10, False)
#mesh_graph(10,50, False)

#erdos_renyi_graph(30, 35, False)
#erdos_renyi_graph(100, 120, False)
#erdos_renyi_graph(500, 520, False)

#gilbert_graph(30, 0.9, False)
#gilbert_graph(100, 0.9, False)
#gilbert_graph(500, 0.9, False)

#geografico_simple_graph(30, 0.3, False)
#geografico_simple_graph(100, 0.3, False)
#geografico_simple_graph(500, 0.15, False)

barabasi_albert_graph(30,2, False)
#barabasi_albert_graph(100,2, False)
#barabasi_albert_graph(500,2, False)

#dorogovtsev_mendes_graph(30, False)
#dorogovtsev_mendes_graph(100, False)
dorogovtsev_mendes_graph(500, False)