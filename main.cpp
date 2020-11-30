//
//  main.cpp
//  Lab 5
//
//  Created by Павло Сливка on 15.11.20.
//  Copyright © 2020 Павло Сливка. All rights reserved.
//

#include <iostream>
#include "Header.h"
#include <string>
#include <vector>
#define length 5
using namespace std;

int main(int argc, const char * argv[]) {
    Home home;
    
    Pet Stepan("Stepan", "Dog", 3, "Hello", 8, DOG);
    home.addAnimal(Stepan);
    Pet Barbos("Barbos", "Dog", 4, "Hi", 4, DOG);
    home.addAnimal(Barbos);
    Pet Garfild("Garfild", "Cat", 10, "Guten Tag", 6, CAT);
    home.addAnimal(Garfild);
    Pet Jackson("Jackson", "Dragon", 1, "Hello", 78, DRAGON);
    home.addAnimal(Jackson);
    Pet Ratatuj("Ratatuj", "Mouse", 2, "Hello", 2, MOUSE);
    home.addAnimal(Ratatuj);
    
    vector<Pet> animals = home.getAnimal();
    sort(animals, 0, length-1);
    for(int i=0; i<length; i++)
    {
        cout << animals[i].getName()<< " ";
        cout << animals[i].getGreeting()<< " ";
        cout << animals[i].getAge()<< " ";
        cout << animals[i].getBreed()<< " ";
        cout << animals[i].getMass()<< " " <<endl;
    }
    
    areFriends(animals, length);
    
    cout << endl;
    cout << "Check politeness of...";
    string name_polite;
    cin >> name_polite;
    for(int i = 0; i<length; i++)
        if(animals[i].getName() == name_polite)
        {
            if(isPolite(&animals[i])) cout << "Is polite";
                else cout << "Isn`t polite";
        }
    cout << endl;
    
    return 0;
}

