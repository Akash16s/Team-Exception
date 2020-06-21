import io, os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"exception-280906-1778b525b949.json"
client = vision.ImageAnnotatorClient()

filename = 'explicit_img.jpg'

with io.open (filename, 'rb') as f:
    content = f.read()

image = vision.types.Image(content=content)
response = client.safe_search_detection(image=image)

safe_search = response.safe_search_annotation

likelihood = ['Unknown', 'Very Unlikely', 'Unlikely', 'Possibly', 'Likely', 'Very Likely']

print('EXPLICIT CONTENT DETECTION: ')
print('adult: {0}'.format(likelihood[safe_search.adult]))
print('spoof: {0}'.format(likelihood[safe_search.spoof]))
print('medical: {0}'.format(likelihood[safe_search.medical]))
print('violence: {0}'.format(likelihood[safe_search.violence]))
print('racy: {0}'.format(likelihood[safe_search.racy]))

