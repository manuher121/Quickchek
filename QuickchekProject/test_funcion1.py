import unittest
import funcion1 as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Orders.orders = [
            db.Sandwich('White','Toasted','Ham','Yellow','Lettuce','Mayo','Salt',False,'1',"False",'1'),
            db.Sandwich('Wheat','Toasted','Ham','Yellow','Lettuce','Mayo','Salt',False,'1',"False",'1'),
            db.Sandwich('Italian','Toasted','Ham','Yellow','Lettuce','Mayo','Salt',False,'1',"False",'1')
        ]

    def test_retrieve(self):
        order_retrieved = db.Orders.retrieve_order("False")
        order_nonexistant = db.Orders.retrieve_order("True")
        self.assertIsNotNone(order_retrieved)
        print(order_nonexistant)