
 
from dataclasses import dataclass 
 
@dataclass
class RankerConfig:
   
    weights: dict
 
   
    missing_policy: str = "error"
 
 
def validate_config(config):
    if not config.weights:
        raise ValueError("Weights cannot be empty")
 
    if config.missing_policy not in ("error", "zero", "ignore"):
        raise ValueError("Invalid missing feature policy")
 
    for feature, weight in config.weights.items():
        if not isinstance(weight, (int, float)):
            raise ValueError(f"Invalid weight for {feature}")
 
        if weight < 0:
            raise ValueError("Weights cannot be negative")
 
    if sum(config.weights.values()) <= 0:
        raise ValueError("Total weight must be positive")
 
 
def validate_candidates(candidates):
    if not isinstance(candidates, list):
        raise TypeError("Candidates must be a list")
 
    seen_ids = set()
 
    for product in candidates:
        if not isinstance(product, dict):
            raise TypeError("Each candidate must be a dictionary")
 
        product_id = product.get("product_id")
 
        if not isinstance(product_id, str) or not product_id:
            raise ValueError("Valid product_id is required")
 
        if product_id in seen_ids:
            raise ValueError("Duplicate product ID")
 
        seen_ids.add(product_id)
 
 
def calculate_score(product, config):
 
    total_score = 0
    used_weight = 0
 
    for feature, weight in config.weights.items():
 
        value = product.get(feature)
 
        # Handle missing or null features
        if value is None:
 
            if config.missing_policy == "error":
                raise ValueError(
                    f"Missing feature: {feature}"
                )
 
            elif config.missing_policy == "zero":
                used_weight += weight
                continue
 
            elif config.missing_policy == "ignore":
                continue
 
       
        if not isinstance(value, (int, float)):
            raise ValueError(
                f"Invalid value for {feature}"
            )
 
        if not 0 <= value <= 1:
            raise ValueError(
                f"{feature} must be between 0 and 1"
            )
 
        total_score += value * weight
        used_weight += weight
 
    if used_weight == 0:
        raise ValueError("No usable features available")
 
    return total_score / used_weight
 
 
def rank_products(candidates, config):
 
    validate_config(config)
    validate_candidates(candidates)
 
    ranked_products = []
 
    for product in candidates:
 
        score = calculate_score(product, config)
 
        result = product.copy()
        result["final_score"] = round(score, 4)
 
        ranked_products.append(result)
 
    
    ranked_products.sort(
        key=lambda product: (
            -product["final_score"],
            product["product_id"]
        )
    )
 
    return ranked_products
 
 

if __name__ == "__main__":
 
    products = [
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
        },
        {
            "product_id": "P-415",
            "relevance": 0.5,
            "popularity": 0.5,
            "price_match": 0.55
        }
    ]
 
    config = RankerConfig(
        weights={
            "relevance": 0.5,
            "popularity": 0.3,
            "price_match": 0.2
        },
        missing_policy="error"
    )
 
    result = rank_products(products, config)
 
    print("\nPRODUCT RECOMMENDATION RANKING")
    print("--------------------------------")
 
    for position, product in enumerate(result, start=1):
 
        print(
            f"Rank: {position} | "
            f"Product: {product['product_id']} | "
            f"Score: {product['final_score']}"
        )