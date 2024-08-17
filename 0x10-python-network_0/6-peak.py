def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    def find_peak_recursive(start, end):
        """Helper function to find peak recursively within the subarray."""
        if start == end:
            return list_of_integers[start]
        
        mid = (start + end) // 2
        mid_value = list_of_integers[mid]
        
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid - 1] <= mid_value) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= mid_value):
            return mid_value
        
        # If the left neighbor is greater, search in the left half
        if mid > 0 and list_of_integers[mid - 1] > mid_value:
            return find_peak_recursive(start, mid - 1)
        
        # If the right neighbor is greater, search in the right half
        return find_peak_recursive(mid + 1, end)
    
    if not list_of_integers:
        return None
    
    return find_peak_recursive(0, len(list_of_integers) - 1)
