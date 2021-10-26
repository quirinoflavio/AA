#include <bits/stdc++.h>
using namespace std;

#define MAXN 100000

int nextHole[MAXN];
int jumps[MAXN];
int block[MAXN];
int input[MAXN];
int jumpCounter, lastHole; 

void update(int idx, int val, int n)
{
    input[idx] = val;
    int b = block[idx];
    while (idx >= 0 && block[idx] == b)
    {
        int j = 0;
        int nh = idx + input[idx];

        if (nh < n && block[nh] == block[idx])
        {
            nextHole[idx] = nextHole[nh];
            jumps[idx] = jumps[nh] + 1;
        }
        else
        {
            nextHole[idx] = nh;
            jumps[idx] = 1;
        }
        idx--;
    }
}

void query(int h, int n)
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

    jumpCounter = jc;
    lastHole = nh+1;
}
void preprocess(int n)
{

    int blk_idx = -1;

    int blk_sz = ceil(sqrt(n));

    for (int i = 0; i < n; i++)
    {
        if (i % blk_sz == 0)
        {
            blk_idx++;
        }
        block[i] += blk_idx;
    }


    for (int i = n - 1; i >= 0; i--)
    {
        int j = 0;
        int nh = i + input[i];

        if (nh < n && block[nh] == block[i])
        {
            nextHole[i] = nextHole[nh];
            jumps[i] = jumps[nh] + 1;
        }
        else
        {
            nextHole[i] = nh;
            jumps[i] = 1;
        }
    }
}

int main()
{
    int n, q, v;
    scanf("%d %d", &n, &q);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &v);
        input[i] = v;
    }
    preprocess(n);

    
    for (int i = 0; i < q; i++)
    {

        int t, p, y;
        scanf("%d", &t);

        if (t == 1)
        {
            scanf("%d", &p);
            query(p-1, n);
            printf("%d %d\n", lastHole, jumpCounter);
        }
        else
        {
            scanf("%d %d", &p, &y);
            update(p - 1, y, n);
        }
    }

    return 0;
}