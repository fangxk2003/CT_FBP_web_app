// your_cpp_program.cpp
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cerr << "Usage: program <input_file> <output_file>\n";
        return 1;
    }

    ifstream in(argv[1]);
    ofstream out(argv[2]);

    string line;
    while (getline(in, line)) {
        out << "Processed: " << line << endl;
    }

    in.close();
    out.close();
    return 0;
}
