#include <bits/stdc++.h>

using namespace std;
int segTree [4000000];
long long int arr [131073];

int xOr(int a, int op, int b){
    if (op) return (a|b);
    else return (a^b);
}

int switchOP(int op){
    return op^1;
}

void build(int id, int l, int r, int op){
    if (l == r) segTree[id] = arr[l-1];
    else {
        int m = (l + r) / 2;
        build(id*2, l, m, switchOP(op));
        build(id*2+1, m+1, r, switchOP(op));
        segTree[id] = xOr(segTree[id*2], op, segTree[id*2+1]);
    }
}
void update(int id, int l, int r, int v, int pos, int op){
    if (l == r) segTree[id] = v;
    else{
        int m = (l + r) / 2;
        if (pos <= m) update(id*2, l, m, v, pos, switchOP(op));
        else update(id*2+1, m+1, r, v, pos, switchOP(op));
        segTree[id] = xOr(segTree[id*2], op, segTree[id*2+1]);
    }
}

int main(){
    int arrSize, q, i, x, n;
    bool b1;

    cin >> n >> q;
    arrSize = 1 << n;
    for(int i = 0; i < arrSize; i++){
        cin >> arr[i];
    }

    int op = (n % 2) ? 1 : 0;
    build(1, 1, arrSize, op);
    
    for(int j = 0; j < q; j++){
        cin >> i >> x;
        
        update(1, 1, arrSize, x, i, op);

        cout << segTree[1] << endl;

    }

}