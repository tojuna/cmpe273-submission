# Read Me: 

## **1.** Shorten URL: 

*curl -X POST -d "https://www.facebook.com/" -H "Content-Type: text/plain" http://127.0.0.1:5000/shorten*

**Output:** New URL created: 127.0.0.1:5000/CvlqF

## **2.** Click on the newly generated link: http://127.0.0.1:5000/CvlqF .

If we put this link in the browser we are redirected to long url website. Number of clicks increase for this short URL whenever you visit this link.

*curl http://127.0.0.1:5000/CvlqF*                            

<!-- **Output:** <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="https://www.facebook.com/">https://www.facebook.com/</a>. If not click the link. -->

**3.** Find clicks for the shortened link '127.0.0.1:5000/CvlqF': 

*curl http://127.0.0.1:5000/clicks/127.0.0.1:5000/CvlqF*       

**Output:** Number of clicks on this shortened link: 1

**4.** Retrieve long URL for given short URL '127.0.0.1:5000/CvlqF':

*curl http://127.0.0.1:5000/retrieve/127.0.0.1:5000/CvlqF*     

**Output:** Long URL for given short url: https://www.facebook.com/

**5.** Update clicks for the given short link using update PATCH:

*curl -X PATCH -d '{"clicks": 5}' -H "Content-Type: application/json" http://127.0.0.1:5000/update/127.0.0.1:5000/CvlqF*

**Output:** Updated count for given short link to: 5
