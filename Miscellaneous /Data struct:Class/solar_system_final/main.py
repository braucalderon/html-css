
from Solar_System import Solar_System
from Planet import Planet
from Sun import Sun
import ast


def main():

    print ("\t\t\t\t ASTRONOMY\n")
    ss = Solar_System('SOLAR SYSTEM', 27000, 1000, 'Proxima Centauri', 4.22,
                     'Alpha Centauri', 4.37, 761642, 'Kuiper cliff', 50, 'Sun')
    print(ss)
    s = Sun('Sun', 432169, 1.989, 5778, 1.4, 0)
    ss.addPlanets(s)

    #__________________________________
    # upload planets from a structure document
    # document is not very user friendly
    # information must be input in the document in the same manner
    # with no more or less than six parameters
    while True:
        try:
            filepath = input('\nEnter the file path to upload: ').lower() + '.txt'
            if filepath not in ' ':
                with open(filepath) as fp:
                    for line in fp:
                        data = line.split()
                        #print(data[0], data[1], data[2], data[3], data[4], data[5])
                        #__________________________________________________________
                        # data is uploaded in the parameters from the document to the
                        # Planet class adding the Planet class into the solar system
                        # class and print each planet
                        #  ast.literal_eval evaluates strings or floats 
                        m = Planet(data[0].upper(), float(data[1]), float(data[2]), float(data[3]), float(data[4]), ast.literal_eval(data[5]))
                        ss.addPlanets(m)
                ss.showPlanets()
                fp.close()
                break
        except FileNotFoundError:
            print('No such file or directory: ', filepath)
    #________________________________________
    # planet's information added for later used in the program
    # and added into the solar system 
    mars = ['Deimos', 'Phobos']
    ma = Planet('Mars', 2106, 141.6, 0.107, 1.9, mars)
    ss.addPlanets(ma)
    
    nept = ['Triton','Proteus','Nereid','Larissa','Galatea','Despina','Thalassa',
            'Naiad','Halimede','Neso','Sao','Laomedeia']
    ne = Planet('Neptune', 15299, 2794000, 17.5, 165, nept)
    ss.addPlanets(ne)
    
    ura = ['Titania','Oberon','Umbriel','Ariel','Miranda','Sycorax','Puck','Portia',
           'Juliet','Caliban','Belinda','Cressida']
    ur = Planet('Uranus', 15759, 178400, 14.54, 84, ura)
    ss.addPlanets(ur)
    
    sat = ['Titan','Rhea','Lapetus','Dione','Tethys','Enceladus','Mimas','Hyperion',
           'Phoebe','Janus','Epimetheus','Prometheus']
    sa = Planet('Saturn', 36184, 890.7, 95.16, 29, sat)
    ss.addPlanets(sa)
    
    jup = ['Ganymede','Callisto','Io','Europa','Amakthea','Himalia','Thebe','Elara','Pasiphae',
           'Metis','Carme','Sinope','Lysithea']
    ju = Planet('Jupiter', 43441, 483.8, 317.8, 12, jup)
    ss.addPlanets(ju)
    
    e = ['Luna']
    er = Planet('Earth', 3959, 92.96, 0.107, 365, e)
    ss.addPlanets(er)
    
    mer = []
    me = Planet('Mercury', 1516, 35.98, 0.058, 88, mer)
    ss.addPlanets(mer)
    
    ven = []
    ve = Planet('Venus', 3760, 67.24, 0.815, 225, ven)
    ss.addPlanets(ven)
 
    #_____________________________
    # Removing Moons Only
    # Remove moons based on information in the planet class added in the main file
    #_____________________________
    
    times = 0
    while True:
        
        print('\nRemove Moons from planets')
        s = input('Input planet, otherwise press enter to skip: ').lower()
        
        if s in ' ':
            break;
        if s == 'uranus':
            u=input('Enter the Moon to remove from the planet: ').title()
            if u not in ' ':
                ur.removeMoon(u)
                print('Moons in ', s.title(), ':\n')
                print(ur.getNumMoons())
                break;
        if s == 'earth':
            u=input('Enter the Moon to remove from the planet: ').title()
            if u not in ' ':
                er.removeMoon(u)
                print('Moons in ', s.title(), ':\n')
                print(er.getNumMoons())
                break;
        if s == 'mars':
            u1=input('Enter the Moon to remove from the planet: ').title()
            if u1 not in ' ':
                ma.removeMoon(u1)
                print('Moons in ', s.title(), ':\n')
                print(ma.getNumMoons())
                break;
        if s == 'saturn':
            u=input('Enter the Moon to remove from the planet: ').title()
            if u not in ' ':
                sa.removeMoon(u)
                print('Moons in ', s.title(), ':\n')
                print(sa.getNumMoons())
                break;
        if s == 'neptune':
            u=input('Enter the Moon to remove from the planet: ').title()
            if u not in ' ':
                ne.removeMoon(u)
                print('Moons in ', s.title(), ':\n')
                print(ne.getNumMoons())
                break;
        if s == 'jupiter':
            u=input('Enter the Moon to remove from the planet: ').title()
            if u not in ' ':
                ju.removeMoon(u)
                print('Moons in ', s.title(), ':\n')
                print(ju.getNumMoons())
                break;               
        p = ['jupiter', 'neptune', 'earth', 'saturn', 'mars', 'uranus']
        n = ['venus', 'mercury']
        if s not in p and s != 'venus' and s != 'mercury':
            times += 1
            print ('\nPlanet', s.title(), ' is not in our the Solar System.')
        if s in n:
            times += 1
            print (s.title(), ' does not have Moons')
        if times  == 2:
            break;

    #____________________________
    # adding only moons to the planets
    # add moons based on the information in the planert class in the main file
    #____________________________
    
    times = 0
    while True:
        print('\nAdd Moons to the planets')
        add = input('Input the planet, otherwise press enter to skip: ').lower()

        if add in ' ':
            break;
        if add == 'uranus':
            u=input('Add Moon: ').title()
            if u not in ' ':
                ur.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(ur.getNumMoons())
                break;
        if add == 'earth':
            u=input('Add Moon: ').title()
            if u not in ' ':
                er.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(er.getNumMoons())
                break;
        if add == 'mars':
            u=input('Add Moon: ').title()
            if u not in ' ':
                ma.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(ma.getNumMoons())
                break;
        if add == 'saturn':
            u=input('Add Moon: ').title()
            if u not in ' ':
                sa.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(sa.getNumMoons())
                break;
        if add == 'neptune':
            u=input('Add Moon: ').title()
            if u not in ' ':
                ne.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(ne.getNumMoons())
                break;
        if add == 'jupiter':
            u=input('Add Moon: ').title()
            if u not in ' ':
                ju.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(ju.getNumMoons())
                break;
        if add == 'venus':
            u=input('Add Moon: ').title()
            if u not in ' ':
                m.addMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(m.getNumMoons())
                break;
        if add == 'mercury':
            u=input('Add Moon: ').title()
            if u not in ' ':
                me.removeMoon(u)
                print('Moon added to ', add.title(), ':\n')
                print(me.getNumMoons())
                break;               
        p = ['jupiter', 'neptune', 'earth', 'saturn', 'mars', 'uranus', 'venus', 'mercury']
        if add not in p:
            times += 1
            print ('\nPlanet ', add.title(), ' is not in our Solar System')
        if times  == 2:
            break
    #_______________________________
    # saves new changes to the file as moons
    # by calling the planet class and saving it into a file with the
    # changes in the planets moons only.
    sav = input('\nPress < y > to create and save a new file: ')
    if sav == 'y':
        save = input('Create file name: ') + '.txt'
        f = open(save,'w')
        f.write(str(Solar_System('SOLAR SYSTEM', 27000, 1000, 'Proxima Centauri', 4.22,
                     'Alpha Centauri', 4.37, 761642, 'Kuiper cliff', 50, 'Sun')))
        f.write(str(Sun('Sun', 432169, 1.989, 5778, 1.4, 0)))
        f.write(str(Planet('Mars', 2106, 141.6, 0.107, 1.9, mars)))
        f.write(str(Planet('Neptune', 15299, 2794000, 17.5, 165, nept)))
        f.write(str(Planet('Uranus', 15759, 178400, 14.54, 84, ura)))
        f.write(str(Planet('Saturn', 36184, 890.7, 95.16, 29, sat)))
        f.write(str(Planet('Jupiter', 43441, 483.8, 317.8, 12, jup)))
        f.write(str(Planet('Mercury', 1516, 35.98, 0.058, 88, mer)))
        f.write(str(Planet('Venus', 3760, 67.24, 0.815, 225, ven)))
        f.write(str(Planet('Earth', 3959, 92.96, 0.107, 365, e)))
        f.close()
        print('File Saved')
    
    ##_______________________________    
    ## Program Issues:
    ## file must be structre very specific for the file to read when uploading info from it
    ## While loop at the file path until a right file is input to upload the planets
    ## If mooon is not on the list, it will return the lists of the moons anyway
    ## it can only change information about the moons
    ## saving a file with the previous name it will overwrite the file
        
    
main()
