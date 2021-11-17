publisher_list = [
    {'id': 1, 'name': 'ABC', 'website': 'www.abcdefg.com', 'email': 'abc@naver.com'},
    {'id': 2, 'name': 'hanbit', 'website': 'www.h.com', 'email': 'h@naver.com'},
    {'id': 3, 'name': 'info', 'website': 'http://www.info.com', 'email': 'info@naver.com'},
    {'id': 4, 'name': 'good', 'website': 'http://www.good.com', 'email': 'good@naver.com'}
]

for publisher in publisher_list:
    print(publisher.get('id'), publisher.get('name'),
          publisher.get('website'), publisher.get('email'))
