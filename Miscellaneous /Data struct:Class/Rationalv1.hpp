//
//  Rationalv1.hpp
//  Rational
//
//  Created by Braulio Cald on 4/24/18.
//  Copyright © 2018 Braulio Cald. All rights reserved.
//

#ifndef Rationalv1_hpp
#define Rationalv1_hpp

#include <stdio.h>
#include <iostream>

class Rational {
    
public:
    // constructor
    Rational(int n = 0, int d = 1) { set(n, d); }
    
    // sets to n / d
    bool set(int n, int d);
    
    // access functions
    int num() const { return num_; }
    int den() const { return den_; }
    
    // returns decimal equivalent
    double decimal() const { return num_ / double(den_); }
    
private:
    int num_, den_; // numerator and denominator
};

// prototype for operator+ standalone function
Rational operator+(const Rational &r1, const Rational &r2);
Rational operator-(const Rational &r1, const Rational &r2);
Rational operator*(const Rational &r1, const Rational &r2);
Rational operator/(const Rational &r1, const Rational &r2);




#endif /* Rational_hpp */
