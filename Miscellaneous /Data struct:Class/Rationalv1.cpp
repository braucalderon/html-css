//
//  Rationalv1.cpp
//  Rational
//
//  Created by Braulio Cald on 4/24/18.
//  Copyright © 2018 Braulio Cald. All rights reserved.
//

#include"Rationalv1.hpp"
#include <iostream>
using namespace std;

bool Rational::set(int n, int d)
{
    if (d != 0) {
        num_ = n;
        den_ = d;
        return true;
    }
    else
        return false;
}


Rational operator+(const Rational &r1, const Rational &r2){
    int num, den;
    
    num = r1.num() * r2.den() + r2.num() * r1.den();
    den = r1.den() * r2.den();
    return Rational(num, den);
}
Rational operator-(const Rational &r1, const Rational &r2){
    int num, den;
    
    num = r1.num() * r2.den() - r2.den() * r1.den();
    den = r1.den() * r2.den();
    return Rational(num, den);
}
Rational operator*(const Rational &r1, const Rational &r2){
    int num, den;
    
    num = r1.num() * r2.num();
    den = r1.den() * r2.den();
    return Rational(num, den);
}
Rational operator/(const Rational &r1, const Rational &r2){
    int num, den;
    
    num = r1.num() / r1.den();
    den = r2.den() / r2.num();
    return Rational(num, den);
}



