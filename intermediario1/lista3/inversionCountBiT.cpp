#include<bits/stdc++.h> 
using namespace std; 
//const int MAXN = 2000001;
//int arr1[MAXN];
//int arr2[MAXN];
#define LL long long
  
LL a[200009];
LL b[200009];
LL tree[200009];
LL n;




LL query(LL idx)
{
    LL ret=0;
    while(idx>0)
    {
        ret+=tree[idx];
        idx-=idx&-idx;
    }
    return ret;
}

// int query(int BITree[], int index) { 
//     int ret = 0;

//     while (index > 0) {       
//         ret += BITree[index]; 
//         index -= index & (-index); 
//     } 

//     return ret; 
// } 

void update(LL idx,LL val)
{
    while(idx<=n)
    {
        tree[idx]+=val;
        idx+=idx&-idx;
    }
}

// void update(int BITree[], int n, int index, int val) { 
//     while (index <= n) { 
//        BITree[index] += val; 
  
//        index += index & (-index); 
//     } 
// } 

// int getInvCount(int arr[], int n) { 
//     int invCount = 0;

//     int maxElement = 0; 
//     for (int i=0; i<n; i++) 
//         if (maxElement < arr[i]) 
//             maxElement = arr[i]; 
  
    
//     int BIT[maxElement+1]; 
//     for (int i=1; i<=maxElement; i++) 
//         BIT[i] = 0; 
  
    
//     for (int i=n-1; i>=0; i--) { 
//         invCount += query(BIT, arr[i]-1); 
  
//         update(BIT, maxElement, arr[i], 1); 
//     } 
  
//     return invCount; 
// } 

int main() {
    LL i,j,k,m,d,test,t=0, num;
    scanf("%lld",&test);
    while(test--)
    {
        cin >> n;
        memset(tree,0,sizeof(tree));
        for(i=0;i<n;i++)
        {
            cin >> num;
            a[i] = num;
            b[i] = num;
        }
        sort(b,b+n);
        
        for(i=0;i<n;i++)
        {
            d=lower_bound(b,b+n,a[i])-b;
            a[i]=d+1;
            cout << "a[" << i << "] = " << d+1 << endl;
        }
        LL ans=0;
        for(i=n-1;i>=0;i--)
        {
            ans=ans+query(a[i]-1);
            update(a[i],1);
        }

        cout << ans << endl;
    }
    return 0;
} 