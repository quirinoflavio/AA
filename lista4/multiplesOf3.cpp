#include <bits/stdc++.h>

using namespace std;

void update(int bit[], int n, int index, int value){
    index = index + 1;

    while (index <= n){
        bit[index] += value;
        index += (index & (-index));
    }
    
}

int query(int bit[], int index){
    int sum = 0;
    index = index + 1;

    while (index > 0){
        sum += bit[index];
        index -= (index & (-index);
    }

    return sum;
}

int sum(int a, int b){
    return;
}

