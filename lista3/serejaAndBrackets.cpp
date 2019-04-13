#include <bits/stdc++.h>

using namespace std;

struct node{
    int opening = 0;
    int matched = 0;
    int closing = 0;
};

node segTree [4000000];
string arr;

node createNode(char bracket) {
    node newNode;
    (bracket == '(') ? (newNode.opening = 1) : (newNode.closing = 1);
    return newNode;
}

node crossOver(node n1, node n2){
    node newNode;
    int b, oa1, a, c;
    b = n1.matched + n2.matched + min(n1.opening, n2.closing);
    oa1 = min(n1.opening, n2.closing);
    n1.opening -= oa1;
    n2.closing -= oa1;

    a = n1.opening + n2.opening;
    c = n1.closing + n2.closing;

    newNode.opening = a;
    newNode.matched = b;
    newNode.closing = c;
    return newNode;
}

void build(int id, int l, int r){
    if (l == r) {
        segTree[id] = createNode(arr[l-1]);
    }else{
        int m = (l + r) / 2;
        build(id*2, l, m);
        build(id*2+1, m+1, r);
        segTree[id] = crossOver(segTree[id*2], segTree[id*2+1]);
    }
}



node query(int id, int l, int r, int x, int y){
    if (x <= l && r <= y) return segTree[id];
    else if (y < l || r < x) {
        node emptyNode;
        return emptyNode;
    }
    int m = (l + r) / 2;
    return crossOver(query(id*2, l, m, x, y), query(id*2+1, m+1, r, x, y));
}



int main(){
    int N, q, q1, q2;
    cin >> arr;
    cin >> q;
    N = arr.length();
    build(1, 1, N);
    while (q > 0){
        cin >> q1 >> q2;
        cout << query(1, 1, N, q1, q2).matched * 2 << endl;
        q--;
    }

    return 0;
}