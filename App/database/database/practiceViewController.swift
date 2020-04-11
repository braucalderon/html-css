//
//  practiceViewController.swift
//  database
//
//  Created by Braulio Cald on 7/22/19.
//  Copyright © 2019 Braulio Cald. All rights reserved.
//

import UIKit
import Firebase



class practiceViewController: UIViewController, HomeConnectDelegate {
    
    
    
    var Model = Model_Connect()
    
    @IBOutlet weak var lastName_Label: UILabel!
    @IBOutlet weak var room_label: UILabel!
    @IBOutlet weak var room_number: UITextField!
    @IBOutlet weak var last_name: UITextField!
    @IBOutlet weak var login_search: UIButton!
   

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //
        Model.downloadInfo()
        Model.delegate = self       // assign itself to the property of the Model_Connect class
       
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    func itemsdownloaded(locations: [Location]) {
        
    }
    
    
    
} // end class 
