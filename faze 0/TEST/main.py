import fileinput
import sys
import json

#key is ID and value is line
FilmIndex = {}
ArtistIndex = {}

def add_film (FilmID, FilmName, DirectorName, ProductionYear, Genre):
    is_exist = False
    id_check = False

    curr_film = open("Film.txt", "r")
    current_line = 0
    for i in curr_film:
        #check if exist
        if FilmID+'/'+FilmName+'/'+DirectorName+'/'+ProductionYear+'/'+Genre in i:
            is_exist = True
        #check id
        s_index = i.find(' ')
        e_index = i.find('/')
        if FilmID == i[s_index+1:e_index:]:
            id_check = True

        current_line += 1
    curr_film.close

    if is_exist:
        return "Error: This record exist in DataBase!"
    
    elif id_check:
        return "Error: Use an other FilmeID, this ID exist in DataBase!"
    
    else:
        line_number = str(current_line)
        append_film = open("Film.txt", "a")
        append_film.write(line_number +' '+FilmID+'/'+FilmName+'/'+DirectorName+'/'+ProductionYear+'/'+Genre+'\n')
        append_film.close()

        #indexing
        FilmIndex[FilmID] = line_number

        return "Record Added Successfully!"

def add_artist(ArtistID, ArtistName, Age, ArtistFilms):
    is_exist = False
    id_check = False
    films_exist = False
    
    #check if the film exist
    film = open("Film.txt", "r")
    artist_films = ArtistFilms.split(',')
    for i in film:
        record = i.split('/')
        if record[1] in artist_films:
            artist_films.remove(record[1])

    if len(artist_films) == 0:
        films_exist = True
    film.close
    
    if films_exist:

        curr_artist = open("Artist.txt", "r")
        current_line = 0
        for i in curr_artist:
            #check if exist
            if ArtistID+'/'+ArtistName+'/'+Age+'/'+ArtistFilms in i:
                is_exist = True
            #check id
            s_index = i.find(' ')
            e_index = i.find('/')
            if ArtistID == i[s_index+1:e_index:]:
                id_check = True

            current_line += 1
        curr_artist.close

        if is_exist:
            return "Error: This record exist in DataBase!"
        
        elif id_check:
            return "Error: Use another ArtistID, this ID exist in DataBase!"
        
        else:
            line_number = str(current_line)
            append_artist = open("Artist.txt", "a")
            append_artist.write(line_number +' '+ArtistID+'/'+ArtistName+'/'+Age+'/'+ArtistFilms+'\n')
            append_artist.close()

            #indexing
            ArtistIndex[ArtistID] = line_number

            return "Record Added Successfully!"
    else:
        return "Films you have entered do not exist i Film DataBase!"

def find(find_type, id_name, value):
    #finding film
    if find_type == "Film":
        #find by id
        if id_name == "FilmID":
            try:
                line_number = int(FilmIndex[value])

                res = ""

                film = open("Film.txt", "r")
                for i, line in enumerate(film):
                    if i == line_number:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        res = line                    
                film.close()

                if res == "":
                    return "Record not fund!!"
                else:
                    return res

            except:
                return "Record not fund!!"

        #find by name
        elif id_name == "FilmName":

            res = ""

            film = open("Film.txt", "r")
            for i in film:
                try:
                    s_index = i.find(" ")
                    reco = i[s_index::]
                    a_name = reco.split('/')[1]
                    if value in a_name:
                        res = reco  
                except:
                    continue

            film.close()

            if res == "":
                return "Record not fund!!"
            else:
                return res
    
    ##finding artist
    elif find_type == "Artist":
        #find by id
        if id_name == "ArtistID":
            try:
                line_number = int(ArtistIndex[value])

                res = ""

                artist = open("Artist.txt", "r")
                for i, line in enumerate(artist):
                    if i == line_number:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        res = temp                    
                artist.close()

                if res == "":
                    return "Record not fund!!"
                else:
                    return res

            except:
                return "Record not fund!!"

        #find by name
        elif id_name == "ArtistName":
            res = ""

            artist = open("Artist.txt", "r")
            for i in artist:
                try:
                    s_index = i.find(" ")
                    reco = i[s_index::]
                    a_name = reco.split('/')[1]
                    if value in a_name:
                        res = reco  
                except:
                    continue
                                  
            artist.close()

            if res == "":
                return "Record not fund!!"
            else:
                return res

