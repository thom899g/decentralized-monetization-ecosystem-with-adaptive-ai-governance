import logging
from typing import Any

class ModuleBase:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def log_info(self, message: str) -> None:
        """Logs an informational message."""
        self.logger.info(message)
    
    def log_error(self, message: str) -> None:
        """Logs an error message."""
        self.logger.error(message)
    
    def handle_exception(self, e: Exception, message: str = "An error occurred") -> None:
        """Handles exceptions and logs them."""
        self.logger.error(f"{message}: {str(e)}")
        raise