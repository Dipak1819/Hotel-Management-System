#welcome to hotel sangrila, located in the serene beauty of the himalayas , thsi is astheticlally most pleasing hotel
#today we are going to be designing the room booking system of the hotel

#so how our classes are going to be structured , first we are going to have a class hotel 


#now we build the front end of the rooms
from hotels import Hotel

def main():
    x='*' * 10
    print(f'{x} welcome to the hotel management system. Please choose a option {x} \n')
    print('1. Add rooms \n')
    print('2. List all rooms \n')
    print('3. Book a room \n')
    print('4. Check out room \n')
    print('5. exit \n')
    hm=Hotel('Sangrila')
    flag=True
    while flag:
        choice=int(input("enter your choice: "))
        if choice==1:
            room_num=int(input("enter the room number you want to add: "))
            rtype=input('enter the type of the room: ')
            price=int(input('enter the price of the room: '))
            hm.add_rooms(room_num,rtype,price)
        elif choice==2:
            hm.list_rooms()
        elif choice==3:
            num=int(input('enter the room number you want to book: \n'))
            gname=input('enter hte guest name who want to book the room: \n')
            hm.book_rooms(num,gname)
        elif choice==4:
            num2=int(input('enter the room number you want to book: \n'))
            hm.check_out(num2)
        elif choice==5: 
            flag=False
        else:
            print('please enter a valid option')
            continue
if __name__ == '__main__':
    main()
