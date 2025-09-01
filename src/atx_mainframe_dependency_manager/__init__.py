"""
ATX Mainframe Dependency Manager

A Model Context Protocol (MCP) server for managing mainframe component dependencies and relationships.
This package provides tools for analyzing, tracking, and managing dependencies between mainframe
components such as COBOL programs, JCL jobs, and copybooks.
"""

__version__ = "0.1.0"
__author__ = "Arunkumar Selvam"
__email__ = "aruninfy123@gmail.com"

from .dependency_manager import DependencyManager
from .server import main

__all__ = ["DependencyManager", "main"]
