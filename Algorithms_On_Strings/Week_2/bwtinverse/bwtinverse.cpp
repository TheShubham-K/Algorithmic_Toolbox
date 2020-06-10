#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

string InverseBWT(const string &bwt)
{
  string text = "";

  // write your code here
  vector<pair<char, int>> col1(bwt.size());
  for (int i = 0; i < bwt.size(); i++)
  {
    col1[i] = make_pair(bwt[i], i);
  }
  sort(col1.begin(), col1.end());

  pair<char, int> symbol = col1[0];
  for (int i = 0; i < bwt.size(); i++)
  {
    symbol = col1[symbol.second];
    text += symbol.first;
  }
  return text;
}

int main()
{
  string bwt;
  cin >> bwt;
  cout << InverseBWT(bwt) << endl;
  return 0;
}
