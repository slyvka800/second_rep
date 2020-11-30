
#include <string>
#include <vector>
using namespace std;
enum kind{
    DOG,
    CAT,
    BIRD,
    ELEPHANT,
    SQUIRREL,
    DRAGON,
    MOUSE
};

class Pet
{
private:
    
    string name;
    string breed;
    int age;
    string greeting;
    int mass;
    kind Kind;

public:
    Pet();
    ~Pet();
    Pet(string, string, int, string, int, kind);
    
    friend bool isPolite(Pet*);
    string getName();
    string getGreeting();
    int getAge();
    string getBreed();
    int getMass();
};

class Home
{
private:
    int count = 0;
    vector<Pet> animal;
public:
    Home();
    ~Home();
    void addAnimal(Pet);
    vector<Pet> getAnimal();
    
};

void sort(vector <Pet> &, int, int);
void areFriends(vector <Pet>&, int);
