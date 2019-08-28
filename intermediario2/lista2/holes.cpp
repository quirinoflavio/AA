// C++ program to demonstrate working of Square Root
// Decomposition.
#include "iostream"
#include "math.h"
using namespace std;

#define MAXN 100000
#define SQRSIZE 317

int nextHole[MAXN];
int jumps[MAXN];
int block[MAXN];
int input[MAXN];
int blk_sz; // block size

// Time Complexity : O(1)
void update(int idx, int val, int n)
{
    input[idx] = val;
    int b = block[idx];
    while (idx >= 0 && block[idx] == b)
    {
        int j = 0;
        int nh = idx + input[idx];
        while (nh < n && block[nh] == block[idx])
        {
            j = jumps[nh];
            nh = nextHole[nh];
        }
        nextHole[idx] = nh;
        jumps[idx] = j + 1;
        idx--;
    }
}

// Time Complexity : O(sqrt(n))
pair<int, int> query(int h, int n)
{

    int jc = 0;
    int nh = h;
    while (h < n)
    {
        nh = h;
        jc += jumps[h];
        h = nextHole[h];
    }

    while (nh + input[nh] < n)
    {
        nh = nh + input[nh];
    }

    return {nh+1 , jc};
}

// Fills values in input[]
void preprocess(int n)
{

    // initiating block pointer
    int blk_idx = -1;

    // calculating size of block
    blk_sz = ceil(sqrt(n));

    // building the decomposed array
    for (int i = 0; i < n; i++)
    {
        if (i % blk_sz == 0)
        {
            // entering next block
            // incementing block pointer
            blk_idx++;
        }
        block[i] += blk_idx;
    }

    nextHole[n-1] = input[n-1] + n-1;
    jumps[n-1] = 1;
    for (int i = n - 2; i >= 0; i--)
    {
        int j = 0;
        int nh = i + input[i];
        /*
        while (nh < n && block[nh] == block[i])
        {
            j = jumps[nh];
            //mudar para nextHOle
            nh = nh + input[nh];
        }

        nextHole[i] = nh;
        jumps[i] = j + 1;
        */
       if (nh < n && block[nh] == block[i]){
        nextHole[i] = nextHole[nh] ;
        jumps[i] = jumps[nh] +1;
       }
       else{
           nextHole[i] = nh;
           jumps[i] = 1;
       }
    }
}

// Driver code
int main()
{
    int n, q, v;
    cin >> n >> q;

    //preenche array
    for (int i = 0; i < n; i++)
    {
        cin >> v;
        input[i] = v;
    }
    preprocess(n);
    for (int i = 0; i < n; i++)
    {
        cout << block[i]<<" ";

    }
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        cout << nextHole[i]<<" ";

    }
    cout << endl;
    for (int i = 0; i < n; i++)
    {
        cout << jumps[i]<<" ";

    }
    cout << endl;
    
    //for nas queries
    for (int i = 0; i < q; i++)
    {
        
        int t, p, y;
        cin >> t;
        
        if (t == 1)
        {
            //não consegue ler p
            cin >> p;
            pair<int, int> q = query(p - 1, n);
            cout << q.first << " " << q.second << endl;
        }
        else
        {
            cin >> p >> y;
            update(p, y, n);
        }
    }
    

    return 0;
}