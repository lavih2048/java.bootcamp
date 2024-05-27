# conjunto

set([1,2,3,1,3,4]) # {1,2,3,4}    obs: não garante a ordem dos elementos

# .intersection

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # 2, 3


# .difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # 1
conjunto_b.difference(conjunto_a) # 4

# .symmetric_difference

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) # 1, 4

# .issubset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issubset(conjunto_b) # true
conjunto_b.issubset(conjunto_a) # false

# .issuperset

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_a.issuperset(conjunto_b) # false
conjunto_b.issuperset(conjunto_a) # true

# isdisjoint

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b) # true
conjunto_a.isdisjoint(conjunto_c) # false

# .add

sorteio = {1,23}

sorteio.add(25) # 1,23,25
sorteio.add(42) # 1,23,25,42
sorteio.add(25) # 1,23,25,42

# in (verificar se determinado valor está dentro do conjunto)

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

1 in numeros # true
10 in numeros # false

# .discard / .remove tem a mesma função, remove o valor escolhido