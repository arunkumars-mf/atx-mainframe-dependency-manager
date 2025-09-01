# ATX Mainframe Dependency Manager

A Model Context Protocol (MCP) server for managing mainframe component dependencies and relationships.

## Features

- **Dependency Analysis**: Analyze direct and recursive dependencies between mainframe components
- **Impact Assessment**: Understand the impact of changes to specific components  
- **Component Discovery**: Find components by name, type, or file path
- **Orphan Detection**: Identify unused components with no dependencies or dependents
- **Statistics and Reporting**: Get comprehensive statistics about your mainframe codebase
- **Source Code Access**: Read and analyze mainframe source code files

## Installation

```bash
pip install atx-mainframe-dependency-manager
```

## Configuration

Set these environment variables:

- `ATX_MF_DEPENDENCIES_FILE`: Path to the JSON file containing dependency data
- `ATX_MF_CODE_BASE`: Base path for mainframe source code

```bash
export ATX_MF_DEPENDENCIES_FILE="/path/to/dependencies.json"
export ATX_MF_CODE_BASE="/mainframe/source"
```

## Dependencies JSON Format

```json
[
  {
    "name": "PAYROLL",
    "type": "COB", 
    "path": "/mainframe/cobol/PAYROLL.cob",
    "dependencies": [
      {
        "name": "EMPLOYEE",
        "dependencyType": "COPY"
      }
    ]
  }
]
```

## Analysis Tools

### Component Analysis
- `get_component_info` - Get detailed component information
- `get_component_dependencies` - Get direct dependencies
- `get_recursive_dependencies` - Get complete dependency tree
- `get_component_dependents` - Get components that depend on this one
- `get_recursive_dependents` - Get complete impact tree

### Discovery Tools  
- `get_components_by_type` - List components by type (COB, JCL, CPY, etc.)
- `find_component_by_path` - Find components by file path
- `get_orphaned_components` - Find unused components

### Source Code Tools
- `read_component_source` - Read actual source code content
- `get_component_source_info` - Get source file accessibility details
- `list_component_directory` - List files in component directories
- `validate_source_access` - Check source file accessibility

### System Analysis
- `get_dependency_statistics` - Get comprehensive codebase statistics
- `get_configuration_info` - Get current configuration status

### Management Tools
- `load_dependencies` - Load dependency data from JSON file
- `add_component` - Add new components
- `add_dependency` - Add new dependency relationships  
- `save_dependencies` - Save current state to JSON file

## MCP Server Configuration

```json
{
  "mcpServers": {
    "atx-mainframe-dependency-manager": {
      "command": "atx-mainframe-dependency-manager",
      "env": {
        "ATX_MF_DEPENDENCIES_FILE": "/path/to/dependencies.json",
        "ATX_MF_CODE_BASE": "/mainframe/source"
      }
    }
  }
}
```

## License

MIT License - see LICENSE file for details.
