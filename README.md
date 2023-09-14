# search_by_image

Here already attched a picture for testing. 
You can change the test picture by replacing the value of 'PICTURE_NAME' in config.py with yours, and place your picture at the same place as the codes.
The screenshot would be saved at same place, which you can change its name in config.py too, the default name is 'screenshot.png'.

For validating if the selected result page is related to the search picture, I suppose we need to provide the infomation for validation. 
The validation info is kept by 'VALIDATE_STRINGS' in config.py. The values would be used for searching in the selected result page, if the searching result is not null, we consider the validation result is related, otherwise it is not related.

You could also find log file, which named as search.log. Its name can be changed in config.py.
