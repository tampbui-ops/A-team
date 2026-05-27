"""
Base Agent Configuration
"""
import logging
from typing import List, Optional


class BaseAgent:
    """
    Base class for all agents in the A-team system.
    Provides common functionality for planning, researching, executing, and checking.
    """
    
    def __init__(self, name: str, role: str, description: str):
        """
        Initialize a base agent.
        
        Args:
            name: Agent name
            role: Agent role/responsibility
            description: Agent description
        """
        self.name = name
        self.role = role
        self.description = description
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """Setup logging for the agent"""
        logger = logging.getLogger(self.name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            f'[{self.name}] %(asctime)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
    
    def log(self, message: str, level: str = "info"):
        """Log a message"""
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
    
    def get_system_prompt(self) -> str:
        """Get system prompt for GPT. Override in subclasses."""
        return f"You are {self.name}, a {self.role}. {self.description}"
    
    def get_info(self) -> dict:
        """Get agent information"""
        return {
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "system_prompt": self.get_system_prompt()
        }
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.role})"
