class PlannerAgent:
    def plan(self, task):
        # Simple task decomposition
        return [
            f"Analyze task: {task}",
            f"Generate solution for: {task}",
            f"Summarize results for: {task}"
        ]