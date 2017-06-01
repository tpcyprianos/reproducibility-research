
# coding: utf-8

# In[3]:

from py2neo import authenticate, Graph, Node

host     = "127.0.0.1:7474/"
user     = "neo4j"
password = "neo4jresearch"

authenticate(host, user, password)
graph = Graph("http://"+ host)

