#include <iostream>
#include <vector>

using std::vector;


int lcs2(vector<int> &a, vector<int> &b) {
  //write your code here
  vector<int> result;
  int m = a.size();
  int n = b.size();
  int t = max(m,n);
  int D[m+1][n+1];
  for(int i=0;i<=m;++i) D[i][0]=i;
  for(int i=0;i<=n;++i) D[0][i]=i;
  for(int i=1;i<=m;++i)
  	for(int j=1;j<=n;++j)
  	{
  		int op[3]={t,t,t}; //t is equal to infinite 
  		op[0] = D[i-1][j]+1;
  		op[1] = D[i][j-1]+1;
  		if(a[i-1]==b[j-1]) op[2] = D[i-1][j-1];
  		else op[2] = D[i-1][j-1] + 1; 
  		D[i][j] = min(op[1],op[0]);
  		D[i][j] = min(D[i][j],op[2]);
	}
  	//Backward
  	int i = m;
  	int j = n;
  	while(i!=0&&j!=0)
  	{
  		if(D[i][j]==D[i-1][j-1]&&D[i][j]<=D[i][j-1]&&D[i][j]<=D[i-1][j]) 
		{
		  result.push_back(a[j-1]);
		  i--;
		  j--;
		  continue;	
		}
		if(D[i-1][j]<=D[i][j-1])
		{
			i--;
			continue;
		}
		if(D[i][j-1]<=D[i-1][j])
		{
			j--;
			continue;
		}
	}
  return result.size();
}




// int lcs2(vector<int> &a, vector<int> &b) {
//   //write your code here
//   return std::min(std::min(a.size(), b.size()), c.size());
// }

int main() {
  size_t n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> a[i];
  }

  size_t m;
  std::cin >> m;
  vector<int> b(m);
  for (size_t i = 0; i < m; i++) {
    std::cin >> b[i];
  }

  std::cout << lcs2(a, b) << std::endl;
}
