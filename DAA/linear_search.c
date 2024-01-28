#include <stdio.h>

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++)
        if (arr[i] == key) return i;
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5}, n = 5, key = 3;
    int result = linearSearch(arr, n, key);
    printf(result != -1 ? "Element found at index %d\n" : "Element not found\n", result);
    return 0;
}
