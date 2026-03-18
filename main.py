from agents.planner import PlannerAgent
from agents.worker import WorkerAgent
from agents.verifier import VerifierAgent


def main():
    user_task = input("Enter a task: ")

    planner = PlannerAgent()
    worker = WorkerAgent()
    verifier = VerifierAgent()


    print("\n[Planner] Breaking task into steps...")
    steps = planner.plan(user_task)

    results = []
    for step in steps:
        print(f"\n[Worker] Executing: {step}")
        result = worker.execute(step)
        results.append(result)

    print("\n[Verifier] Checking results...")
    verification = verifier.verify(results)

    print("\nFinal Output:")
    print(verification)

if __name__ == "__main__":
    main()
    print("wokring")