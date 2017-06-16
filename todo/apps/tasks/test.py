from django.test import TestCase

from todo.apps.tasks.models import Task

class ModelTaskTest(TestCase):
    def setUp(self):
        Task.objects.create(
            name="Tarefa 1",
            status="A",
            order=5)
        Task.objects.create(
            name="Tarefa 2",
            status="E",
            order=3)
        Task.objects.create(
            name="Tarefa 3",
            status="E",
            order=2)

    def test_object_is_todo(self):
        task = Task.objects.filter(status='A')
        self.assertEqual(task.count(), 1)
        self.assertEqual(task[0].status, 'A')

    def test_order_tasks(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks[0].order, 2)
        self.assertEqual(tasks[1].order, 3)
        self.assertEqual(tasks[2].order, 5)

    def test_reorder_tasks_doing(self):
        tasks = Task.objects.filter(status='E')
        self.assertEqual(tasks[0].order, 2)
        for i, task in enumerate(tasks):
            task.order = i

        self.assertEqual(tasks[0].order, 0)
        self.assertEqual(tasks[1].order, 1)

    def test_save_task(self):
        task = Task.objects.create(
            name="Nova Tarefa",
            status="A",
            order=1)
        task.save()
