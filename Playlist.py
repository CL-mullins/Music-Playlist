from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    #creates a song method
    new_song = Song(title)
    #set the new song to the first song
    new_song.next = self.__first_song
    self.__first_song = new_song
    #set the new head to the new first song


  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song  = self.__first_song
    counter = 0

    while current_song != None:
      if current_song.get_title() == title:
        return counter
      counter += 1
      current_song = current_song.next 
    return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_node = self.__first_song
    previous = None
    
    #WHere are we searching for the title?
    #seems counter intuitive to be like: since it isn't found, do this
    #when we haven't found it yet.
    while current_node != None:
      if current_node.get_title() != title:
        previous = current_node
        current_node = current_node.next


      if current_node.get_title() == title:
        if previous == None:
          self.__first_song = self.__first_song.next
          return
          print('Song Removed!')
        #If next pointer is pointing to none, we're on the last song
        if current_node.next == None:
          #Remove last song
          previous.set_next_song(None)
          print('Song Removed!')
          return

        previous.next = current_node.next
      return
          


      #setting previousSong.next() = currentSong.next()

    # while not found:
    #   if current_node == title: #If we want to remove the head
    #     current_node = current_node.get_next_song()
    #   else: 
    #     previous = current_node
    #     current_node = current_node.get_next_song()
    #     if found == True:
    #       if previous == None:
    #         self.__first_song = current_node.get_title()
    #       else:
    #         current_node = current_node.get_next_song() #Moving the index over one
    #         previous.set_next_song(current_node.get_next_song())




  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    counter = 0
    current_node =  self.__first_song
    
    while current_node != None:
      counter += 1
      current_node = current_node.next
    return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    counter = 1
    current_song = self.__first_song
    while current_song != None:
      print(f'{counter}. {current_song}')
      counter += 1
      current_song = current_song.next
    pass

  