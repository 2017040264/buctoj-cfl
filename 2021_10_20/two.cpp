#include<iostream>
using namespace std;
const int mod = 1e9 + 7;

int main() {
	string n;
	cin >> n;

	long long res = 1, cnt = 0;
	for (long long i = 0; i < n.size(); i++) {
		cnt = (cnt * 3) % mod;//d[i][1]=d[i-1][1]*3

		if (n[i] == '1') {
			cnt = (cnt + res) % mod;//d[i][1]+=d[i-1][0]
			res = (res * 2) % mod;//d[i][0]=d[i-1][0]*2
		}
	}

	cout << (res + cnt) % mod;//d[length(n)][0]+d[length(n)][1]
	return 0;
}
