#include <stdio.h>

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[minIndex]) minIndex = j;
        int temp = arr[i]; arr[i] = arr[minIndex]; arr[minIndex] = temp;
    }
}

int main() {
    int arr[] = {5, 2, 9, 1, 5}, n = 5;
    selectionSort(arr, n);
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}
