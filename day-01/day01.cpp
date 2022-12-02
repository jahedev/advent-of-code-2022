#include <algorithm>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

long int day1_p1(ifstream &ifs) {
  long int max_sum = -1;
  long int sum = 0;

  string line;
  while (getline(ifs, line)) {
    if (line == "") {
      sum = 0;
    } else {
      sum += stoi(line);
    }
    max_sum = max(sum, max_sum);
  }

  return max_sum;
}

long long int day1_p2(ifstream &ifs) {
  priority_queue<long int> max_cals;

  long int sum = 0;

  string line;
  while (getline(ifs, line)) {
    if (line == "") {
      max_cals.push(sum);
      sum = 0;
    } else {
      sum += stoi(line);
    }
  }
  max_cals.push(sum);

  long int max_sum = 0;

  for (int i = 1; i <= 3; i++) {
    max_sum += max_cals.top();
    max_cals.pop();
  }

  return max_sum;
}

int main() {
  string filename = "input.txt";
  ifstream ifs(filename);

  long int ans_p1 = day1_p1(ifs);
  ifs.clear();
  ifs.seekg(0);
  long int ans_p2 = day1_p2(ifs);

  cout << "Part 1: " << ans_p1 << endl;
  cout << "Part 2: " << ans_p2 << endl;

  ifs.close();
  return 0;
}