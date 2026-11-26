import unittest
 
from eligibility_filter import filter_eligible_products
 
 
class TestEligibilityFilter(unittest.TestCase):
 
    def setUp(self):
 
        self.valid_product = {
            "product_id": "P-101",
            "name": "Laptop",
            "active": True,
            "available": True,
            "blocked": False,
            "score": 0.86
        }
 
    
    def test_inactive_product(self):
 
        product = self.valid_product.copy()
        product["active"] = False
 
        result = filter_eligible_products([product])
 
        self.assertEqual(result, [])
 
   
    def test_unavailable_product(self):
 
        product = self.valid_product.copy()
        product["available"] = False
 
        result = filter_eligible_products([product])
 
        self.assertEqual(result, [])
 
    
    def test_blocked_product(self):
 
        product = self.valid_product.copy()
        product["blocked"] = True
 
        result = filter_eligible_products([product])
 
        self.assertEqual(result, [])
 
    
    def test_duplicate_products(self):
 
        products = [
            self.valid_product,
            self.valid_product.copy()
        ]
 
        result = filter_eligible_products(products)
 
        self.assertEqual(len(result), 1)
 
    # Test 5: High score but inactive
    def test_high_score_inactive_product(self):
 
        product = self.valid_product.copy()
        product["active"] = False
        product["score"] = 0.99
 
        result = filter_eligible_products([product])
 
        self.assertEqual(result, [])
 
    
    def test_empty_input(self):
 
        result = filter_eligible_products([])
 
        self.assertEqual(result, [])
 
    
    def test_all_ineligible(self):
 
        products = []
 
        for field, value in [
            ("active", False),
            ("available", False),
            ("blocked", True)
        ]:
            product = self.valid_product.copy()
            product[field] = value
            products.append(product)
 
        result = filter_eligible_products(products)
 
        self.assertEqual(result, [])
 
    
    def test_eligible_product(self):
 
        result = filter_eligible_products(
            [self.valid_product]
        )
 
        self.assertEqual(len(result), 1)
        self.assertEqual(
            result[0]["product_id"], "P-101"
        )
 
 
if __name__ == "__main__":
    unittest.main()