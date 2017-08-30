import fresh_tomatoes
import media #The class Movie is imported into the file
#Below are three instances or objects
#All variables below is unique to Toy Story and belongs to Toy Story, these are called Instance --> variables
toy_story=media.Movie("Toy Story",
                                 "A story of the boy",
                                 "https://vignette3.wikia.nocookie.net/soundeffects/images/5/51/Toy_Story_Poster.png/revision/latest?cb=20150824001525",
                                 "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
#All variables below is unique to bossbby and belongs to bossbaby, these are called Instance --> variables
bossbaby=media.Movie("Bossbaby",
                                  "Boss baby story",
                                  "https://i.ytimg.com/vi/aku0GPFLb3k/maxresdefault.jpg",
                                  "https://www.youtube.com/watch?v=O2Bsw3lrhvs")
#All variables below is unique to vivegam and belongs to vivegam, these are called Instance --> variables
vivegam=media.Movie("vivegam ",
                                  "The Ultimate Movie",
                                  "http://www.ssmusic.tv/wp-content/uploads/2017/02/Screen-Shot-2017-02-27-at-3.06.42-AM.jpg",
                                  "https://www.youtube.com/watch?v=yJdHR8nCYWk")
#All variables below is unique to bahubali2 and belongs to bahubali2, these are called Instance --> variables
bahubali2=media.Movie ("Bahubali2 ",
                                        " The ultimate hit",
                                        "https://www.filmiwiki.com/wp-content/uploads/2017/03/16-Baahubali-2-1.jpg ",
                                        "https://www.youtube.com/watch?v=94BzBOpv42g")
#All variables below is unique to bahubali2 and belongs to bahubali2, these are called Instance --> variables
student_of_the_year=media.Movie("Student of the year ",
                                        "The college student story",
                                        "http://wallpapers.filmibeat.com/ph-1024x768/2012/11/135418816317328.jpg",
                                        "https://www.youtube.com/watch?v=94BzBOpv42g")
movies=[toy_story,bossbaby,vivegam,bahubali2,student_of_the_year]
fresh_tomatoes.open_movies_page(movies)                              
                                 
