def filter_eligible_products(products):
    """
    Remove inactive, unavailable, blocked
    and duplicate products.
 
    Duplicate policy for this example:
    Keep the first eligible occurrence.
    """
 
    eligible_products = []
    seen_product_ids = set()
 
    for product in products:
 
        # Validate required fields
        required_fields = [
            "product_id",
            "active",
            "available",
            "blocked",
            "score"
        ]
 
        for field in required_fields:
            if field not in product:
                raise ValueError(
                    f"Missing required field: {field}"
                )
 
        # Rule 1: Remove inactive products
        if product["active"] is not True:
            continue
 
        # Rule 2: Remove unavailable products
        if product["available"] is not True:
            continue
 
        # Rule 3: Remove blocked products
        if product["blocked"] is True:
            continue
 
        # Rule 4: Remove duplicate products
        product_id = product["product_id"]
 
        if product_id in seen_product_ids:
            continue
 
        seen_product_ids.add(product_id)
 
        # Product passed all eligibility checks
        eligible_products.append(product)
 
    return eligible_products
 