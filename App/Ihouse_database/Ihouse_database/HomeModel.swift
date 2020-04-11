//
//  HomeModel.swift
//  Ihouse_database
//
//  Created by Braulio Cald on 7/31/19.
//  Copyright © 2019 Braulio Cald. All rights reserved.
//

import UIKit

protocol  HomeConnectDelegate {
    func itemsdownloaded(locations:[Location])
}


class HomeModel: NSObject {
    
    var delegate: HomeConnectDelegate?
    let serviceUrl = "https://braucalderon.com/service.php"
    
    func downloadInfo() {
        
        // connect web service url
        let Url = URL(string: serviceUrl)
        if let Url = Url {
            _ = URLSession(configuration: URLSessionConfiguration.default)
            
            let task = URLSession.shared.dataTask(with: Url) { (data, response, error) in
                if error != nil {
                    print("Failed to download")
                }else{
                    self.parseJason(data!)
                    print("Data Downloaded")
                    }
            }
            task.resume()
            
            
            
//            let task = session.dataTask(with: Url)
//            {(data, responce, error) in
//                if error != nil {
//                    print("Failed to download data")
//
//                }else{
//                    print("Data downloaded")
//                    self.parseJason(data!)
//                }
//
//            }
//            // resume the task
//            task.resume()
        }
    }
    func parseJason(_ data: Data){
        var locArray = [Location]()
        
        do{
            let jsonArray = try JSONSerialization.jsonObject(with: data, options: []) as! [Any]
            
            
            
            for jsonResult in jsonArray{
                
                let jsonDic = jsonResult as! [String:String]
                
                let loc = Location(firstname: jsonDic["firstname"]!, lastname: jsonDic["lastname"]!, room: jsonDic["room"]!, freenights: jsonDic["freenights"]!, paidnights: jsonDic["paidnights"]!, totalnights: jsonDic["totalnights"]!)
                
                
                locArray.append(loc)
            }
            DispatchQueue.main.async {
                self.delegate?.itemsdownloaded(locations: locArray)
            }
           
            
            
        } catch{
            print ("There was an error")
        }
    }
    
} // end class
