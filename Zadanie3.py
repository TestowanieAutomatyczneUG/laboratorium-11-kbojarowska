import unittest
from unittest.mock import MagicMock

class FriendShips:
    def __init__(self):
        self.friendships = {}
    
    def addFriend(self, person, friend):
        if person not in self.friendships.keys():
            self.friendships[person] = [friend]
        else:
            self.friendships[person].append(friend)

    def makeFriends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise Exception('Person must be str')
        elif person1 in self.friendships.keys() and person2 in self.friendships[person1]:
            raise Exception('They are already friends')
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)
        return self.friendships

    def getFriendsList(self, person):
        if type(person) is not str:
            raise Exception('Person must be str')
        elif person not in self.friendships.keys():
            raise Exception('No given person')
        return self.friendships[person]

    def areFriends(self, person1, person2):
        if type(person1) is not str or type(person2) is not str:
            raise Exception("Person must be str")
        elif person1 in self.friendships[person2] and person2 in self.friendships[person1]:
            return True
        return False

class FriendShipsClass:
    def __init__(self):
        self.database = FriendShips()

    def makeFriends(self, person1, person2):
        self.database.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.database.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.database.areFriends(person1, person2)
    
class TestFriendShips(unittest.TestCase):

    def setUp(self):
        self.temp = FriendShips()
        self.temp.friendships = {
            "Miotk" : ["Kowalski", "Nowak", "Bobkowska"],
            "Kowalski": ["Miotk"],
            "Nowak": ["Miotk"],
            "Bobkowska": ["Miotk"],
            "Kowalska": []
        }

    def test_add_friend_new_person(self):
        self.temp.addFriend("Bobkowski", "Wiśniewski")
        self.assertEqual(self.temp.friendships["Bobkowski"], ["Wiśniewski"])

    def test_add_friend_existing_person(self):
        self.temp.addFriend("Kowalski", "Wiśniewski")
        self.assertEqual(self.temp.friendships["Kowalski"], ["Miotk", "Wiśniewski"])

    def test_make_friends(self):
        self.temp.makeFriends('Bobkowski', 'Wiśniewski')
        self.assertEqual(self.temp.friendships,{
            "Miotk" : ["Kowalski", "Nowak", "Bobkowska"],
            "Kowalski": ["Miotk"],
            "Nowak": ["Miotk"],
            "Bobkowska": ["Miotk"],
            "Kowalska": [],
            "Bobkowski": ["Wiśniewski"],
            "Wiśniewski": ["Bobkowski"]
        })

    def test_make_friends_person2_not_str_int(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends("Bobkowski", 123)

    def test_make_friends_person1_not_str_int(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends(123, "Bobkowski")

    def test_make_friends_person2_not_str_list(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends("Bobkowski", [])

    def test_make_friends_person1_not_str_list(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends([], "Bobkowski")

    def test_make_friends_person2_not_str_dict(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends("Bobkowski", {})

    def test_make_friends_person1_not_str_dict(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.makeFriends({}, "Bobkowski")

    def test_make_friends_already_are_friends(self):
        with self.assertRaisesRegex(Exception, 'They are already friends'):
            self.temp.makeFriends("Miotk", "Nowak")

    def test_get_friends_list(self):
        self.assertEqual(self.temp.getFriendsList("Nowak"), ["Miotk"])

    def test_get_friends_list_person_not_str_int(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.getFriendsList(4)

    def test_get_friends_list_person_not_str_list(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.getFriendsList([])

    def test_get_friends_list_person_not_str_dict(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.getFriendsList({})
        
    def test_get_friends_list_non_existing_person(self):
        with self.assertRaisesRegex(Exception, 'No given person'):
            self.temp.getFriendsList("Friend")

    def test_are_friends_true(self):
        self.assertTrue(self.temp.areFriends("Miotk", "Bobkowska"))

    def test_are_friends_false(self):
        self.assertFalse(self.temp.areFriends("Miotk", "Kowalska"))

    def test_are_friends_person2_not_str_int(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends("Bobkowski", 123)

    def test_are_friends_person1_not_str_int(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends(123, "Bobkowski")

    def test_are_friends_person2_not_str_list(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends("Bobkowski", [])

    def test_are_friends_person1_not_str_list(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends([], "Bobkowski")

    def test_are_friends_person2_not_str_dict(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends("Bobkowski", {})

    def test_are_friends_person1_not_str_dict(self):
        with self.assertRaisesRegex(Exception, 'Person must be str'):
            self.temp.areFriends({}, "Bobkowski")

    
class TestFriendShipsClass(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShipsClass()

    def test_friendships_class_make_friends(self):
        self.temp.database = MagicMock()
        self.temp.makeFriends("Bobkowski", "Wiśniewski")
        self.temp.database.makeFriends.assert_called_with("Bobkowski", "Wiśniewski")

    def test_friendships_class_make_friends_friend2_not_str_int(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends("Bobkowski", 123)
        self.temp.database.makeFriends.assert_called_with("Bobkowski", 123)

    def test_friendships_class_make_friends_friend1_not_str_int(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends(123, "Bobkowski")
        self.temp.database.makeFriends.assert_called_with(123, "Bobkowski")

    def test_friendships_class_make_friends_friend2_not_str_list(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends("Bobkowski", [])
        self.temp.database.makeFriends.assert_called_with("Bobkowski", [])

    def test_friendships_class_make_friends_friend1_not_str_list(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends([], "Bobkowski")
        self.temp.database.makeFriends.assert_called_with([], "Bobkowski")

    def test_friendships_class_make_friends_friend2_not_str_dict(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends("Bobkowski", {})
        self.temp.database.makeFriends.assert_called_with("Bobkowski", {})

    def test_friendships_class_make_friends_friend1_not_str_dict(self):
        self.temp.database.makeFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.makeFriends({}, "Bobkowski")
        self.temp.database.makeFriends.assert_called_with({}, "Bobkowski")

    def test_friendships_class_get_friends_list(self):
        self.temp.database.getFriendsList = MagicMock(return_value=["Miotk"])
        self.assertEqual(self.temp.getFriendsList("Nowak"), ["Miotk"])
        self.temp.database.getFriendsList.assert_called_with("Nowak")

    def test_friendships_class_get_friends_list_person_not_str_int(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.getFriendsList(5)
        self.temp.database.getFriendsList.assert_called_with(5)

    def test_friendships_class_get_friends_list_person_not_str_list(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.getFriendsList([])
        self.temp.database.getFriendsList.assert_called_with([])

    def test_friendships_class_get_friends_list_person_not_str_dict(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.getFriendsList({})
        self.temp.database.getFriendsList.assert_called_with({})

    def test_friendships_class_get_friends_list_non_existing_person(self):
        self.temp.database.getFriendsList = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.getFriendsList("Friend")
        self.temp.database.getFriendsList.assert_called_with("Friend")

    def test_friendships_class_are_friends_true(self):
        self.temp.database.areFriends = MagicMock(return_value=True)
        self.assertTrue(self.temp.areFriends("Miotk", "Nowak"))
        self.temp.database.areFriends.assert_called_with("Miotk", "Nowak")

    def test_friendships_class_are_friends_false(self):
        self.temp.database.areFriends = MagicMock(return_value=False)
        self.assertFalse(self.temp.areFriends("Miotk", "Kowalska"))
        self.temp.database.areFriends.assert_called_with("Miotk", "Kowalska")

    def test_friendships_class_are_friends_friend1_not_str_int(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends(4, "Nowak")
        self.temp.database.areFriends.assert_called_with(4, "Nowak")

    def test_friendships_class_are_friends_friend2_not_str_int(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends("Nowak", 4)
        self.temp.database.areFriends.assert_called_with("Nowak", 4)

    def test_friendships_class_are_friends_friend1_not_str_list(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends([], "Nowak")
        self.temp.database.areFriends.assert_called_with([], "Nowak")

    def test_friendships_class_are_friends_friend2_not_str_list(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends("Nowak", [])
        self.temp.database.areFriends.assert_called_with("Nowak", [])

    def test_friendships_class_are_friends_friend1_not_str_dict(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends({}, "Nowak")
        self.temp.database.areFriends.assert_called_with({}, "Nowak")

    def test_friendships_class_are_friends_friend2_not_str_dict(self):
        self.temp.database.areFriends = MagicMock(side_effect=Exception)
        with self.assertRaises(Exception):
            self.temp.areFriends("Nowak", {})
        self.temp.database.areFriends.assert_called_with("Nowak", {})

    def tearDown(self):
        self.temp = None