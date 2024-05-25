import pulp

# Створення проблеми максимізації
problem = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Змінні для кількості виробленого лимонаду та фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Обмеження на ресурси
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Обмеження на виробництво
# Вода: 2 од. на одиницю лимонаду + 1 од. на одиницю фруктового соку <= 100 од.
problem += 2 * lemonade + 1 * fruit_juice <= water_limit, "WaterLimit"

# Цукор: 1 од. на одиницю лимонаду <= 50 од.
problem += 1 * lemonade <= sugar_limit, "SugarLimit"

# Лимонний сік: 1 од. на одиницю лимонаду <= 30 од.
problem += 1 * lemonade <= lemon_juice_limit, "LemonJuiceLimit"

# Фруктове пюре: 2 од. на одиницю фруктового соку <= 40 од.
problem += 2 * fruit_juice <= fruit_puree_limit, "FruitPureeLimit"

# Цільова функція: максимізація кількості вироблених напоїв
problem += lemonade + fruit_juice, "TotalProduction"

# Розв'язання проблеми
problem.solve()

# Результати
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Total Production: {pulp.value(problem.objective)}")
