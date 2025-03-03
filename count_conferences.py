import requests
import time
import sys

def over16_count_confererence():
    #over 16 session id
    session_id='a3197fe10e5c13dd59eb0efcf7de7464'
    try:
        get_conference_url=f'https://api.pantel.me/a/get_conference_categories?$={session_id}&lang=en'
        load_conference_url=f'https://api.pantel.me/a/load_conferences?$={session_id}&event_type=1'

        chat_room=requests.get(load_conference_url).json().get('result',[])
        print('over 16 years old users:')
        results= requests.get(get_conference_url).json().get('result',[])
        chat_room_num=len(chat_room)
        print('chat room - ',chat_room_num,end=" | ")
        for game in results:
            results_name= game.get('name',{})
            count_rooms= game.get('count',{})
            print( results_name ,' - ', count_rooms, end=" | ")
        print()
    except Exception as e:
        print("error fetching conference api!")

def under16_count_confererence():
    #over 16 session id
    session_id='b828b4eb1cff22dc78f18a487154f8fd'
    try:
        get_conference_url=f'https://api.pantel.me/a/get_conference_categories?$={session_id}&lang=en'
    
        print('under 16 years old users:')
        results= requests.get(get_conference_url).json().get('result',[])
        for game in results:
            results_name= game.get('name',{})
            count_rooms= game.get('count',{})
            print( results_name , ' - ', count_rooms, end=" | ")
        print()
    except Exception as e:
        print('error fetching conference api!')

def main():

    while(True):
        try:
            over16_count_confererence()
            under16_count_confererence()
            time.sleep(15 * 60)  # Wait for 15 minutes
        except KeyboardInterrupt:
            print('running interrupted by user!')

main()