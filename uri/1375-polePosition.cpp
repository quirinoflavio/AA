#include <bits/stdc++.h>

using namespace std;

int grid[1003];

int main() {

    int n, cn, v;
    bool wrong;
    scanf("%d", &n);
    while (n != 0){
        wrong = false;
        
        memset(grid, 0, sizeof(grid));
        
        for(int i = 0; i < n; i++){
            scanf("%d %d", &cn, &v);
                if((i+v) < 0 || (i+v) >= n || grid[i+v] != 0){
                    wrong = true;
                }
                if (!wrong) grid[i+v] = cn;
            
        }
        if(!wrong){
            for(int i = 0; i < n; i++){
                printf("%d", grid[i]);
                if(i != n-1) printf(" ");
            }
            
        }else{
            printf("-1");
        }
        printf("\n");
        scanf("%d", &n);

    }

    return 0;
}