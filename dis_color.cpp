#include<bits/stdc++.h>
using namespace std;

const int N = 1e6 + 5;

int32_t main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);
    #define Task "Flower"
    if(fopen(Task".inp","r")){
        freopen(Task".inp","r",stdin);
        freopen(Task".out","w",stdout);
    }
    int t;
    cin >> t;
    while(t--){
        int n , m , k;
        cin >> n >> m >> k;
        cout << min(n , k) * min(m , k) << "\n";
    }
    return 0;
}
