from pyplangraph.planning_graph import PlanningGraph, NoOpAction
from pyplangraph.planning_graph_planner import GraphPlanner


if __name__ == "__main__":
    # Create planning graph with visualization enabled
    planning_graph = PlanningGraph(
        "domain/dock-worker-robot-domain.pddl",
        "domain/dock-worker-robot-problem.pddl",
        visualize=True,
    )

    # Generate the graph
    graph = planning_graph.create(max_num_of_levels=10)
    print(f"Planning graph created with {graph} levels.")

    # Save visualization
    graph.visualize_png("my_planning_graph.png")

    # Extract a plan
    goal = planning_graph.goal
    graph_planner = GraphPlanner()
    layered_plan = graph_planner.plan(graph, goal, planning_graph)

    if layered_plan is None:
        print("No plan can be generated.")
    else:
        print(f"Layered plan: {layered_plan}")
        for k in layered_plan.data:
            plan = [
                str(x) for x in layered_plan.data[k].plan if not isinstance(x, NoOpAction)
            ]
            print(f"Level {k}: {plan}")
