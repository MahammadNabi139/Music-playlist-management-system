import os

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

def tofile(song):
    with open("playlist.txt", "a") as f1:
        f1.write(song + '\n')

def add_node(first):
    song = input("\n\a\a\a\aEnter Song name: ")
    while first.next:
        first = first.next
    first.next = Node(song)
    first.next.prev = first
    tofile(song)

def add_node_file(first, song):
    while first.next:
        first = first.next
    first.next = Node(song)
    first.next.prev = first

def delete_file(song):
    temp_file = open("temp.txt", "w")
    with open("playlist.txt", "r") as f1:
        for line in f1:
            if song != line.strip():
                temp_file.write(line)
            else:
                x = 1
    temp_file.close()
    os.remove("playlist.txt")
    os.rename("temp.txt", "playlist.txt")
    if x == 0:
        print("There is no song with the name you entered.")
    else:
        print("Song has been deleted.")

def del_node(first):
    while first.next and first.next.next:
        first = first.next
    temp = first.next
    first.next = None
    del temp
    print("Deleted")

def printlist(first):
    print("\nPlaylist Name -")
    while first:
        print(first.song)
        first = first.next

def count_nodes(first):
    i = 0
    while first:
        i += 1
        first = first.next
    print(f"\nTotal songs: {i}")

def del_pos(pointer, pos):
    i = 0
    if pos == 1:
        temp = pointer
        delete_file(temp.song)
        pointer = pointer.next
        pointer.prev = None
        del temp
        print("\nThe list is updated\nUse the display function to check")
        return pointer

    while i < pos - 1:
        prev1 = pointer
        pointer = pointer.next
        i += 1

    if pointer.next is None:
        temp = pointer
        delete_file(temp.song)
        prev1.next.prev = None
        prev1.next = None
        del temp
        print("\nThe list is updated\nUse the display function to check")
    else:
        temp = pointer
        delete_file(temp.song)
        prev1.next = temp.next
        temp.next.prev = prev1
        del temp
        print("\nThe list is updated\nUse the display function to check")

def search1(first):
    song = input("\n\a\a\a\aEnter song to be searched: ")
    flag = 0
    while first:
        if first.song == song:
            print("\n\a\a\a\a#Song Found")
            flag += 1
            break
        first = first.next
    if flag == 0:
        print("\n\a\a\a\a#Song Not found")

def create():
    top = None

def push(data, top):
    if top is None:
        top = Node(data)
    elif top.song != data:
        temp = Node(data)
        temp.next = top
        top = temp

def display(top):
    top1 = top
    if top1 is None:
        print("\n\a\a\a\a=>NO recently played tracks.")
        return
    print("\n\a\a\a\a#Recently played tracks-")
    while top1:
        print(top1.song)
        top1 = top1.next

def play(first, top):
    printlist(first)
    song = input("\n\a\a\a\aChoose song you wish to play: ")
    flag = 0
    while first:
        if first.song == song:
            print(f"\n\a\a\a\a=>Now Playing......{song}")
            flag += 1
            push(song, top)
            break
        first = first.next
    if flag == 0:
        print("\n\a\a\a\a#Song Not found")

def recent(top):
    display(top)

def topelement(top):
    top1 = top
    if top1 is None:
        print("\n\a\a\a\a#NO last played tracks.")
        return
    print(f"\n=>Last Played Song - {top.song}")

def sort(pointer):
    a = b = c = e = tmp = None
    while e != pointer.next:
        c = a = pointer
        b = a.next
        while a != e:
            if a.song > b.song:
                if a == pointer:
                    tmp = b.next
                    b.next = a
                    a.next = tmp
                    pointer = b
                    c = b
                else:
                    tmp = b.next
                    b.next = a
                    a.next = tmp
                    c.next = b
                    c = b
            else:
                c = a
                a = a.next
            b = a.next
            if b == e:
                e = a
    return pointer

def addplaylist(start):
    with open("playlist.txt", "r") as f1:
        for line in f1:
            add_node_file(start, line.strip())
    print("Playlist Added")

def del_search(start):
    printlist(start)
    song = input("\n\a\a\a\aChoose song you wish to delete: ")
    flag = 0
    temp = None
    while start:
        if start.song == song:
            print("\n\a\a\a\a#Song Found")
            temp = start
            delete_file(temp.song)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            del temp
            flag += 1
            break
        start = start.next
    if flag == 0:
        print("\n\a\a\a\a#Song Not found")

def deletemenu(start):
    c = int(input("Which type of delete do you want?\n1. By Search\n2. By Position: "))
    if c == 1:
        del_search(start)
    elif c == 2:
        pos = int(input("\nEnter the pos of the song: "))
        del_pos(start, pos - 1)

def main():
    choice = 0
    loc = 0
    start = Node(input("\t\t\t\a\a\a\a*WELCOME\n\n*Please use '_' for space.\n\nEnter your playlist name: "))
    hold = start
    top = start
    create()

    while choice != 11:
        print("\n1. Add New Song\n2. Delete Song\n3. Display Entered Playlist\n4. Total Songs\n5. Search Song\n6. Play Song\n7. Recently Played Tracks\n8. Last Played Playlist\n9. Sorted playlist\n10. Add From File\n11. Exit")
        choice = int(input("\n\a\a\a\aEnter your choice: "))

        if choice == 1:
            add_node(start)
        elif choice == 2:
            deletemenu(start)
        elif choice == 3:
            printlist(start)
        elif choice == 4:
            count_nodes(hold)
        elif choice == 5:
            search1(start)
        elif choice == 6:
            play(start, top)
        elif choice == 7:
            recent(top)
        elif choice == 8:
            topelement(top)
        elif choice == 9:
            start.next = sort(start.next)
            printlist(start)
        elif choice == 10:
            addplaylist(start)
        elif choice == 11:
            exit(0)

if __name__ == "__main__":
    main()