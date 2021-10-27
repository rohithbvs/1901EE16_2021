import os
import re


def Lucifer(webseries_name, season_padding, episode_padding):
    '''we are checking if we have the correct_srt folder if not we are making the new one'''
    folder1 = "correct_srt"
    if not os.path.exists(folder1):
        os.makedirs(folder1)

    '''we are converting into int type so that we cant use in zfill() function'''
    season_pad = int(season_padding)
    episode_pad = int(episode_padding)

    '''we are deriving all required paths which are going to be useful'''
    basepath = "./wrong_srt"
    destination_dir = os.path.join(os.getcwd(), "correct_srt", webseries_name)
    dest = os.path.join(os.getcwd(), "correct_srt")
    folder_path = os.path.join(basepath, webseries_name)
    files = os.listdir(folder_path)

    '''we are extracting one by one file from files and doing required operations'''
    for file in files:
        '''the following pattern is writtien by some groups which are useful for extracting given information'''
        pattern = re.compile(r'([a-zA-Z]+)\s-\s([a-z0-9]+)\s-\s([a-zA-Z\s\']+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z0-9]+)')
        found = re.match(pattern, str(file))

        series_name =found.group(1)
        season_num = found.group(2)
        episode_name = found.group(3)

        '''this pattern2 is extracting season number and episode number from title'''
        pattern2 = re.compile(r'([0-9]+)x([0-9]+)')
        found2 = re.match(pattern2,season_num)
        episode_num = found2.group(2)
        season_num = found2.group(1)
        extention = str(found.group(7))

        '''these 2 if cases take care of base case when episode padding or season padding is 1'''
        if (season_pad==1 and len(season_num)==2):
            if(season_num[0]=='0'):
                season_num = season_num[1]
        if (episode_pad==1 and len(episode_num)==2):
            if(episode_num[0]=='0'):
                episode_num = episode_num[1]
        '''the final_name stores the final file name after performing required actions '''
        final_name = series_name + " - " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(
            episode_pad) + " - " + episode_name + "." + extention

        '''this piece of code is useful for dropping files in required location '''
        des = os.path.join(destination_dir, final_name)
        if not os.path.isdir(destination_dir):
            os.chdir(dest)
            os.mkdir("Lucifer")

        if not os.path.isfile(des):
            os.chdir(destination_dir)
            with open(final_name, 'w') as file:
                pass

    return



def Gameofthrones(webseries_name, season_padding, episode_padding):
    '''we are checking if we have the correct_srt folder if not we are making the new one'''
    folder1 = "correct_srt"
    if not os.path.exists(folder1):
        os.makedirs(folder1)

    '''we are converting into int type so that we cant use in zfill() function'''
    season_pad = int(season_padding)
    episode_pad = int(episode_padding)

    '''we are deriving all required paths which are going to be useful'''
    basepath = "./wrong_srt"
    destination_dir = os.path.join(os.getcwd(), "correct_srt", webseries_name)
    dest = os.path.join(os.getcwd(), "correct_srt")
    folder_path = os.path.join(basepath, webseries_name)
    files = os.listdir(folder_path)

    '''we are extracting one by one file from files and doing required operations'''
    for file in files:
        '''the following pattern is writtien by some groups which are useful for extracting given information'''
        pattern = re.compile(r'([a-zA-Z\s]+)-\s([a-z0-9]+)\s-\s([a-zA-Z\s\']+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z0-9]+)')
        found = re.match(pattern, str(file))

        series_name = found.group(1)
        season_num = found.group(2)
        episode_name = found.group(3)

        '''this pattern2 is extracting season number and episode number from title'''
        pattern2 = re.compile(r'([0-9]+)x([0-9]+)')
        found2 = re.match(pattern2, season_num)
        episode_num = found2.group(2)
        season_num = found2.group(1)
        extention =  str(found.group(8))

        '''these 2 if cases take care of base case when episode padding or season padding is 1'''
        if (season_pad==1 and len(season_num)==2):
            if(season_num[0]=='0'):
                season_num = season_num[1]
        if (episode_pad==1 and len(episode_num)==2):
            if(episode_num[0]=='0'):
                episode_num = episode_num[1]
        '''the final_name stores the final file name after performing required actions '''
        final_name = series_name + "- " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(
            episode_pad) + " - " + episode_name + "." + extention

        '''this piece of code is useful for dropping files in required location '''
        des = os.path.join(destination_dir, final_name)
        if not os.path.isdir(destination_dir):
            os.chdir(dest)
            os.mkdir("Game of Thrones")
        if not os.path.isfile(des):
            os.chdir(destination_dir)
            with open(final_name, 'w') as file:
                pass

    return


def Breaking_bad(webseries_name, season_padding, episode_padding):
    '''we are checking if we have the correct_srt folder if not we are making the new one'''
    folder1 = "correct_srt"
    if not os.path.exists(folder1):
        os.makedirs(folder1)

    '''we are converting into int type so that we cant use in zfill() function'''
    season_pad = int(season_padding)
    episode_pad = int(episode_padding)

    '''we are deriving all required paths which are going to be useful'''
    basepath = "./wrong_srt"
    destination_dir = os.path.join(os.getcwd(), "correct_srt", webseries_name)
    dest = os.path.join(os.getcwd(), "correct_srt")
    folder_path = os.path.join(basepath, webseries_name)
    files = os.listdir(folder_path)

    '''we are extracting one by one file from files and doing required operations'''
    for file in files:
        '''the following pattern is writtien by some groups which are useful for extracting given information'''
        pattern = re.compile(r'([a-zA-Z\s]+)([a-z0-9]+)\s([a-z0-9]+).([a-zA-Z]+).([a-zA-Z]+).([a-zA-Z0-9]+)')
        found = re.match(pattern, str(file))
        series_name = "Breaking Bad"
        season_num = found.group(2)

        '''this pattern2 is extracting season number and episode number from title'''
        pattern2 = re.compile(r'([0-9]+)e([0-9]+)')
        found2 = re.match(pattern2, season_num)
        episode_num = found2.group(2)
        season_num = found2.group(1)
        extention = str(found.group(6))

        '''these 2 if cases take care of base case when episode padding or season padding is 1'''
        if (season_pad==1 and len(season_num)==2):
            if(season_num[0]=='0'):
                season_num = season_num[1]
        if (episode_pad==1 and len(episode_num)==2):
            if(episode_num[0]=='0'):
                episode_num = episode_num[1]
        '''the final_name stores the final file name after performing required actions '''
        final_name = series_name + " - " + "Season " + season_num.zfill(season_pad) + " Episode " + episode_num.zfill(
            episode_pad) +"." + extention

        '''this piece of code is useful for dropping files in required location '''
        des = os.path.join(destination_dir, final_name)
        if not os.path.isdir(destination_dir):
            os.chdir(dest)
            os.mkdir("Breaking Bad")
        if not os.path.isfile(des):
            os.chdir(destination_dir)
            with open(final_name, 'w') as file:
                pass

    return


def regex_renamer():
    # Taking input from the user
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")

    webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
    season_padding = int(input("Enter the Season Number Padding: "))
    episode_padding = int(input("Enter the Episode Number Padding: "))

    if webseries_num == 1:

        Breaking_bad('Breaking Bad', season_padding, episode_padding)

    elif webseries_num == 2:

        Gameofthrones('Game of Thrones', season_padding, episode_padding)

    elif webseries_num == 3:

        Lucifer('Lucifer', season_padding, episode_padding)

    return


regex_renamer()