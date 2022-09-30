#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
const int N = 1e5 + 5;
int n, m, s, p, cnt;
int vis[N], now[N];
struct node{
	int from,to;
}e[N];
void add(int u, int v){
	e[++cnt].from = now[u];
	now[u] = cnt;
	e[cnt].to = v;
}
void dfs(int u){
	vis[u] = 1;
	for(int i = now[u]; i; i = e[i].from){
		int v = e[i].to;
		if(!vis[v]) dfs(v);
	}
}
int main(){
    cin >> n >> m;
    int x, y;
    for(int i = 1; i <= m ; i++){
    	cin >> x >> y;
    	add(x,y);
	} 
	cin >> s >> p;
	int t = 0;
	dfs(s);
	if(vis[p]) t++;
	memset(vis,0,sizeof(vis));
	dfs(p);
	if(vis[s]) t++;
	if(t == 2) cout << "yes";
	else cout << "no"; 
	return 0;
}