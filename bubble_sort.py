def bubble_sort(A, i):
	if i == 1:
		return A
	else:
		for j in range(i - 1):
			if A[j] > A[j+1]:
				A[j], A[j + 1] = A[j + 1], A[j]
		return bubble_sort(A, i - 1)

if __name__ == "__main__":
	print(bubble_sort([24, 13, 9, 64, 7, 23, 34, 47], 8))
