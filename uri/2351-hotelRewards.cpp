#include <bits/stdc++.h>

#define ll long long
using namespace std;

vector<int> prices;

int main()
{

    int n, k, p;
    
    priority_queue<int, vector<int>, greater<int>> priority;

    while (cin >> n >> k)
    {
        int free = 0, count = 0;
        int sum = 0;
        
        for (int i = 0; i < n; i++)
        {
            cin >> p;
            prices.push_back(p);
            sum += p;
        }

        for (int i = 0; i < n; i++)
        {
            if (count == k)
            {
                free++;
                count = 0;
            }
            else
                count++;
            priority.push(prices[i]);
            if (priority.size() > free)
                priority.pop();
        }
        int l = priority.size();
        for (int i = 0; i < l; i++)
        {
            sum -= priority.top();
            priority.pop();
        }

        cout << sum << endl;

    prices.clear();
    }
    return 0;
}