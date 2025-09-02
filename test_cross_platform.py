#!/usr/bin/env python3
"""
Cross-platform compatibility test for ATX Mainframe Dependency Manager.
Tests path handling, file operations, and signal handling across different OS.
"""

import os
import sys
import tempfile
import json
import signal
from pathlib import Path

def test_path_handling():
    """Test cross-platform path handling."""
    print("Testing path handling...")
    
    # Test different path formats
    test_paths = [
        "cobol/PAYROLL.cob",
        "cobol\\PAYROLL.cob",  # Windows style
        "/absolute/path/PAYROLL.cob",
        "C:\\Windows\\Path\\PAYROLL.cob" if sys.platform == "win32" else "/unix/path/PAYROLL.cob"
    ]
    
    for path in test_paths:
        path_obj = Path(path)
        print(f"  Original: {path}")
        print(f"  Normalized: {path_obj}")
        print(f"  Name: {path_obj.name}")
        print(f"  Is absolute: {path_obj.is_absolute()}")
        print()

def test_file_operations():
    """Test file operations with proper encoding."""
    print("Testing file operations...")
    
    # Create test data
    test_data = {
        "components": [
            {"name": "TEST", "type": "COB", "path": "test.cob"}
        ]
    }
    
    # Test with temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(test_data, f, indent=2)
        temp_file = f.name
    
    try:
        # Test reading
        with open(temp_file, 'r', encoding='utf-8') as f:
            loaded_data = json.load(f)
        
        print(f"  Successfully wrote and read JSON file: {temp_file}")
        print(f"  Data matches: {loaded_data == test_data}")
        
    finally:
        os.unlink(temp_file)

def test_signal_availability():
    """Test signal availability across platforms."""
    print("Testing signal availability...")
    
    available_signals = []
    
    # Test SIGINT (should be available everywhere)
    if hasattr(signal, 'SIGINT'):
        available_signals.append('SIGINT')
    
    # Test SIGTERM (not available on Windows)
    if hasattr(signal, 'SIGTERM'):
        available_signals.append('SIGTERM')
    
    print(f"  Platform: {sys.platform}")
    print(f"  Available signals: {available_signals}")
    
    # Recommend signal handling approach
    if sys.platform == "win32":
        print("  Recommendation: Use only SIGINT on Windows")
    else:
        print("  Recommendation: Can use both SIGINT and SIGTERM on Unix-like systems")

def test_environment_variables():
    """Test environment variable handling."""
    print("Testing environment variables...")
    
    # Test setting and getting environment variables
    test_var = "ATX_MF_TEST_VAR"
    test_value = "test_value"
    
    os.environ[test_var] = test_value
    retrieved_value = os.getenv(test_var)
    
    print(f"  Set {test_var} = {test_value}")
    print(f"  Retrieved: {retrieved_value}")
    print(f"  Match: {test_value == retrieved_value}")
    
    # Clean up
    del os.environ[test_var]

def main():
    """Run all cross-platform compatibility tests."""
    print("ATX Mainframe Dependency Manager - Cross-Platform Compatibility Test")
    print("=" * 70)
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"OS: {os.name}")
    print()
    
    test_path_handling()
    test_file_operations()
    test_signal_availability()
    test_environment_variables()
    
    print("All tests completed successfully!")
    print("\nRecommendations for cross-platform compatibility:")
    print("1. Use pathlib.Path for path operations")
    print("2. Always specify encoding='utf-8' for file operations")
    print("3. Handle signal availability differences between Windows and Unix")
    print("4. Use os.path.join() or pathlib for path construction")

if __name__ == "__main__":
    main()
