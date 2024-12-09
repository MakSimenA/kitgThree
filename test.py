import unittest
from mine import dijkstra
class TestDijkstra(unittest.TestCase):

    def test_dijkstra_empty_graph(self):
        # Тестируем пустой граф
        empty_graph = {}
        expected_distances = {}
        result = dijkstra(empty_graph, 'A')  # Стартовая вершина не имеет значения в пустом графе
        self.assertEqual(result, expected_distances)

    def setUp(self):
        # Создаем граф для тестирования
        self.graph1 = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

        self.graph2 = {
            'A': {'B': 2},
            'B': {'A': 2, 'C': 3},
            'C': {'B': 3, 'D': 1},
            'D': {'C': 1}
        }

    def test_dijkstra_graph1(self):
        # Тестируем первый граф
        expected_distances = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 4
        }
        result = dijkstra(self.graph1, 'A')
        self.assertEqual(result, expected_distances)

    def test_dijkstra_graph2(self):
        # Тестируем второй граф
        expected_distances = {
            'A': 0,
            'B': 2,
            'C': 5,
            'D': 6
        }
        result = dijkstra(self.graph2, 'A')
        self.assertEqual(result, expected_distances)

    def test_dijkstra_empty_graph(self):
        # Тестируем пустой граф
        empty_graph = {}
        expected_distances = {}
        result = dijkstra(empty_graph, 'A')  # Стартовая вершина не имеет значения в пустом графе
        self.assertEqual(result, expected_distances)