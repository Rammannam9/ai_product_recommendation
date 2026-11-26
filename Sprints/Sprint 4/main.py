 
from eligibility_filter import filter_eligible_products
from ranker import rank_products
 
 

products = [
 
    {
        "product_id": "P-101",
        "name": "Laptop",
        "active": True,
        "available": True,
        "blocked": False,
        "score": 0.86
    },
 
    {
        "product_id": "P-205",
        "name": "Mobile",
        "active": False,
        "available": True,
        "blocked": False,
        "score": 0.99
    },
 
    {
        "product_id": "P-310",
        "name": "Headphones",
        "active": True,
        "available": False,
        "blocked": False,
        "score": 0.90
    },
 
    {
        "product_id": "P-415",
        "name": "Smart Watch",
        "active": True,
        "available": True,
        "blocked": True,
        "score": 0.75
    },
 
    {
        "product_id": "P-101",
        "name": "Laptop Duplicate",
        "active": True,
        "available": True,
        "blocked": False,
        "score": 0.86
    },
 
    {
        "product_id": "P-520",
        "name": "Keyboard",
        "active": True,
        "available": True,
        "blocked": False,
        "score": 0.95
    }
]
 
 

eligible_products = filter_eligible_products(products)
 
 

final_recommendations = rank_products(eligible_products)
 
 

print("\nFINAL PRODUCT RECOMMENDATIONS")
 
for product in final_recommendations:
 
    print("--------------------------")
 
    print("Product ID:", product["product_id"])
    print("Product Name:", product["name"])
    print("Recommendation Score:", product["score"])
 