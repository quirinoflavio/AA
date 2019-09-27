#include <bits/stdc++.h>

using namespace std;

#define LIM (int) 1e9 + 1

int A, B;

int calc_conta(int val){
    int acum = 0;

    if(val > 100){
        val -= 100;
        acum += 100*2;
    } else{
        acum += val*2;
        val -= val;
    } 

    if(val > 9900) {
        val -= 9900;
        acum += 9900*3;
    }else {
        acum += val*3;
        val -= val;
    }

    if(val > 990000) {
        val -= 990000;
        acum += 990000*4;
    }else {
        acum += val*5;
        val -= val;
    }

    acum += val*7;
    return acum;
}

int calc_A(int A, int a){
    return A - a;
}
int calc_B(int B, int a){
    return B + a;
}

int binarySearch(int l, int r) 
{ 
    printf("%d %d\n", l, r);
    if (r >= l) { 
        int mid = l + (r - l) / 2; 
  
        // If the element is present at the middle 
        // itself 
        int custo = calc_conta(mid);
        int resA = calc_A(A, custo);
        int resB = calc_B(B, custo);

        if (resA == resB) // && custo < resB 
            return custo; 
  
        // If element is smaller than mid, then 
        // it can only be present in left subarray 
        if (custo < A) 
            return binarySearch(l, mid - 1); 
  
        // Else the element can only be present 
        // in right subarray 
        return binarySearch(mid + 1, r); 
    } 
  
    // We reach here when element is not 
    // present in array 
    return -1; 
} 

int main(){
    


    scanf("%d%d", &A, &B);
    while(A != 0){
        int a = binarySearch(1, LIM);


        printf("%d\n", a);


        scanf("%d%d", &A, &B);
    }



    return 0;
}