# =====================================================
# SPRINT 2 - MODULE 05
# AI-BASED PRODUCT RECOMMENDATION SYSTEM
# Scoring Design using Python
# =====================================================
 
 
WEIGHTS = {
    "relevance": 0.50,
    "popularity": 0.30,
    "category_match": 0.20
}
 

 
FEATURE_CONTRACT = {
    "relevance": {
        "description": "How relevant the product is to the customer",
        "type": "float",
        "range": "0 to 100",
        "required": True
    },
 
    "popularity": {
        "description": "Popularity of the product",
        "type": "float",
        "range": "0 to 100",
        "required": False
    },
 
    "category_match": {
        "description": "How well the product matches the category",
        "type": "float",
        "range": "0 to 100",
        "required": True
    }
}
 
 

 
def normalize_score(value):
 
    if value is None:
        return None
 
    if isinstance(value, bool):
        raise ValueError("Boolean is not a valid score")
 
    if not isinstance(value, (int, float)):
        raise ValueError("Score must be numeric")
 
    if not 0 <= value <= 100:
        raise ValueError("Score must be between 0 and 100")
 
    return value / 100
 
 

 
def calculate_product_score(product):
 
    weighted_total = 0
    available_weight = 0
    normalized_features = {}
    warnings = []
 
    for feature, weight in WEIGHTS.items():
 
        value = product.get(feature)
 
        try:
            normalized_value = normalize_score(value)
 
        except ValueError as error:
 
            if FEATURE_CONTRACT[feature]["required"]:
                return {
                    "name": product["name"],
                    "score": None,
                    "status": "Rejected",
                    "reason": str(error)
                }
 
            warnings.append(f"{feature}: {error}")
            continue
 
    
 
        if normalized_value is None:
 
            if FEATURE_CONTRACT[feature]["required"]:
                return {
                    "name": product["name"],
                    "score": None,
                    "status": "Rejected",
                    "reason": f"Missing required feature: {feature}"
                }
 
            warnings.append(f"{feature} is missing")
            continue
 
        normalized_features[feature] = normalized_value
 
        weighted_total += normalized_value * weight
        available_weight += weight
 

 
    if available_weight == 0:
        return {
            "name": product["name"],
            "score": None,
            "status": "Rejected",
            "reason": "No usable features"
        }
 
 
    final_score = weighted_total / available_weight
 
    return {
        "name": product["name"],
        "score": round(final_score, 4),
        "status": "Success",
        "features": normalized_features,
        "warnings": warnings
    }
 
 
 
products = [
 
    {
        "name": "Samsung",
        "relevance": 90,
        "popularity": 80,
        "category_match": 100
    },
 
    {
        "name": "iPhone",
        "relevance": 85,
        "popularity": 95,
        "category_match": 90
    },
 
    {
        "name": "OnePlus",
        "relevance": 75,
        "popularity": 70,
        "category_match": 85
    },
 
    {
        "name": "Motorola",
        "relevance": 80,
        "popularity": None,
        "category_match": 90
    },
 
    {
        "name": "Nokia",
        "relevance": None,
        "popularity": 75,
        "category_match": 80
    }
]
 
 
 
results = []
 
for product in products:
 
    result = calculate_product_score(product)
 
    results.append(result)
 
 
 
print("\nPRODUCT SCORING RESULTS")
print("-" * 55)
 
for result in results:
 
    if result["status"] == "Success":
 
        print(
            result["name"],
            "Final Score:",
            result["score"]
        )
 
        if result["warnings"]:
            print("Warnings:", result["warnings"])
 
    else:
 
        print(
            result["name"],
            "Status:",
            result["status"],
            "Reason:",
            result["reason"]
        )
 
 
 
valid_products = [
    result for result in results
    if result["status"] == "Success"
]
 
ranked_products = sorted(
    valid_products,
    key=lambda item: (
        item["score"],
        item["features"]["relevance"],
        item["name"]
    ),
    reverse=True
)
 
print("\nFINAL PRODUCT RANKING")
print("-" * 55)
 
for position, product in enumerate(ranked_products, start=1):
 
    print(
        position,
        product["name"],
        "Score:",
        product["score"]
    )
 
print("\nSPRINT 2 SCORING COMPLETED")