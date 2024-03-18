#include <stdio.h>

int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key) return mid;
        (arr[mid] < key) ? (low = mid + 1) : (high = mid - 1);
    }
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5}, n = 5, key = 3;
    int result = binarySearch(arr, 0, n - 1, key);
    printf(result != -1 ? "Element found at index %d\n" : "Element not found\n", result);
    return 0;
}
