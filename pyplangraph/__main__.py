import argparse

from . import VERSION

from .planning_graph import PlanningGraph, NoOpAction
from .planning_graph_planner import GraphPlanner


def main():
    parser = argparse.ArgumentParser(description=f"Generate a planning graph for a planning problem - Version {VERSION}.")
    parser.add_argument(
        "DOMAIN",
        type=str,
        help="Path to the domain PDDL file",
    )
    parser.add_argument(
        "PROBLEM",
        type=str,
        help="Path to the problem PDDL file",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="Maximum number of levels in the planning graph (Default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="planning_graph.png",
        help="Output filename for the planning graph visualization (Default: %(default)s)",
    )
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Generate a layered plan from the planning graph",
    )
    args = parser.parse_args()

    planning_graph = PlanningGraph(
        args.DOMAIN,
        args.PROBLEM,
        visualize=True,
    )
    graph = planning_graph.create(max_num_of_levels=args.max)
    print(f"Planning graph created with {graph} levels.")
    graph.visualize_png(args.output)

    if args.plan:
        goal = planning_graph.goal
        graph_planner = GraphPlanner()
        layered_plan = graph_planner.plan(graph, goal, planning_graph)
        if layered_plan is None:
            print("No plan can be generated.")
            exit(1)

        print(f"Layered plan: {layered_plan}")
        for k in layered_plan.data:
            plan = [str(x) for x in layered_plan.data[k].plan if not isinstance(x, NoOpAction)]
            print(k, plan)


if __name__ == "__main__":
    main()
