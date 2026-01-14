#welcome to hotel sangrila, located in the serene beauty of the himalayas , thsi is astheticlally most pleasing hotel
#today we are going to be designing the room booking system of the hotel

#so how our classes are going to be structured , first we are going to have a class hotel 


#now we build the front end of the rooms
from hotels import Hotel
from datetime import datetime

def main():
    x='*' * 10
    print(f'{x} welcome to the hotel management system. Please choose a option {x} \n')
    hm=Hotel('Sangrila')
    flag=True
    while flag:
        print('\n1. Add rooms \n')
        print('2. List all rooms \n')
        print('3. Book a room \n')
        print('4. Check out room \n')
        print('5. Delete Room \n')
        print('6. Search Room by type (Standard/Deluxe/Suite): \n')
        print('7. Search Room by Price Range: \n')
        print('8. View Room Bookings \n')
        print('9. Exit')
        
        try:
            choice=int(input("enter your choice: "))
        except ValueError:
            print('Please enter a valid number')
            continue
            
        if choice==1:
            room_num=int(input("enter the room number you want to add: "))
            rtype=input('enter the type of the room (standard/deluxe/suite):  ')
            hm.add_rooms(room_num,rtype)
        elif choice==2:
            hm.list_rooms()
        elif choice==3:
            num=int(input('enter the room number you want to book: \n'))
            gname=input('enter the guest name who want to book the room: \n')
            print('Date format: YYYY-MM-DD (e.g., 2026-01-15)')
            indate=input('enter the check in date: ')
            outdate=input('enter the checkout date: ')
            hm.book_rooms(num,gname,indate,outdate)
        elif choice==4:
            num2=int(input('enter the room number you want to check out: \n'))
            hm.check_out(num2)
        elif choice==5:
            num3=int(input('enter the room number you want to delete: \n'))
            hm.delete_rooms(num3)
        elif choice==6:
            x=input("enter the type of room you want to search: \n")
            hm.search_room_by_type(x)
        elif choice==7:
            min1=int(input('enter the minimum price of the room: \n'))
            max1=int(input('the maximum price of the room \n'))
            hm.search_by_price_range(min1,max1)
        elif choice==8:
            num4=int(input('enter the room number to view bookings: \n'))
            hm.view_room_bookings(num4)
        elif choice==9: 
            flag=False
        else:
            print('please enter a valid option')
            continue
if __name__ == '__main__':
    main()