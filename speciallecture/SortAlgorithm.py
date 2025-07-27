import csv


class SortAlgorithm:
    def buggy_quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x <= pivot]
            greater_than_pivot = [x for x in arr[1:] if x > pivot]
            return self.buggy_quick_sort(less_than_pivot) + [pivot] + self.buggy_quick_sort(greater_than_pivot)