def remove_film(ID):
    try:
        line_number = int(FilmIndex[ID])

        for i, line in enumerate(fileinput.input("Film.txt", inplace=1)):
            if i == line_number:
                temp = line
                line = line.replace(temp, str(i)+' '+'\n')
            sys.stdout.write(line)

        del FilmIndex[ID]

        return "Record removed!"

    except:
        return "Record not fund!!"


def remove_artist(ID):
    try:
        line_number = int(ArtistIndex[ID])

        for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
            if i == line_number:
                temp = line
                line = line.replace(temp, str(i)+' '+'\n')
            sys.stdout.write(line)

        del ArtistIndex[ID]

        return "Record removed!"
        
    except:
        return "Record not fund!!"

def update_id(Update_type, ID, field, value):
    #Update for Artist
    if Update_type == "Artist":
        culomn = 0
        if field == "ArtistName":
            culomn = 1
        elif field == "ArtistID":
            culomn = 0
        elif field == "Age":
            culomn = 2 

        try:
            line_number = int(ArtistIndex[ID])

            if culomn == 0:
                try:
                    new_id_check = ArtistIndex[value]
                    return "new id exist in database, use another id!!"

                except:
                    for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                        if i == line_number:
                            s_index = line.find(" ")
                            temp = line[s_index::]
                            old_fields = line[s_index::]
                            old_val = old_fields.split('/')[culomn]
                            line = line.replace(old_val, value)
                        sys.stdout.write(line)

                    del ArtistIndex[ID]
                    ArtistIndex[value] = line_number

                    return "Record Updated!"
            else:

                for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                    if i == line_number:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        old_fields = line[s_index::]
                        old_val = old_fields.split('/')[culomn]
                        line = line.replace(old_val, value)
                    sys.stdout.write(line)

                return "Record Updated!"
        
        except:
            return "Record not fund!!"
        

    #Update for film
    elif Update_type == "Film":
        culomn = 0
        if field == "FilmName":
            culomn = 1
        elif field == "FilmID":
            culomn = 0

        try:
            line_number = int(FilmIndex[ID])

            old_val = ""

            if culomn == 0:
                try:
                    new_id_check = FilmIndex[value]
                    return "new id exist in database, use another id!!"

                except:

                    for i, line in enumerate(fileinput.input("Film.txt", inplace=1)):
                        if i == line_number:
                            s_index = line.find(" ")
                            temp = line[s_index::]
                            old_fields = line[s_index::]
                            old_val = old_fields.split('/')[culomn]
                            line = line.replace(old_val, value)
                        sys.stdout.write(line)

                    del FilmIndex[ID]
                    FilmIndex[value] = line_number
                    return "Record Updated!"
            
            elif culomn == 1:

                for i, line in enumerate(fileinput.input("Film.txt", inplace=1)):
                    if i == line_number:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        old_fields = line[s_index::]
                        old_val = old_fields.split('/')[culomn]
                        line = line.replace(old_val, value)
                    sys.stdout.write(line)

                for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                    if old_val in line:
                        s_in = line.find(" ")
                        num = line[:s_in:]
                        old_fields = line[s_in::]
                        ls = old_fields.split('/')
                        old_films = ls[3]
                        if(old_val in old_films):
                            temp = old_films
                            new_films = temp.replace(old_val, value)
                            ls[3] = new_films
                            line = num + '/'.join(ls)

                    sys.stdout.write(line)

                return "Record Updated!"
        
        except:
            return "Record not fund!!"


