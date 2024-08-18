// #include <bits/stdc++.h>

// using namespace std;

// const int M = 2e5 + 5;
// int a[M];
// int v[M];

// void solve() {
//    	int n; cin >> n;
//    	for(int i = 1; i <= n; i++) cin >> a[i];
//    	for(int i = 1; i <= n; i++) v[i] = 0;
//    	v[n + 1] = 0;

// 	bool ok = true;
// 	for(int i = 1; i <= n; i++) {
// 		v[a[i]] = true;
// 		if(i > 1 && !v[a[i] - 1] && !v[a[i] + 1]) ok = false;
// 	}

// 	if(ok) {
// 		cout << "YES" << '\n';
// 	} else {
// 		cout << "NO" << '\n';
// 	}
// }

// int main() {
//     int t = 1;
//     cin >> t;
//     while (t--) {
//         solve();
//     }
//     return 0;
// }

#include <bits/stdc++.h>

using namespace std;

const int M = 2e5 + 5;
int a[M];
int c[M];
int v[M];
map<int, int> p;

void solve() {
    int n; cin >> n;
    for(int i = 1; i <= n; i++) cin >> a[i];

	int m; cin >> m;
	for(int i = 1; i <= m; i++) {
		string q; cin >> q;
		p.clear();
		if(q.size() != n) {
			cout << "NO" << '\n';
			continue;
		}
		for(int i = 0; i <= 26; i++) {
			v[i] = false;
		}

		bool ok = true;
		for(int i = 0; i < n; i++) {
			int d = q[i] - 'a';
			if(!v[d]) {
				if(p[a[i + 1]]) ok = false;
				p[a[i + 1]] = true;
				v[d] = true;
				c[d] = a[i + 1];
			}

			ok &= (c[d] == a[i + 1]);
		}

		if(ok) {
			cout << "YES" << '\n';
		} else {
			cout << "NO" << '\n';
		}
	}
}

int main() {
    int t = 1;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
