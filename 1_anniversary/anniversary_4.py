from datetime import datetime, timedelta
import emoji

plus_days = 2000
wedding_day = datetime(2017, 7, 22)
the_day = wedding_day + timedelta(days=plus_days) 
result = emoji.emojize(f":ring: 우리 결혼한지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일")
print(result)
result1 = emoji.emojize("😀")

result1 = emoji.emojize(':thumbs_up:')
print(result1)
print(emoji.emojize(':thumbs_down:'))
print(emoji.emojize(':deaf_woman:'), fg='red')
	



# pip install emoji
# http://unicode.org/emoji/charts/full-emoji-list.html