def update_name(Update_type, name, field, value):
    #Update for Artist
    if Update_type == "Artist":
        culomn = 0
        if field == "ArtistName":
            culomn = 1
        elif field == "ArtistID":
            culomn = 0
        elif field == "Age":
            culomn = 2 

        line_number = ""

        check = False

        if culomn == 0:
            try:
                new_id_check = ArtistIndex[value]
                return "new id exist in database, use another id!!"
            except:

                for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                    s_in = line.find(" ")
                    if name == line[s_in::].split('/')[1]:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        line_number = line[:s_index:]
                        old_fields = line[s_index::]
                        old_val = old_fields.split('/')[culomn]
                        line = line.replace(old_val, value)
                    sys.stdout.write(line)

                del ArtistIndex[ID]
                ArtistIndex[value] = line_number

                check = True

        else:

            for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                s_in = line.find(" ")
                if name == line[s_in::].split('/')[1]:
                    s_index = line.find(" ")
                    temp = line[s_index::]
                    line_number = line[:s_index:]
                    old_fields = line[s_index::]
                    old_val = old_fields.split('/')[culomn]
                    line = line.replace(old_val, value)
                sys.stdout.write(line)

            check = True

        if check:
            return "Record Updated!"
        else:
            return "Record not fund!!"
        

    #Update for film
    elif Update_type == "Film":
        culomn = 0
        if field == "FilmName":
            culomn = 1
        elif field == "FilmID":
            culomn = 0

        line_number = ""

        old_val = ""

        check = False

        if culomn == 0:
            try:
                new_id_check = FilmIndex[value]
                return "new id exist in database, use another id!!"
            except:

                for i, line in enumerate(fileinput.input("Film.txt", inplace=1)):
                    s_in = line.find(" ")
                    if name == line[s_in::].split('/')[1]:
                        s_index = line.find(" ")
                        temp = line[s_index::]
                        line_number = line[:s_index:]
                        old_fields = line[s_index::]
                        old_val = old_fields.split('/')[culomn]
                        line = line.replace(old_val, value)
                    sys.stdout.write(line)

                del FilmIndex[ID]
                FilmIndex[value] = line_number

                check =True
        
        elif culomn == 1:

            for i, line in enumerate(fileinput.input("Film.txt", inplace=1)):
                s_in = line.find(" ")
                if name == line[s_in::].split('/')[1]:
                    s_index = line.find(" ")
                    temp = line[s_index::]
                    old_fields = line[s_index::]
                    old_val = old_fields.split('/')[culomn]
                    line = line.replace(old_val, value)
                sys.stdout.write(line)

            for i, line in enumerate(fileinput.input("Artist.txt", inplace=1)):
                if old_val in line:
                    s_in = line.find(" ")
                    num = line[:s_in:]
                    old_fields = line[s_in::]
                    ls = old_fields.split('/')
                    old_films = ls[3]
                    if(old_val in old_films):
                        temp = old_films
                        new_films = temp.replace(old_val, value)
                        ls[3] = new_films
                        line = num + '/'.join(ls)

                sys.stdout.write(line)

                check =True

        if check:
            return "Record Updated!"
        else:
            return "Record not fund!!"

def FilmArtists():
    film = open("Film.txt", "r")
    artist = open("Artist.txt", "r")

    result = ""

    for i in film:
        s_index = i.find(" ")
        slash = i.find("/")
        film_name = i[s_index::].split('/')[1]
        actors = []
        for j in artist:
            try:
                s_in = j.find(" ")
                rec = j[s_in::].split('/')
                if film_name in rec[3]:
                    actors.append(rec[1])
            except:
                continue
        temp = i[slash+1::].find("/")
        result += film_name + "/" + ",".join(actors) + i[slash+1::][temp::] + "\n"
        # print(i[slash+1::])

    return result

def save():
    f = open("temp_film.txt", "w")
    f.write(str(FilmIndex))
    f.close

    a = open("temp_artist.txt", "w")
    a.write(str(ArtistIndex))
    a.close

def read():
    f = open("temp_film.txt", "r")
    temp = f.readline()
    if temp != "" and temp != "{"+"}":
        json_acceptable_string = temp.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        FilmIndex = d
    f.close

    a = open("temp_artist.txt", "r")
    tempi = a.readline()
    if tempi != "" and tempi != "{"+"}":
        json_acceptable_stringi = tempi.replace("'", "\"")
        di = json.loads(json_acceptable_stringi)
        ArtistIndex = di
    a.close

