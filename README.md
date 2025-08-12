# planning-graph

This library implements Planning Graph and its planner that can be used to solve STRIPS-like AI Planning Problems using PDDL. Planning graphs and associated planner was first introduced in:

* A. Blum and M. Furst (1997). [Fast planning through planning graph analysis](https://www.sciencedirect.com/science/article/pii/S0004370296000471). Artificial intelligence. 90:281-300.

Given a domain and problem in PDDL, the library can comptue the planning graph, output it to an image, as well as compute a solution plan from it if any exists.

An associated post to this repo can be found at [here](https://towardsdatascience.com/improving-classical-ai-planning-complexity-with-planning-graph-c63d47f87018).

## Installation

Alternatively, it can be installed directly from the repo:

```console
pip install git+https://github.com/COSC1127-AI/planning_graph
```

or, clone the repository and install:

```shell
$ git clone https://github.com/COSC1127-AI/planning_graph
$ cd fond-utils
$ pip install .
```

For development, it is best to install the package as editable: `pip install -e .`

> [!CAUTION]
> The original repo publishes in PyPi [here](https://pypi.org/project/planning-graph/), but it is currently different from the version provided in this repo.

## CLI Usage

## As a library

To create a Planning Graph from PDDL:

```python
from planning_graph.planning_graph import PlanningGraph


planning_graph = PlanningGraph('domain/dock-worker-robot-domain.pddl',
                               'domain/dock-worker-robot-problem.pddl')

graph = planning_graph.create(max_num_of_levels=10)
```

`planning_graph.create()` returns a Graph object if the goal state is achieved, or the maximum number of levels have been reached.

To create an image visualization of the planning graph, you can set `visualize=True` (by default
it is set to `False`) and then visualize it as a PNG image:

```python
from planning_graph.planning_graph import PlanningGraph


planning_graph = PlanningGraph('domain/dock-worker-robot-domain.pddl',
                               'domain/dock-worker-robot-problem.pddl',
                               visualize=True)

graph = planning_graph.create(max_num_of_levels=10)
graph.visualize_png("generated_graph.png")
```

The result looks like the following:

![alt text](domain/planning_graph.png)

### Find a solution plan

To find a solution plan you simply have to create a Planner and pass the arguments it requires.

```python
from planning_graph.planning_graph import PlanningGraph
from planning_graph.planning_graph_planner import GraphPlanner


planning_graph = PlanningGraph('domain/dock-worker-robot-domain.pddl',
                               'domain/dock-worker-robot-problem.pddl')

graph = planning_graph.create(max_num_of_levels=10)
goal = planning_graph.goal
graph_planner = GraphPlanner()
layered_plan = graph_planner.plan(graph, goal)
```

This returns a layered plan if the solution exists, otherwise, it returns `None`.

## pddlpy

`pddlpy` included in this repo is the work of Hernán M. Foffani, it is copied from [here.](https://github.com/hfoffani/pddl-lib). It is copied because it won't work when installed as a package due to wrong version of antlr4 package. There are no changes made to it.

> [!NOTE]
> Would be best to migrate the parser to [pddl](https://github.com/AI-Planning/pddl) - see issue [#3](https://github.com/COSC1127-AI/planning_graph/issues/3)
