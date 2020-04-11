//
//  ViewController.swift
//  Log_In
//
//  Created by Braulio Cald on 8/12/19.
//  Copyright © 2019 Braulio Cald. All rights reserved.
//

import UIKit
import Firebase


class ViewController: UIViewController {

    @IBOutlet weak var emailtextfiel: UITextField!
    
    @IBOutlet weak var passwordtextfield: UITextField!
    
    @IBOutlet weak var LogInButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    
    
    @IBAction func LogIn_Button(_ sender: UIButton) {
        
        if let email = emailtextfiel.text, let password = passwordtextfield.text
        {
            Auth.auth().signIn(withEmail: email, password: password) { [weak self] user, error in
                guard self != nil else { return }
                // ...
            }
        }
        
        
        
    }
    

}

