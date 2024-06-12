import unittest
from unittest.mock import patch
from task import Task, make_task, task_list

class TestTaskModule(unittest.TestCase):
    """Unit test class for the task module."""

    def setUp(self):
        """Set up the test environment by clearing the existing tasks list."""
        task_list.existing_tasks = []

    @patch('task.input', side_effect=['Test Task', 'yes', 'yes', '2024-05-20'])
    def test_make_task(self, mock_input):
        """Test creating a task and adding it to the task list."""
        make_task()
        self.assertEqual(len(task_list.existing_tasks), 1)
        self.assertEqual(task_list.existing_tasks[0].title, 'Test Task')
        self.assertEqual(task_list.existing_tasks[0].complete, False)

    @patch('task.input', side_effect=['Test Task', 'Test Task'])
    def test_delete_task(self, mock_input):
        """Test deleting a task from the task list."""
        task = Task('Test Task', '2024-05-20', '10:00', False, '2024-05-21')
        task_list.existing_tasks.append(task)
        Task.delete_task()
        self.assertEqual(len(task_list.existing_tasks), 0)

    @patch('task.input', side_effect=['Test Task', 'Test Task'])
    def test_task_complete(self, mock_input):
        """Test marking a task as complete in the task list."""
        task = Task('Test Task', '2024-05-20', '10:00', False, '2024-05-21')
        task_list.existing_tasks.append(task)
        Task.task_complete()
        self.assertTrue(task_list.existing_tasks[0].complete)


if __name__ == '__main__':
    unittest.main()
