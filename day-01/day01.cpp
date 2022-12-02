#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string filename = "input.txt";

  ifstream ifs(filename);

  long int max_sum;
  long int sum;

  string line;
  while (getline(ifs, line)) {
    if (line == "") {
      sum = 0;
    } else {
      sum += stoi(line);
    }
    max(sum, max_sum);
  }
  max_sum = max(sum, max_sum);

  cout << endl << max_sum << endl;

  ifs.close();
  return 0;
}