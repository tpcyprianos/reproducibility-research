# Delivery 

In this directory you will find the [Paper](paper.ipynb) the corresponding ``.tex``, the ``references.bib`` and the codes used in the experiment.

## Workflow 

The workflow with the inputs and outputs of this research is organized as follows:

![Workflow Research](../figures/Research.png)

## Execute the experiment

To execute the experiment, follow the steps:

1. Make sure you have did all installation steps (described in ``\environment``). 
2. Start your Neo4j Server.
3. Verifiy the code ``connection_neo4j.ipynb``. The ``host``, ``user`` and ``password`` need to be corrects. 
3. Follow the workflow image: first, execute the Prepreprocessing (``preprocessing_data.ipynb``).
4. Secondly, execute the ``indexing_data.ipynb``.
5. Open the Neo4j Server in Browser, the graph generated can be visualized.