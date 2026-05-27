"""
Checker Agent - Validates outputs and ensures quality
"""
from config.agent_config import BaseAgent


class Checker(BaseAgent):
    """
    The Checker agent validates results against criteria,
    identifies issues, and ensures quality standards.
    """

    def __init__(self):
        super().__init__(
            name="Checker",
            role="Quality Assurance",
            description="Validates outputs, checks quality, and ensures accuracy"
        )

    def get_system_prompt(self) -> str:
        return """You are an expert quality assurance specialist. Your role is to:
1. Validate results against defined criteria and standards
2. Identify errors, inconsistencies, or gaps
3. Provide detailed feedback for improvements
4. Ensure deliverables meet all requirements
5. Document issues with severity levels
6. Recommend corrections and refinements

Always be thorough and provide constructive feedback with actionable recommendations."""

    def execute(self, results: dict, criteria: dict = None):
        """
        Check and validate execution results.
        
        Args:
            results: The execution results to validate
            criteria: Success criteria to validate against
            
        Returns:
            Validation report dict with issues and recommendations
        """
        report = {
            "results_task": results.get("plan_task", "Unknown"),
            "validation_status": "passed",
            "issues": [],
            "recommendations": [],
            "quality_score": 100,
            "details": {}
        }
        
        # Basic validation checks
        checks = [
            {"name": "Completion Status", "passed": results.get("status") == "completed"},
            {"name": "No Critical Errors", "passed": len(results.get("errors", [])) == 0},
            {"name": "Has Outputs", "passed": len(results.get("outputs", [])) > 0},
            {"name": "Execution Log Present", "passed": len(results.get("execution_log", [])) > 0}
        ]
        
        failed_checks = [c for c in checks if not c["passed"]]
        
        if failed_checks:
            report["validation_status"] = "failed"
            report["quality_score"] = 100 - (len(failed_checks) * 25)
            
            for check in failed_checks:
                report["issues"].append(f"Failed: {check['name']}")
        
        # Add recommendations
        if results.get("errors"):
            report["recommendations"].append("Review and resolve reported errors")
        
        if report["quality_score"] < 100:
            report["recommendations"].append("Re-execute with corrections")
        
        report["details"] = {
            "checks_performed": len(checks),
            "checks_passed": len(checks) - len(failed_checks),
            "checks_failed": len(failed_checks)
        }
        
        return report

    def validate_against_criteria(self, output: str, criteria: list) -> dict:
        """Validate output against specific criteria"""
        validation = {
            "output_length": len(output),
            "criteria_met": 0,
            "criteria_total": len(criteria),
            "all_met": False,
            "details": []
        }
        
        for criterion in criteria:
            met = criterion.lower() in output.lower()
            validation["details"].append({
                "criterion": criterion,
                "met": met
            })
            if met:
                validation["criteria_met"] += 1
        
        validation["all_met"] = validation["criteria_met"] == validation["criteria_total"]
        
        return validation

    def generate_report(self, validation: dict) -> str:
        """Generate a detailed validation report"""
        report = f"""
Quality Assurance Report
======================
Task: {validation.get('results_task', 'N/A')}
Status: {validation.get('validation_status', 'N/A')}
Quality Score: {validation.get('quality_score', 0)}%

Issues Found:
{chr(10).join(f'- {issue}' for issue in validation.get('issues', ['None'])) if validation.get('issues') else '- None'}

Recommendations:
{chr(10).join(f'- {rec}' for rec in validation.get('recommendations', ['None'])) if validation.get('recommendations') else '- None'}

Details:
- Checks Performed: {validation.get('details', {}).get('checks_performed', 0)}
- Checks Passed: {validation.get('details', {}).get('checks_passed', 0)}
- Checks Failed: {validation.get('details', {}).get('checks_failed', 0)}
"""
        return report
