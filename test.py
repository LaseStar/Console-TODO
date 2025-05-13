from fileinput import filename

import pytest
from TODO import load_tasks, save_tasks
import os

@pytest.fixture
def sample_tasks():
    return [{"task": "Test", "done": False, "category": "Work", "deadline": None}]

def tesst_save_tasks(sample_tasks, tmp_path):
    test_file = tmp_path / "test_task.json"
    save_tasks(sample_tasks, filename=test_file)
    loaded =load_tasks(filename=test_file)
    assert loaded == sample_tasks

def test_add_task(sample_tasks):
    pass