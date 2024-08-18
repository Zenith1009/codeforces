#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

// Function to calculate the squared distance between two points
ll calculateDistanceSquared(ll x1, ll y1, ll x2, ll y2) {
    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
}

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        
        vector<pair<ll, ll>> circles(n);
        for (int i = 0; i < n; i++) {
            cin >> circles[i].first >> circles[i].second;
        }
        
        ll xs, ys, xt, yt;
        cin >> xs >> ys >> xt >> yt;
        
        ll comp = calculateDistanceSquared(xs, ys, xt, yt);
        bool possible = true;

        for (const auto& circle : circles) {
            ll xi = circle.first, yi = circle.second;
            ll distanceToStart = calculateDistanceSquared(xs, ys, xi, yi);
            ll distanceToEnd = calculateDistanceSquared(xt, yt, xi, yi);
            
            // If the target is within the reach of the circle before you can get there
            if (distanceToEnd <= comp) {
                possible = false;
                break;
            }
        }

        if (possible) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}