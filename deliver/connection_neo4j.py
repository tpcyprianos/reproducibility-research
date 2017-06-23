
# coding: utf-8

# ## Connecting Neo4j from Python
# For connecting the Graph Database to Python, I am using [Py2neo](http://py2neo.org/v3/) Driver. There are some options of [Neo4j-Python Drivers](https://neo4j.com/developer/python/#neo4j-python-driver), but for these experiments, the official documentation of Py2neo showed be enough, according the official documentation: 
# >"*Py2neo provides a set of core graph data types that are completely compatible with Neo4j but that can also be used independently of it. These types include the fundamental entities Node and Relationship as well as classes that represent collections of these entities.*"
# 
# Before use this program code, you may check:
# 1. The py2neo is installed correctly (look at the [documentation](http://py2neo.org/v3/)):
# ```
# pip install py2neo
# ```
# 2. Your Neo4j server is started (locally or container Docker)
# 3. The parameters of host, user and password of graph database are corrects

# In[1]:

from py2neo import authenticate, Graph, Node

host     = "192.168.99.100:7474"
user     = "neo4j"
password = "neo4jresearch"

authenticate(host, user, password)
graph = Graph("http://"+ host)