read()
save()
#User Interface for getting queries!
while True:

    save()

    print("\nEnter your command (Add, Find, Remove, Update, FilmArtists):")
    print("To exit the app enter :exit")
    command = input()

    #Add Query
    if command == "Add":
        print("Enter the type of your Add qurey(Film, Artist):")
        add_type = input()

        #here we get the query of adding film
        if add_type == "Film":
            FilmID = input("Enter FilmID: ")
            FilmName = input("Enter FilmName: ")
            DirectorName = input("Enter DirectorName: ")
            ProductionYear = input("Enter ProductionYear: ")
            Genre = input("Enter Genre: ")

            print(add_film(FilmID, FilmName, DirectorName, ProductionYear, Genre))
            continue

        #here we get the query of adding arist
        elif add_type == "Artist":
            ArtistID = input("Enter ArtistID: ")
            ArtistName = input("Enter ArtistName: ")
            Age = input("Enter Age: ")
            ArtistFilms = input("Enter ArtistFilms(don't forget ','!): ")

            print(add_artist(ArtistID, ArtistName, Age, ArtistFilms))
            continue

        #invalid type
        else:
            print("Invalid Type")
            continue

    #Find Query
    elif command == "Find":
        find_type = input("What do you want to find?(Film, Artist): ")

        #finding film
        if find_type == "Film":
        
            #Getting type for search
            id_name = input("How do you want to find film?(FilmID or FilmName): ")

            #Getting the value and printting the result
            if id_name == "FilmID":
                value = input("Enter the FilmID: ")
                print(find(find_type, id_name, value))
                continue

            elif id_name == "FilmName":
                value = input("Enter the FilmName: ")
                print(find(find_type, id_name, value))
                continue

            #Invalid type for search
            else:
                print("Invalid field for search!")
                continue

        #finding artist
        elif find_type == "Artist":
        
            #Getting type for search
            id_name = input("How do you want to find artist?(ArtistID or ArtistName): ")

            #Getting the value and printting the result
            if id_name == "ArtistID":
                value = input("Enter the ArtistID: ")
                print(find(find_type, id_name, value))
                continue

            elif id_name == "ArtistName":
                value = input("Enter the ArtistName: ")
                print(find(find_type, id_name, value))
                continue

            #Invalid type for search
            else:
                print("Invalid field for search!")
                continue

        else:
            print("Invalid find type")
            continue

    #Remove query
    elif command == "Remove":
        remove_type = input("Which one do you what to remove?(Artist or Film): ")

        #Remove Film
        if remove_type == "Film":
            ID = input("Enter Film ID: ")
            print(remove_film(ID))
            continue

        #Remove Artist
        elif remove_type == "Artist":
            ID = input("Enter Artist ID: ")
            print(remove_artist(ID))
            continue

        #Invalid type
        else:
            print("Invalid remove tyepe!")
            continue

    #Update command
    elif command == "Update":

        Update_type = input("What do you want to update?(Artist or Film): ")

        #Update for Artist
        if Update_type == "Artist":

            ID_name = input("Do you want to update with ID or Name: ")

            if ID_name == "ID":
                ID = input("Enter ArtistID: ")

                field = input("Which field of Atrist do you want to update?(ArtistID, ArtistName , Age): ")

                #Check Invalid input for Artist field
                if field != "ArtistID" and field != "ArtistName" and field != "Age":
                    if field == "ArtistFilms":
                        print("You can't update ArtistFilms field!")
                    else:
                        print("Invalid field!")
                    continue

                value = input("Enter the new value: ")

                print(update_id(Update_type, ID, field, value))
                continue

            elif ID_name == "Name":
                name = input("Enter ArtistName: ")

                field = input("Which field of Atrist do you want to update?(ArtistID, ArtistName , Age): ")

                #Check Invalid input for Artist field
                if field != "ArtistID" and field != "ArtistName" and field != "Age":
                    if field == "ArtistFilms":
                        print("You can't update ArtistFilms field!")
                    else:
                        print("Invalid field!")
                    continue

                value = input("Enter the new value: ")

                print(update_name(Update_type, name, field, value))
                continue

            else:
                print("Invalid input!")
                continue

        #Update for film
        elif Update_type == "Film":

            ID_name = input("Do you want to update with ID or Name: ")

            if ID_name == "ID":
                ID = input("Enter Film ID: ")

                field = input("which field of Film do you want to update?(FilmID, FilmName): ")

                #Check Invalid input for Film field
                if field != "FilmID" and field != "FilmName" :
                    print("Invalid field!")
                    continue

                value = input("Enter the new value: ")

                print(update_id(Update_type, ID, field, value))
                continue
            
            elif ID_name == "Name":
                name = input("Enter Film Name: ")

                field = input("which field of Film do you want to update?(FilmID, FilmName): ")

                #Check Invalid input for Film field
                if field != "FilmID" and field != "FilmName" :
                    print("Invalid field!")
                    continue

                value = input("Enter the new value: ")

                print(update_name(Update_type, name, field, value))
                continue

            else:
                print("Invalid input!")
                continue

        #Invalid Entity
        else:
            print("Invalid Entity!")
            continue

    #FilmArtists command
    elif command == "FilmArtists":
        print(FilmArtists())
        continue

    #exit command
    elif command == "exit":
        print("Goodbye, see you soon!!")
        break

    #Invalid command
    else:
        print("Invalid command!")
        continue
