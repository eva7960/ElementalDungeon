import unittest
from Model.Maze import Maze
from Model.Room import Room
from Model.Potion import HealthPotion, VisionPotion


class TestMaze(unittest.TestCase):
    def setUp(self):
        Maze.delete_instance()  # Ensure fresh singleton instance for each test
        self.maze_size = 3
        self.maze = Maze(self.maze_size)

    def tearDown(self):
        Maze.delete_instance()  # Clean up singleton instance

    def test_singleton_enforcement(self):
        with self.assertRaises(Exception) as context:
            Maze(self.maze_size)
        self.assertEqual(str(context.exception), "Dungeon already exists!")

    def test_get_instance(self):
        self.assertEqual(Maze.get_instance(), self.maze)

    def test_delete_instance(self):
        Maze.delete_instance()
        self.assertIsNone(Maze.get_instance())

    def test_maze_size_and_initialization(self):
        self.assertEqual(len(self.maze.get_array()), self.maze_size)
        for row in self.maze.get_array():
            self.assertEqual(len(row), self.maze_size)
            for room in row:
                self.assertIsInstance(room, Room)


    def test_set_and_get_array(self):
        custom_array = [[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)]
        self.maze.set_array(custom_array)
        self.assertEqual(self.maze.get_array(), custom_array)

    def test_check_neighbor_none(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                self.maze.room_array[i][j].set_has_visited(True)
        self.assertIsNone(self.maze.check_neighbors(self.maze.room_array[0][1]))

    def test_check_neighbor(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        neighbors = [self.maze.room_array[0][1], self.maze.room_array[0][1], self.maze.room_array[1][2], self.maze.room_array[2][1]]
        self.assertIn(self.maze.check_neighbors(self.maze.room_array[1][1]), neighbors)

    def test_remove_west_wall(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.remove_walls(self.maze.room_array[1][1], self.maze.room_array[0][1])
        self.assertEqual(self.maze.room_array[1][1].get_wwall(), False)
        self.assertEqual(self.maze.room_array[0][1].get_ewall(), False)

    def test_remove_east_wall(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.remove_walls(self.maze.room_array[1][1], self.maze.room_array[2][1])
        self.assertEqual(self.maze.room_array[1][1].get_ewall(), False)
        self.assertEqual(self.maze.room_array[2][1].get_wwall(), False)

    def test_remove_north_wall(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.remove_walls(self.maze.room_array[1][1], self.maze.room_array[1][0])
        self.assertEqual(self.maze.room_array[1][1].get_nwall(), False)
        self.assertEqual(self.maze.room_array[1][0].get_swall(), False)

    def test_remove_south_wall(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.remove_walls(self.maze.room_array[1][1], self.maze.room_array[1][2])
        self.assertEqual(self.maze.room_array[1][1].get_swall(), False)
        self.assertEqual(self.maze.room_array[1][2].get_nwall(), False)

    def test_generate_maze(self):
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            location = room.get_location()
            col, row = location
            if not room.get_nwall() and row > 0:  # North wall is open
                dfs(self.maze.get_array()[col][row - 1])
            if not room.get_swall() and row < self.maze_size - 1:  # South wall is open
                dfs(self.maze.get_array()[col][row + 1])
            if not room.get_wwall() and col > 0:  # West wall is open
                dfs(self.maze.get_array()[col - 1][row])
            if not room.get_ewall() and col < self.maze_size - 1:  # East wall is open
                dfs(self.maze.get_array()[col + 1][row])

        start_room = self.maze.get_array()[0][0]
        dfs(start_room)

        total_rooms = self.maze_size * self.maze_size
        self.assertEqual(len(visited), total_rooms)


    def test_exit(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.add_exit()
        exit_flag = False
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                if self.maze.room_array[i][j].has_exit:
                    exit_flag = True
                    break
        self.assertTrue(exit_flag)

    def test_add_monster(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.add_monsters()
        monster_flag = False
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                if not self.maze.room_array[i][j].get_monster() is None:
                    monster_flag = True
                    break
        self.assertTrue(monster_flag)

    def test_add_health_potions(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.add_health_potions()
        potion_flag = False
        potion = None
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                if not self.maze.room_array[i][j].potion is None:
                    potion_flag = True
                    potion = self.maze.room_array[i][j].potion
                    break
        self.assertTrue(potion_flag)
        self.assertIsInstance(potion, HealthPotion)

    def test_add_vision_potions(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.add_vision_potions()
        potion_flag = False
        potion = None
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                if not self.maze.room_array[i][j].potion is None:
                    potion_flag = True
                    potion = self.maze.room_array[i][j].potion
                    break
        self.assertTrue(potion_flag)
        self.assertIsInstance(potion, VisionPotion)


if __name__ == "__main__":
    unittest.main()
