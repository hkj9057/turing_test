import pygame
import time


#key, value
a = {'title': 'a' , 'list_num' : 1, 'location' : '/home/at08/a.mp3', 'like' : 42, 'name' : 'heo gak', 'rangking' : 1}
b = {'title': 'b' , 'list_num' : 11, 'location' : '/home/at08/a.mp3', 'like' : 1001, 'name' : 'heo gak', 'rangking' : 10}
c = {'title': 'c' , 'list_num' : 111, 'location' : '/home/at08/a.mp3', 'like' : 84, 'name' : 'heo gak', 'rangking' : 2}
d = {'title': 'd' , 'list_num' : 1111, 'location' : '/home/at08/a.mp3', 'like' : 1, 'name' : 'heo gak', 'rangking' : 7}
e = {'title': 'e' , 'list_num' : 11111, 'location' : '/home/at08/a.mp3', 'like' : 104, 'name' : 'heo gak', 'rangking' : 4}

music_list = [a,b,c,d,e]
#p = 1이면, 좋아요수, p = 2라면 플레이횟수
p = input()

def like_sort(p,music_list):

    for i in range(len(music_list)):

        for j in range(len(music_list)-1):

            if(music_list[j]['like'] < music_list[j+1]['like']):
                music_list[j],music_list[j+1] = music_list[j+1],music_list[j]


def list_num_sort(p,music_list):

    for i in range(len(music_list)):

        for j in range(len(music_list)-1):

            if(music_list[j]['list_num'] < music_list[j+1]['list_num']):
                music_list[j],music_list[j+1] = music_list[j+1],music_list[j]

def ranking_sort(p,music_list):

    for i in range(len(music_list)):

        for j in range(len(music_list)-1):

            if(music_list[j]['ranking'] < music_list[j+1]['ranking']):
                music_list[j],music_list[j+1] = music_list[j+1],music_list[j]


if (p == 'like'):
    like_sort(p,music_list)
elif(p == 'list_num'):
    list_num_sort(p,music_list)
elif(p == 'ranking'):
    ranking_sort(p,music_list)

print(music_list)

pygame.init()

pygame.mixer.music.load(music_list[0]['location'])

pygame.mixer.music.play()

time.sleep(10)

