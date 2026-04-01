#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    int n = 5;

    // Update beginning
    arr[0] = 100;

    // Update middle
    arr[n/2] = 200;

    // Update end
    arr[n-1] = 300;

    // Print array
    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}