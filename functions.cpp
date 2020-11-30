#include "Header.h"
#include <string>
#include <vector>
#include <iostream>
using namespace std;

Pet::Pet(string name, string breed, int age, string greeting, int mass, kind Kind)
{
    this->name = name;
    this->breed = breed;
    this->age = age;
    this->greeting = greeting;
    this->mass = mass;
    this->Kind = Kind;
}

Pet::~Pet(){};
Home::Home(){};
Home::~Home(){};


void Home::addAnimal(Pet newAnimal)
{
    animal.push_back(newAnimal);
    this->count++;
}

vector<Pet> Home::getAnimal()
{
    return animal;
}

string Pet::getName()
{
    return name;
}

string Pet::getGreeting()
{
    return greeting;
}
int Pet::getAge()
{
    return age;
}
int Pet::getMass()
{
    return mass;
}
string Pet::getBreed()
{
    return breed;
}

bool isPolite(Pet* a)
{
    Pet b = *a;
    if(b.getGreeting() == "Hello") return 1;
    else return 0;
}

void areFriends(vector <Pet> &animal, int l)
{
    for(int i=0; i<(l-1); i++)
    {
        if( abs( animal[i+1].getAge()-animal[i].getAge() ) < 2 )
        {
            cout << endl;
            cout << animal[i+1].getName() << " and " << animal[i].getName() << " are friends";
            cout << endl;
        }
    }
}

//sort
void swap(Pet &a, Pet &b)
{
    Pet v = a;
    a = b;
    b = v;
}

int partition(vector<Pet> &a,int low,int high)
{
    int pivot = a[high].getAge();
    int i = low-1;
    
    for(int j=low; j<high; j++)
    {
        if(a[j].getAge() < pivot)
        {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[++i], a[high]);
    return i;
}

void sort(vector<Pet> &a, int low, int high)
{
    if(low < high)
    {
        int pi = partition(a, low, high);
        sort(a, low, pi-1);
        sort(a, pi+1, high);
        
    }
}
