import numpy as np

pathPrices = 'instrumentsPrices.txt'
pathNames = 'instrumentsNames.txt'
pathSuppliers = 'instrumentsSuppliers.txt'
pathMatrix = 'matrix.txt'
pathMatrix2 = 'matrix2.txt'

def separateAnswers():
    print('----------------------------------')

pricesArray = np.array(np.genfromtxt(pathPrices, delimiter=',', dtype=float))
namesArray = np.array(np.genfromtxt(pathNames, delimiter=',', dtype=str))
suppliresArray = np.array(np.genfromtxt(pathSuppliers, delimiter=',', dtype=str))
# Seria uma melhor prática separar o np.genfromtxt em uma váriavel e passar essa variável pro np.array?
separateAnswers()

# 2.1 - Dado estatístico sem axis
highestPrice = pricesArray.max()
cheapestPrice = pricesArray.min()
print(f'The highest quoted price: US$ {highestPrice} The cheapest quoted price: US${cheapestPrice}')
separateAnswers()

# 2.2 - Dado estatísico com axis = 0
suppliersPrices = pricesArray.sum(axis=0)
for i in range(len(suppliersPrices)):
    print(f'All instruments from {suppliresArray[i]} costs US${suppliersPrices[i]}')
separateAnswers()

# 2.3 - Dado estatístico com axis = 1
instrumentsPrices = pricesArray.mean(axis=1)
for i in range(len(instrumentsPrices)):
    print(f'The average value of quoted {namesArray[i]} were US${instrumentsPrices[i]}')
separateAnswers()

# 3 - Obter a transposta de uma matriz e realizar uma operação com ela 
## Cria matriz para verificar se um matriz é simétrica, utilizando sua transposta na verificação
matrixArray = np.array(np.genfromtxt(pathMatrix, delimiter=',', dtype=float))
def checkSymmetricMatrix(m):
    transposedM = m.T
    if np.array_equal(m, transposedM):
        return True
    return False

print(checkSymmetricMatrix(matrixArray))
separateAnswers()

# 4 - Realizar um produto escalar entre duas matrizes ou de um array com uma matriz;
matrix2Array = np.array(np.genfromtxt(pathMatrix2, delimiter=',', dtype=float))
dotProductMatrix = matrixArray @ matrix2Array
print(dotProductMatrix)
separateAnswers()

# 5 - Criar um filtro para a matriz; 
## Filtra preços entre a faixa de 500 e 1000
pricesInRange = pricesArray[(pricesArray > 500) & (pricesArray < 1000)]
print(pricesInRange)
separateAnswers()

# 6 - Realizar alguma operação aritmética (número com matriz, array com matriz, etc.);
## Aplica desconto fixo nos produtos conforme o fornecedor
discountsPercentages = [0.75, 0.8, 0.9, 0.95]
pricesWithDiscount = pricesArray * discountsPercentages
print(pricesWithDiscount)
separateAnswers()
