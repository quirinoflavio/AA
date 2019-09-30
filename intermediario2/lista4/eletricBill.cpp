#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define LIM (int) 1e9 + 1

ll A, B;

ll calc_conta(ll val){
    ll acum = 0;

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
        acum += 990000*5;
    }else {
        acum += val*5;
        val -= val;
    }

    acum += val*9;
    return acum;
}

ll calc_consumo(ll val){
    ll cons = 0;

    if(val >= 200){
        val -= 200;
        cons += 100;
    } else{
        cons += val/2;
        val -= val;
    } 

    if(val >= 29700) {
        cons += 9900;
        val -= 29700;
    }else {
        cons += val/3;
        val -= val;
    }

    if(val >= 4950000) {
        cons += 990000;
        val -= 4950000;
    }else {
        cons += val/5;
        val -= val;
    }

    cons += val/7;
    return cons;
}


ll binarySearch(ll l, ll r) { 
    
    
    if (r >= l) { 
        
        ll c1 = (l+r) >> 1; 
        ll custo1 = calc_conta(c1);
        ll custo2 = B + custo1;
        ll c2 = calc_consumo(custo2);
        ll total = calc_conta(c1 + c2);

        //printf("%lld..%lld %lld %lld %lld %lld %lld\n", l, r, c1, custo1, c2, custo2, total);

        if (total == A)
            return custo1; 
  
        if (total > A) 
            return binarySearch(l, c1 - 1); 
  
        return binarySearch(c1 + 1, r); 
    } 

    return -1; 
} 

int main(){
    


    scanf("%lld%lld", &A, &B);
    while(A != 0){
        ll a = binarySearch(1, A);


        printf("%lld\n", a);


        scanf("%lld%lld", &A, &B);
    }



    return 0;
}