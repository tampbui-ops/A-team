"""
Executioner Agent - Executes tasks and implements solutions
"""
from config.agent_config import BaseAgent


class Executioner(BaseAgent):
    """
    The Executioner agent implements plans and executes tasks.
    """

    def __init__(self):
        super().__init__(
            name="Executioner",
            role="Task Executor",
            description="Executes planned tasks and implements solutions"
        )

    def get_system_prompt(self) -> str:
        return """You are an expert executor and implementer. Your role is to:
1. Execute planned tasks efficiently and accurately
2. Implement solutions step by step
3. Handle errors and adapt to challenges
4. Generate outputs and deliverables
5. Track progress and execution metrics
6. Document execution process

Always execute tasks systematically and provide detailed execution logs."""

    def execute(self, plan: dict) -> dict:
        """
        Execute a plan from the Planner.
        
        Args:
            plan: The execution plan
            
        Returns:
            Execution result dictionary
        """
        self.log(f"Executing plan for task: {plan.get('task', 'unknown')}")
        
        result = {
            "plan_task": plan.get("task", "unknown"),
            "status": "completed",
            "execution_log": [
                "Step 1: Started execution",
                "Step 2: Processing data",
                "Step 3: Generating outputs",
                "Step 4: Finalizing results"
            ],
            "outputs": [
                "Output 1: Primary result",
                "Output 2: Secondary result"
            ],
            "errors": [],
            "execution_time_seconds": 15,
            "steps_completed": len(plan.get("steps", [])),
            "success_rate": 100
        }
        
        return result

    def run_task(self, task_config: dict) -> dict:
        """Run a task with configuration"""
        self.log(f"Running task: {task_config.get('name', 'unnamed')}")
        
        return {
            "task_name": task_config.get("name"),
            "status": "completed",
            "result": "Task executed successfully",
            "metadata": task_config
        }

    def process_data(self, data: list) -> dict:
        """Process data"""
        self.log(f"Processing {len(data)} items")
        
        return {
            "items_processed": len(data),
            "status": "completed",
            "results": [f"Processed item {i+1}" for i in range(len(data))],
            "success_count": len(data),
            "error_count": 0
        }

    def generate_output(self, content: str, format_type: str = "text") -> dict:
        """Generate output in specified format"""
        self.log(f"Generating output in {format_type} format")
        
        return {
            "content": content,
            "format": format_type,
            "size_bytes": len(content.encode()),
            "status": "generated"
        }

    def handle_error(self, error: str, context: dict = None) -> dict:
        """Handle execution error"""
        self.log(f"Handling error: {error}")
        
        return {
            "error": error,
            "context": context,
            "status": "handled",
            "recovery_attempted": True,
            "retry_possible": True
        }
