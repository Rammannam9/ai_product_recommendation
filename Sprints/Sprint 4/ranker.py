def rank_products(products):
 
    
    ranked_products = sorted(
        products,
        key=lambda product: product["score"],
        reverse=True
    )
 
    return ranked_products