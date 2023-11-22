# Curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Contoh penggunaan dengan Higher-Order Function (HOF)
def HOF():
    multiplier = perkalian(5)
    result = multiplier(3)
    print(result)

HOF()

# Contoh penggunaan dengan Currying
def currying():
    result = perkalian(5)(3)
    print(result)

currying()
