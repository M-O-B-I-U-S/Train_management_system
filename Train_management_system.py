import json

def main_menu():
    while True:
        print("\n.....MAIN MENU.....\n")
        print("\n 1. Admin\n 2. Enquiry\n 3. Reservation\n 4. Search The Train\n 5. Booking Information\n 6. Exit\n\n......................\n")
        choice=int(input("Enter your choice : "))

        if choice==1:
            print("Admin Control Panel")
    

        elif choice==2:
            print("\n....Enquiry....\n")
            print("\n 1. Train Enquiry\n 2. Train Services\n 3. Help\n 4. Back to the main menu\n\n.................")
            ch=int(input("Enter your choice :"))
            if ch==1:
                print("Enquiry of the train")
            elif ch==2:
                print("Services of the train")
            elif ch==3:
                while True:
                    print("\n....Help....\n")
                    print("\n 1. Admin\n 2. Enquiry\n 3. Reservation\n 4. Search The Train\n 5. Booking Information\n 6. Instructions\n 7. Back to the main menu \n\n......................\n")
                    opt = int(input("Enter your choice :"))
                    #read json file
                    f = open('info.json','r')  
                    data = json.load(f)
                    if opt == 1:
                        print(data['admin'])
                    elif opt == 2:
                        print(data['enquiry'])
                    elif opt == 3:
                        print(data['Reservation'])
                    elif opt == 4:
                        print(data['Search the train'])
                    elif opt == 5:
                        print(data['Booking Information'])
                    elif opt == 6:
                        print(data['Instructions'])
                    elif opt == 7:
                        break
                    else:
                        print("Invalid choice")
                        
                   
                    
            elif ch==4:
                continue
            else:
                print("Invalid choice")

        elif choice==3:
            print("\n.....Reservation.....\n")
            print("\n 1. Reserve the seat\n 2. Cancel Reservation\n 3. Waiting List\n 4. Back to main menu\n\n......................\n")
            ch = int(input("Enter your choice : "))
            if ch == 1:
                print("Reserve_seat function")

            elif ch == 2:
                print("Cancel_reservation function")

            elif ch == 3:
                print("Waiting_list function")

            elif ch == 4:
                continue

            else:
                print("Invalid choice")

        elif choice==4:
            print("Search the Train")

        elif choice==5:
            print("Booking Information")

        elif choice==6:
            exit()

        else:
            print("Invalid choice")
main_menu()        