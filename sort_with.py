def bubble(items: list) -> list:
  ''' A Python implementiation of the BubbleSort Algorithm. '''
    for idx in range(len(items)):
        for j in range(0, len(items)-idx-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


def selection(items: list) -> list:
    ''' A Python implementiation of the Selection Sort Algorithm. '''
    for idx in range(len(items)):
        min_idx = idx
        for i in range(idx, len(items)):
            if items[i] < items[min_idx]:
                min_idx = i
        items[idx], items[min_idx] = items[min_idx], items[idx]
    return items


def merge(items: list) -> list:
    ''' A Python implementiation of the MergeSort Algorithm. '''
    def _merge(left, right):
            result = []
            while left and right:
                if left[0] <= right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            if left:
                result += left
            if right:
                result += right
            return result 

    if len(items) <= 1:
        return items

    middle = len(items)//2

    left = items[:middle]
    right = items[middle:]
    
    left = merge(left)
    right = merge(right)

    return _merge(left, right)
