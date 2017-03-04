def selection_sort(A, i):
	if i == len(A) - 1:
		return A
	else:
		min = i
		for j in range(i,len(A)):
			if A[j] < A[min]:
				min = j
		A[i], A[min] = A[min], A[i]
		return selection_sort(A, i + 1)

if __name__ == "__main__":
	z = selection_sort([34, 17, 23, 35, 45, 9, 1], 0)
	print(z)
