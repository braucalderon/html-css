//
//  Location.swift
//  database
//
//  Created by Braulio Cald on 7/29/19.
//  Copyright © 2019 Braulio Cald. All rights reserved.
//

import Foundation

struct Location {
    
    
    private var firstname:String
    private var lastname:String
    private var room:String
    private var freenights: String
    private var paidnights: String
    private var totalnights: String
    
    init(){
        firstname = " "
        lastname = " "
        room = " "
        freenights = " "
        paidnights = " "
        totalnights = " "
    }
    
    init(firstname: String, lastname: String, room: String, freenights: String, paidnights: String, totalnights: String ){
        
        self.firstname = firstname
        self.lastname = lastname
        self.room = room
        self.paidnights = paidnights
        self.freenights = freenights
        self.totalnights = totalnights
    }
    
    var description: String {
        return "firstname:  \(firstname), lastname: \(lastname), room: \(room), freenights: \(freenights), paidnights: \(paidnights), totalnights: \(totalnights)"
        
    }
    
   
    
    
}
