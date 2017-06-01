
# coding: utf-8

# In[2]:

from py2neo import authenticate, Graph

host     = "127.0.0.1:7474/"
user     = "neo4j"
password = "neo4jresearch"

authenticate(host, user, password)
graph = Graph("http://"+ host)

