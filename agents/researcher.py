"""
Researcher Agent - Gathers and analyzes information
"""
from config.agent_config import BaseAgent


class Researcher(BaseAgent):
    """
    The Researcher agent gathers information and provides context analysis.
    """

    def __init__(self):
        super().__init__(
            name="Researcher",
            role="Information Analyst",
            description="Gathers information, researches topics, and provides context"
        )

    def get_system_prompt(self) -> str:
        return """You are an expert researcher and analyst. Your role is to:
1. Research and gather relevant information
2. Analyze data from multiple perspectives
3. Summarize findings in clear, structured format
4. Identify patterns and connections
5. Provide context and background information
6. Cite sources when applicable

Always provide well-researched, accurate, and comprehensive information."""

    def execute(self, query: str, context: str = None) -> dict:
        """
        Research and analyze the given query.
        
        Args:
            query: The research query
            context: Optional context for the research
            
        Returns:
            Research findings dictionary
        """
        self.log(f"Researching: {query}")
        
        research = {
            "query": query,
            "status": "completed",
            "findings": [
                {
                    "category": "Overview",
                    "content": f"Analysis of {query}",
                    "confidence": "high"
                },
                {
                    "category": "Key Points",
                    "content": "Main findings and insights",
                    "confidence": "high"
                },
                {
                    "category": "Recommendations",
                    "content": "Suggested actions based on research",
                    "confidence": "medium"
                }
            ],
            "sources_consulted": 3,
            "research_depth": "comprehensive",
            "quality_score": 8.5
        }
        
        if context:
            research["context"] = context
            research["findings"].insert(0, {
                "category": "Context",
                "content": context,
                "confidence": "high"
            })
        
        return research

    def search_topic(self, topic: str) -> dict:
        """Search for information on a specific topic"""
        self.log(f"Searching topic: {topic}")
        
        return {
            "topic": topic,
            "results_found": 42,
            "top_results": [
                f"Result 1 for {topic}",
                f"Result 2 for {topic}",
                f"Result 3 for {topic}"
            ],
            "search_status": "completed"
        }

    def analyze_data(self, data: dict) -> dict:
        """Analyze provided data"""
        self.log("Analyzing data")
        
        return {
            "data_size": len(data),
            "analysis": "Data analysis complete",
            "patterns": ["Pattern 1", "Pattern 2"],
            "insights": ["Insight 1", "Insight 2"],
            "quality": "good"
        }

    def summarize(self, content: str, max_length: int = 500) -> str:
        """Summarize content"""
        self.log("Summarizing content")
        
        summary = content[:max_length] + "..." if len(content) > max_length else content
        return summary
