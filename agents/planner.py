"""
Planner Agent - Creates task plans and strategies
"""
from config.agent_config import BaseAgent


class Planner(BaseAgent):
    """
    The Planner agent analyzes tasks and creates structured execution plans.
    """

    def __init__(self):
        super().__init__(
            name="Planner",
            role="Task Strategist",
            description="Analyzes tasks and creates structured execution plans"
        )

    def get_system_prompt(self) -> str:
        return """You are an expert strategic planner. Your role is to:
1. Analyze complex tasks and break them into manageable steps
2. Identify dependencies and potential roadblocks
3. Create clear, actionable execution plans
4. Define success criteria and milestones
5. Prioritize tasks by importance and sequence
6. Estimate resource requirements

Always provide structured, logical plans that can be executed sequentially."""

    def execute(self, task: str) -> dict:
        """
        Create a plan for the given task.
        
        Args:
            task: The task to plan
            
        Returns:
            A structured plan dictionary
        """
        self.log(f"Planning task: {task}")
        
        plan = {
            "task": task,
            "status": "planned",
            "steps": [
                {
                    "step": 1,
                    "action": "Analyze requirements",
                    "description": "Understand the task requirements and constraints",
                    "priority": "high"
                },
                {
                    "step": 2,
                    "action": "Research context",
                    "description": "Gather relevant background information",
                    "priority": "high"
                },
                {
                    "step": 3,
                    "action": "Execute solution",
                    "description": "Implement the planned solution",
                    "priority": "high"
                },
                {
                    "step": 4,
                    "action": "Validate results",
                    "description": "Check quality and accuracy",
                    "priority": "high"
                }
            ],
            "success_criteria": [
                "Task completed successfully",
                "All steps executed",
                "Quality checks passed",
                "Documentation provided"
            ],
            "estimated_duration": "1-2 hours"
        }
        
        return plan

    def plan_task(self, task: str, context: str = None) -> dict:
        """
        Create a detailed plan with optional context.
        
        Args:
            task: The main task
            context: Optional context information
            
        Returns:
            Detailed execution plan
        """
        self.log(f"Creating detailed plan for: {task}")
        
        plan = self.execute(task)
        if context:
            plan["context"] = context
            plan["steps"][1]["description"] += f" (Context: {context})"
        
        return plan

    def break_down_task(self, task: str, max_steps: int = 5) -> List[str]:
        """Break down task into subtasks"""
        subtasks = [
            f"Step {i+1}: Subtask for {task}"
            for i in range(min(max_steps, 4))
        ]
        return subtasks
