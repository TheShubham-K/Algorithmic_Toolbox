#include <iostream>
#include <vector>

// using std::cin;
// using std::cout;
// using std::vector;
// using std::max;

/*
    ********************SAFE MOVE**********************
    Moving as far as the fuel is good enought to reach another gas station
*/

using namespace std;

    /*
        * This program has Loop nested within another loop
        * So, it seems to have O(n * n) run-time
        * But, the run time of the program is O(n)
            => currentRefills can be atmost n - 1
            => numRefills can be atmost n
            => So there will be atmost n + 1 operations
                => O(n + 1) => O(n)
    */

int compute_min_refills(int d, int tank, vector<int> & stops,int n) {
    // write your code here
    int start = 0, end = 0, count = 0, i = 0;
    int lind = n;
    if (tank >= d)
    {
        return 0;
    }
    while (start < d)
    {
        int check = 0;
        while (i < n && (stops[i] - start) <= tank)
        {
            end = stops[i];
            i++;
            check++;
        }
        if (end == stops[lind - 1])
        {
            if (d - start <= tank)
            {
                return count;
            }
            else
            {
                /*if (d - end <= tank)
                {
                    count++;
                    return count;
                }
                else*/
                if(d-end>tank)
                {
                    return -1;
                }
            }
        }
        if (check == 0)
        {
            return -1;
        }
        else
        {
            count++;
            //cout << end << " ";
            start = end;
        }
    }
    return count;
}

int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops, n) << "\n";

    return 0;
}




// int compute_min_refills(int dist, int tank, vector<int> & stops) {
//     // write your code here
//     return -1;
// }


// int main() {
//     int d = 0;
//     cin >> d;
//     int m = 0;
//     cin >> m;
//     int n = 0;
//     cin >> n;

//     vector<int> stops(n);
//     for (size_t i = 0; i < n; ++i)
//         cin >> stops.at(i);

//     cout << compute_min_refills(d, m, stops) << "\n";

//     return 0;
// }
