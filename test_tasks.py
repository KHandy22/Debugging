import pytest
import ast
import sys
import importlib
from pathlib import Path


# Helper to check code wasn't deleted
def check_min_lines(filepath, min_lines=5):
    source = Path(filepath).read_text()
    lines = [l for l in source.split('\n') if l.strip() and not l.strip().startswith('#')]
    return len(lines) >= min_lines


def can_parse(filepath):
    """Check if file has valid Python syntax"""
    source = Path(filepath).read_text()
    try:
        ast.parse(source)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def import_module(module_name):
    """Dynamically import a module, reloading if already imported"""
    if module_name in sys.modules:
        return importlib.reload(sys.modules[module_name])
    return importlib.import_module(module_name)


# =============================================================================
# TASK 1: Code Errors (no input required)
# =============================================================================

class TestTask1:
    
    def test_file_not_empty(self):
        assert check_min_lines("task1.py", 20), "task1.py appears to have deleted code"
    
    def test_no_syntax_errors(self):
        valid, error = can_parse("task1.py")
        assert valid, f"task1.py has syntax errors: {error}"
    
    def test_snippet_1_greeting(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_1()
        output = capsys.readouterr().out
        assert "Alex" in output, "Should print the name Alex"
        assert "15" in output, "Should print age 15"
    
    def test_snippet_2_pizza(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_2()
        output = capsys.readouterr().out
        assert "24" in output, "Total slices should be 24"
        assert "3" in output, "Slices per person should be 3"
    
    def test_snippet_3_passing(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_3()
        output = capsys.readouterr().out
        assert "passed" in output.lower(), "Jordan scored 75, should pass"
        assert "Jordan" in output, "Should print student name"
    
    def test_snippet_4_tie_game(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_4()
        output = capsys.readouterr().out
        assert "tie" in output.lower(), "Both players scored 150, should be a tie"
    
    def test_snippet_5_weather(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_5()
        output = capsys.readouterr().out
        assert "72" in output, "Temperature should be 72"
        assert "sunny" in output.lower(), "Should say it's sunny"
    
    def test_snippet_6_book_total(self, capsys):
        valid, _ = can_parse("task1.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        task1 = import_module("task1")
        task1.snippet_6()
        output = capsys.readouterr().out
        assert "38.97" in output, "Total should be $38.97"


# =============================================================================
# TASK 2: Input Syntax Errors
# =============================================================================

class TestTask2:
    
    def test_file_not_empty(self):
        assert check_min_lines("task2.py", 15), "task2.py appears to have deleted code"
    
    def test_no_syntax_errors(self):
        valid, error = can_parse("task2.py")
        assert valid, f"task2.py has syntax errors: {error}"
    
    def test_program_1_greeting(self, monkeypatch, capsys):
        valid, _ = can_parse("task2.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        inputs = iter(["Alex", "great"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        task2 = import_module("task2")
        task2.program_1()
        output = capsys.readouterr().out
        assert "Alex" in output, "Should greet with name"
        assert "great" in output, "Should include feeling"
    
    def test_program_2_favorites(self, monkeypatch, capsys):
        valid, _ = can_parse("task2.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        inputs = iter(["blue", "pizza"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        task2 = import_module("task2")
        task2.program_2()
        output = capsys.readouterr().out
        assert "blue" in output, "Should show favorite color"
        assert "pizza" in output, "Should show favorite food"
    
    def test_program_3_scores(self, monkeypatch, capsys):
        valid, _ = can_parse("task2.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        inputs = iter(["85", "92"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        task2 = import_module("task2")
        task2.program_3()
        output = capsys.readouterr().out
        assert "92" in output and "higher" in output.lower(), "92 should be identified as higher"
    
    def test_program_4_birth_year(self, monkeypatch, capsys):
        valid, _ = can_parse("task2.py")
        if not valid:
            pytest.skip("Fix syntax errors first")
        inputs = iter(["Sam", "16"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        task2 = import_module("task2")
        task2.program_4()
        output = capsys.readouterr().out
        assert "Sam" in output, "Should greet with name"
        assert "2010" in output, "16 years old in 2026 means born in 2010"


# =============================================================================
# TASK 3: Data Conversion Errors
# =============================================================================

class TestTask3:
    
    def test_file_not_empty(self):
        assert check_min_lines("task3.py", 25), "task3.py appears to have deleted code"
    
    def test_no_syntax_errors(self):
        valid, error = can_parse("task3.py")
        assert valid, f"task3.py has syntax errors: {error}"
    
    def test_program_1_movie_tickets(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda prompt="": "4")
        from task3 import program_1
        program_1()
        output = capsys.readouterr().out
        assert "48" in output, "4 tickets at $12 = $48"
    
    def test_program_2_addition(self, monkeypatch, capsys):
        inputs = iter(["25", "17"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        from task3 import program_2
        program_2()
        output = capsys.readouterr().out
        assert "42" in output, "25 + 17 = 42, not 2517"
    
    def test_program_3_temperature(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda prompt="": "25")
        from task3 import program_3
        program_3()
        output = capsys.readouterr().out
        assert "77" in output, "25 Celsius = 77 Fahrenheit"
    
    def test_program_4_paycheck(self, monkeypatch, capsys):
        inputs = iter(["40", "15.50"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        from task3 import program_4
        program_4()
        output = capsys.readouterr().out
        assert "620" in output, "40 hours at $15.50 = $620"
    
    def test_program_5_rectangle_decimal(self, monkeypatch, capsys):
        inputs = iter(["8.5", "4"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        from task3 import program_5
        program_5()
        output = capsys.readouterr().out
        assert "34" in output, "8.5 x 4 = 34.0"
    
    def test_program_6_tip_calculator(self, monkeypatch, capsys):
        inputs = iter(["45.50", "20"])
        monkeypatch.setattr('builtins.input', lambda prompt="": next(inputs))
        from task3 import program_6
        program_6()
        output = capsys.readouterr().out
        assert "54.6" in output or "54.60" in output, "45.50 + 20% tip = 54.60"
