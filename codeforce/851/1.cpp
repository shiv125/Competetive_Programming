#include<bits/stdc++.h>
#define ll long long
#define f(i,n) for(int i=0;i<n;i++)
#define rep(i,n) for (int i=1;i<n;i++)
#define ma 2100007
#define inf 1000000000000
using namespace std;
  int[] hungarianMethod(int w[][]) {
        final int n = w.length, m = w[0].length, PHI = -1, NOL = -2;
        boolean[] x[] = new boolean[n][m], ss = new boolean[n], st = new boolean[m];
        int[] u = new int[n], v = new int[m], p = new int[m], ls = new int[n], lt = new int[m], a = new int[n];
        int f = 0;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                f = max(f, w[i][j]);

        fill(u, f);
        fill(p, INF);
        fill(lt, NOL);
        fill(ls, PHI);
        fill(a, -1);

        while (true) {
            f = -1;
            for (int i = 0; i < n && f == -1; i++)
                if (ls[i] != NOL && !ss[i])
                    f = i;

            if (f != -1) {
                ss[f] = true;
                for (int j = 0; j < m; j++)
                    if (!x[f][j] && u[f] + v[j] - w[f][j] < p[j]) {
                        lt[j] = f;
                        p[j] = u[f] + v[j] - w[f][j];
                    }
            } else {
                for (int i = 0; i < m && f == -1; i++)
                    if (lt[i] != NOL && !st[i] && p[i] == 0)
                        f = i;

                if (f == -1) {
                    int d1 = INF, d2 = INF, d;
                    for (int i : u)
                        d1 = min(d1, i);

                    for (int i : p)
                        if (i > 0)
                            d2 = min(d2, i);

                    d = min(d1, d2);

                    for (int i = 0; i < n; i++)
                        if (ls[i] != NOL)
                            u[i] -= d;

                    for (int i = 0; i < m; i++) {
                        if (p[i] == 0)
                            v[i] += d;
                        if (p[i] > 0 && lt[i] != NOL)
                            p[i] -= d;
                    }

                    if (d2 >= d1)
                        break;
                } else {
                    st[f] = true;
                    int s = -1;

                    for (int i = 0; i < n && s == -1; i++)
                        if (x[i][f])
                            s = i;

                    if (s == -1) {
                        for (int l, r; ; f = r) {
                            r = f;
                            l = lt[r];

                            if (r >= 0 && l >= 0)
                                x[l][r] = !x[l][r];
                            else
                                break;

                            r = ls[l];
                            if (r >= 0 && l >= 0)
                                x[l][r] = !x[l][r];
                            else
                                break;
                        }

                        fill(p, INF);
                        fill(lt, NOL);
                        fill(ls, NOL);
                        fill(ss, false);
                        fill(st, false);

                        for (int i = 0; i < n; i++) {
                            boolean ex = true;
                            for (int j = 0; j < m && ex; j++)
                                ex = !x[i][j];
                            if (ex)
                                ls[i] = PHI;
                        }
                    } else
                        ls[s] = f;
                }
            }
        }

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (x[i][j])
                    a[j] = i;
        return a;
    }

int main(){
int t,m,n;
cin>>t;
while (t>0){
t--;
int arr[n][m];
f(i,n){f(j,n) cin>>arr[i][j];}
cout<<hungarianMethod(arr)<<endl;

}
return 0;
}
