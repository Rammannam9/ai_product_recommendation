import unittest
 
from baseline_ranker import (
    RankerConfig,
    calculate_score,
    rank_products
)
 
 
class TestBaselineRanker(unittest.TestCase):
 
    def setUp(self):
 
        self.config = RankerConfig(
            weights={
                "relevance": 0.5,
                "popularity": 0.3,
                "price_match": 0.2
            },
            missing_policy="error"
        )
 
        self.products = [
            {
                "product_id": "P-101",
                "relevance": 0.9,
                "popularity": 0.8,
                "price_match": 0.8
            },
            {
                "product_id": "P-205",
                "relevance": 0.8,
                "popularity": 0.7,
                "price_match": 0.6
            },
            {
                "product_id": "P-310",
                "relevance": 0.7,
                "popularity": 0.8,
                "price_match": 0.65
            }
        ]
 
    
    def test_score_calculation(self):
 
        score = calculate_score(
            self.products[0],
            self.config
        )
 
        self.assertAlmostEqual(score, 0.85)
 
    
    def test_product_sorting(self):
 
        result = rank_products(
            self.products,
            self.config
        )
 
        self.assertEqual(
            result[0]["product_id"],
            "P-101"
        )
 
    
    def test_tie_breaking(self):
 
        products = [
            {
                "product_id": "P-310",
                "relevance": 0.8,
                "popularity": 0.8,
                "price_match": 0.8
            },
            {
                "product_id": "P-205",
                "relevance": 0.8,
                "popularity": 0.8,
                "price_match": 0.8
            }
        ]
 
        result = rank_products(
            products,
            self.config
        )
 
        self.assertEqual(
            result[0]["product_id"],
            "P-205"
        )
 
    
    def test_empty_list(self):
 
        result = rank_products(
            [],
            self.config
        )
 
        self.assertEqual(result, [])
 
   
    def test_missing_feature(self):
 
        product = {
            "product_id": "P-500",
            "relevance": 0.8
        }
 
        with self.assertRaises(ValueError):
            calculate_score(product, self.config)
 

    def test_invalid_feature(self):
 
        product = {
            "product_id": "P-500",
            "relevance": 1.5,
            "popularity": 0.8,
            "price_match": 0.7
        }
 
        with self.assertRaises(ValueError):
            calculate_score(product, self.config)
 
    def test_deterministic_results(self):
 
        result1 = rank_products(
            self.products,
            self.config
        )
 
        result2 = rank_products(
            self.products,
            self.config
        )
 
        self.assertEqual(result1, result2)
 
 
if __name__ == "__main__":
    unittest.main()