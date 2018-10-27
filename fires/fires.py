import qU

def placeFighers(arr, n, minDist, startXX, startYY):
	graph = {}
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			graph[(i, j)] = []

	
	minDistSquares = set()
	for i in range(minDist + 1):
		for j in range(minDist + 1).reverse():
			minDistSquares.add((startXX - i, startYY - j))
			minDistSquares.add((startXX + i, startYY + j))
			minDistSquares.add((startXX - i, startYY + j))
			minDistSquares.add((startXX + i, startYY - j))

