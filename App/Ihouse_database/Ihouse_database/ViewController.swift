//
//  ViewController.swift
//  Ihouse_database
//
//  Created by Braulio Cald on 7/31/19.
//  Copyright © 2019 Braulio Cald. All rights reserved.
//

import UIKit

class ViewController: UIViewController, HomeConnectDelegate, UITableViewDataSource, UITableViewDelegate{
    
    @IBOutlet weak var tableView:
    UITableView!
    var Model = HomeModel()
    
    // Assign an empty array to it
    var table_locations = [Location]()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // set self as the tableview's data source and delegate
        tableView.delegate = self
        tableView.dataSource = self
        
        // Initiate calling the items download
        Model.downloadInfo()
        Model.delegate = self
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        
    }
    
    func itemsdownloaded(locations: [Location]) {
        
        // grab data into tableview
        table_locations = locations
        tableView.reloadData()
    }
    
    // MARK: UITableView Delegate Methods 
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        // if table_locations has nothing then it will return 0
        return table_locations.count
    }
    
    
   
    
    private func tableView( tableView: UITableView, cellForRowAtIndexPath: NSIndexPath) -> UITableViewCell {
        
//        var cell = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        var cell: UITableViewCell = self.tableView.dequeueReusableCell(withIdentifier: "cell")! as UITableViewCell
        cell.textLabel?.text = self.table_locations[Location]
        
        
        
//        cell.textLabel?.text = table_locations[indexPath.row].firstname
       
        
      
      
        return cell
    }


}

