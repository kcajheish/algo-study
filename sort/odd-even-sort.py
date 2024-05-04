class OddEvenSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i%2, n-1, 2):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
