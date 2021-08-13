price = [10, 15, 14, 30, 50]
product = ["apple", "orange", "bananna", "berry", "melon"]
mart = {"product":product,
        "price":price}


res = "\n".join("{} {}".format(x, y) for x, y in zip(product, price))
print(res)
