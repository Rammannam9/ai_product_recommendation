
products = [
    {
        "id": 101,
        "name": "Samsung Mobile",
        "category": "Electronics",
        "brand": "Samsung",
        "available": True,
        "blocked": False,
        "score": 95,
        "reason": "POPULAR",
        "reason_evidence": True
    },
    {
        "id": 102,
        "name": "Apple Mobile",
        "category": "Electronics",
        "brand": "Apple",
        "available": True,
        "blocked": False,
        "score": 90,
        "reason": "MATCHED_PREFERENCE",
        "reason_evidence": True
    },
    {
        "id": 103,
        "name": "Headphones",
        "category": "Accessories",
        "brand": "Sony",
        "available": False,
        "blocked": False,
        "score": 98,
        "reason": "POPULAR",
        "reason_evidence": True
    },
    {
        "id": 104,
        "name": "Smart Watch",
        "category": "Electronics",
        "brand": "Samsung",
        "available": True,
        "blocked": True,
        "score": 85,
        "reason": "POPULAR",
        "reason_evidence": True
    },
    {
        "id": 101,
        "name": "Samsung Mobile Duplicate",
        "category": "Electronics",
        "brand": "Samsung",
        "available": True,
        "blocked": False,
        "score": 80,
        "reason": "POPULAR",
        "reason_evidence": True
    }
]
 
 

def filter_products(products):
 
    eligible_products = []
    seen_ids = set()
 
    for product in products:
 
        if not product["available"]:
            print(product["name"], "- Unavailable")
            continue
 
        if product["blocked"]:
            print(product["name"], "- Blocked")
            continue
 
        if product["id"] in seen_ids:
            print(product["name"], "- Duplicate")
            continue
 
        seen_ids.add(product["id"])
        eligible_products.append(product)
 
    return eligible_products
 
 

 
def rank_products(products):
 
    ranked_products = sorted(
        products,
        key=lambda p: (-p["score"], p["id"])
    )
 
    return ranked_products
 
 

def validate_reason(product):
 
    allowed_reasons = [
        "POPULAR",
        "MATCHED_PREFERENCE"
    ]
 
    if (product["reason"] in allowed_reasons
            and product["reason_evidence"]):
        return product["reason"]
 
    return None
 

def recommend_products(products, limit=5):
 
    eligible = filter_products(products)
 
    ranked = rank_products(eligible)
 
    results = []
 
    for product in ranked[:limit]:
 
        results.append({
            "id": product["id"],
            "name": product["name"],
            "score": product["score"],
            "reason": validate_reason(product)
        })
 
    return results
 
 

print("\nFINAL RECOMMENDATIONS")
 
result = recommend_products(products)
 
for item in result:
    print(item)
 
 

print("\nDETERMINISTIC TEST")
 
first_result = recommend_products(products)
second_result = recommend_products(products)
 
if first_result == second_result:
    print("PASS: Same input produces same ranking")
else:
    print("FAIL: Ranking is different")
 
 

print("\nACCEPTANCE CRITERIA")
 

assert all(p["available"] for p in filter_products(products))
print("PASS: Unavailable products excluded")

assert all(not p["blocked"] for p in filter_products(products))
print("PASS: Blocked products excluded")
 

filtered = filter_products(products)
ids = [p["id"] for p in filtered]
 
assert len(ids) == len(set(ids))
print("PASS: Duplicate products excluded")
 

ranked = rank_products(filtered)
 
scores = [p["score"] for p in ranked]
 
assert scores == sorted(scores, reverse=True)
print("PASS: Products ranked by score")
 

test_product = {
    "reason": "UNSUPPORTED_REASON",
    "reason_evidence": False
}
 
assert validate_reason(test_product) is None
print("PASS: Unsupported reason code excluded")
 
print("\nALL TESTS COMPLETED")