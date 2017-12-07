
# created by Injung Lily Kim
# last modified date: 12/5/2017
# contact: ink20@pitt.edu
#
from PIL import Image
import httplib, urllib, base64, json, io

# Image urls to analyze (body of the request)
bodys = ['{\'URL\': \'http://lifepopper.com/wp-content/uploads/2016/01/World-smile-day-lifepopper-positive-thought-of-the-day-motivational-quotes-words-of-wisdom-happy-smiley-face-4.png\'}',
          '{\'URL\': \'https://i.pinimg.com/474x/27/30/37/273037f28dc31933b9c79c6dc15714f8--gentle-parenting-parenting-tips.jpg\'}',
          '{\'URL\': \'https://s-i.huffpost.com/gen/2184140/images/n-RAGE-628x314.jpg\'}',
         '{\'URL\': \'https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/6/000/2ae/35a/04e1d06.jpg\'}']

urls = ["http://lifepopper.com/wp-content/uploads/2016/01/World-smile-day-lifepopper-positive-thought-of-the-day-motivational-quotes-words-of-wisdom-happy-smiley-face-4.png",
          "https://i.pinimg.com/474x/27/30/37/273037f28dc31933b9c79c6dc15714f8--gentle-parenting-parenting-tips.jpg",
          "https://s-i.huffpost.com/gen/2184140/images/n-RAGE-628x314.jpg",
          "https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/6/000/2ae/35a/04e1d06.jpg"]

# API request for Emotion Detection
headers = {'Content-type': 'application/json',}

params = urllib.urlencode({
   'subscription-key': 'c38328fe488648e6904c03eb5b56baa7',  # Enter EMOTION API key
})

for i in range(0,4):
   try:
      conn = httplib.HTTPSConnection('api.projectoxford.ai')
      conn.request("POST", "/emotion/v1.0/recognize?%s" % params, bodys[i], headers)
      response = conn.getresponse()
      print("########################################")

      fd = urllib.urlopen(urls[i])
      image_file = io.BytesIO(fd.read())
      im = Image.open(image_file)

      data = response.read()
      parseddata = json.loads(data)
      print(json.dumps(parseddata, indent=4, sort_keys=True))
      conn.close()

      im.show()

   except Exception as e:
      print("[Errno {0}] {1}".format(e.errno, e.strerror))