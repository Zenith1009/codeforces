#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#define ll long long
using namespace std;

bool rt_tri(pair<int, int> p1, pair<int, int> p2, pair<int, int> p3) {
    long long d1 = sq_dist(p1, p2);
    long long d2 = sq_dist(p2, p3);
    long long d3 = sq_dist(p3, p1);
    
    vector<long long> sides = {d1, d2, d3};
    sort(sides.begin(), sides.end());
    return sides[0] + sides[1] == sides[2];
}

ll sq_dist(pair<int, int> a, pair<int, int> b) {
    return pow(a.first - b.first, 2) + pow(a.second - b.second, 2);
}

int solve() {
    int n;
    cin >> n;
    vector<pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].first >> points[i].second;
    }
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (rt_tri(points[i], points[j], points[k])) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << solve() << endl;
    }
    return 0;
}
