#include <bits/stdc++.h>

#define MAXN 100005
#define PI 3.14159265359
using namespace std;

int scores[MAXN];
int aux[MAXN];

int main()
{
    int n, score;
    while (cin >> n)
    {
        for (int i = 0; i < n; i++)
        {
            cin >> score;
            scores[i] = score;
        }

        sort(scores, scores + n);

        int i = 0, j = n - 1, k = 0;
        while (i <= j)
        {
            aux[i++] = scores[k++];
            if (k < n)
                aux[j--] = scores[k++];
        }


        double S = 0;
        double sen = sin(2*PI / n);
        
        for(int x = 0; x < n-1; x++){
            S += (aux[x] * aux[x+1] * sen);
        }
        S += (aux[n-1] * aux[0] * sen);
        S/=2;

        cout << fixed << setprecision(3) << S << endl;
    }

    return 0;
}