import unittest
from Model.Room import Room

class MyTestCase(unittest.TestCase):
    def test_room_constructor_all_walls_no_monster_no_potion(self):
        room = Room(True,True,True,True,(3,4),None,None)
        self.assertEqual(room.get_ewall(),True)
        self.assertEqual(room.get_wwall(),True)
        self.assertEqual(room.get_nwall(),True)
        self.assertEqual(room.get_swall(),True)
        self.assertEqual(room.location,(3,4))
        self.assertEqual(room.potion,None)
        self.assertEqual(room.monster,None)

    def test_room_constructor_monster_and_potion(self):
        room = Room(False, False, False, False, (3, 2), True, True)
        self.assertEqual(room.monster,True)
        self.assertEqual(room.potion,True)

    def test_room_no_walls(self):
        room = Room(False,False,False,False,(3,2),None,None)
        self.assertEqual(room.get_ewall(), False)  # add assertion here
        self.assertEqual(room.get_wwall(), False)
        self.assertEqual(room.get_nwall(), False)
        self.assertEqual(room.get_swall(), False)

    def test_visited_false(self):
        room = Room(False,False,False,False,(3,2),None,None)
        self.assertEqual(room.get_has_visited(), False)  # add assertion here

    def test_visited_true(self):
        room = Room(False,False,False,False,(3,2),None,None)
        room.set_has_visited(True)
        self.assertEqual(room.get_has_visited(), True)  # add assertion here

    def test_hero_has_visited(self):
        room = Room(False,False,False,False,(3,2),None,None)
        room.set_hero_has_visited(True)
        self.assertEqual(room.get_hero_has_visited(), True)  # add assertion here

    def test_hero_hasnt_visited(self):
        room = Room(False,False,False,False,(3,2),None,None)
        room.set_has_visited(False)
        self.assertEqual(room.get_hero_has_visited(), False)  # add assertion here

    def test_has_exit_true(self):
        room = Room(False,False,False,False,(3,2),None,None)
        room.set_has_exit(True)
        self.assertEqual(room.has_exit, True)  # add assertion here

    def test_has_exit_false(self):
        room = Room(False,False,False,False,(3,2),None,None)
        room.set_has_exit(False)
        self.assertEqual(room.has_exit, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
