"""This file contains various methods to setup Markov chains
as random walks on graphs from the networkx package.
"""

import markovmixing as mkm

def nx_graph_srw(G):
	"""Returns the srw on the graph G 
	"""
	import networkx as nx

	A = nx.to_scipy_sparse_matrix(G)
	P = mkm.graph_srw_transition_matrix(A)
	mc = mkm.MarkovChain(P)
	mc.set_stationary_distribution(mkm.graph_srw_stationary_distribution(A))

	return mc

def nx_graph_lazy_srw(G):
	"""Returns the lazy srw on the graph G 
	"""
	import networkx as nx

	A = nx.to_scipy_sparse_matrix(G)
	P = mkm.lazy(mkm.graph_srw_transition_matrix(A))
	mc = mkm.MarkovChain(P)
	mc.set_stationary_distribution(mkm.graph_srw_stationary_distribution(A))

	return mc

def nx_graph_nbrw(G):
	import networkx as nx

	A = nx.to_scipy_sparse_matrix(G)
	P = mkm.graph_nbrw_transition_matrix(A)
	mc = mkm.MarkovChain(P)
	mc.set_stationary_distribution(mkm.uniform_distribution(mc.get_n()))

	return mc

def nx_graph_analyze_lazy_srw(G): # pragma: no cover
	import networkx as nx
	import matplotlib.pyplot as plt

	mc = mkm.nx_graph_lazy_srw(G)
	mc.add_distributions(mkm.random_delta_distributions(mc.get_n(),5))
	
	mc.compute_tv_mixing()

	plt.figure()
	for i in range(mc.num_distributions()):
		(x,tv) = mc.distribution_tv_mixing(i)
		plt.plot(x, tv)

	plt.xlabel("t")
	plt.ylabel("Distance to stationary distribution in total variation")
	plt.show()	

def nx_graph_analyze_nbrw(G): # pragma: no cover
	import networkx as nx
	import matplotlib.pyplot as plt

	mc = mkm.nx_graph_nbrw(G)
	mc.add_distributions(mkm.random_delta_distributions(mc.get_n(),5))
	
	mc.compute_tv_mixing()

	plt.figure()
	for i in range(mc.num_distributions()):
		(x,tv) = mc.distribution_tv_mixing(i)
		plt.plot(x, tv)

	plt.xlabel("t")
	plt.ylabel("Distance to stationary distribution in total variation")
	plt.show()	
