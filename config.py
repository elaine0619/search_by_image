import os


config = { 
	'BROWSER': 'Chrome', # Chrome, Firefox, or IE
	'SEARCH_ENGINE': 'https://www.baidu.com',
	'PICTURE_NAME': 'SpongeBob.jpg',
	'VISIT_RESULT': 1,
	'LAST_SCREENSHOT': 'screenshot.png',
	'VALIDATE_STRINGS': ["海绵宝宝"],
	'LOG_NAME': 'search.log'
}

config['PICTURE_PATH'] = os.path.join(os.getcwd(), config['PICTURE_NAME'])
config['SCREENSHOT_PATH'] = os.path.join(os.getcwd(), config['LAST_SCREENSHOT'])
