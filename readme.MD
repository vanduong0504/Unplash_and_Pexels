<h1 align="center">  Image crawler with Pexels and Unsplash </h1>

<h2> :pencil: About the project </h2>

This project is using API from [*Pexels*](https://www.pexels.com/) and [*Unsplash*](https://unsplash.com/) to crawl 
images. You need to get your **API key** from website to be able to crawl the data.

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2> :scroll: Usage </h2>
<ul>
<li> First you need to install some helpful packages:</li>
    
`pip install requirements.txt`

<li> Then run main.py file for image scarping: </li>

`python main.py --web unsplash --key Your-API-KEY --q vietnam --remove 1`

<li> Using merge.py if you want to merge your image folders: </li>

`python merge.py PATH-TO-FOLDER1 PATH-TO-FOLDER2 ... OUTPUT`


</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
<h2> :dart: Note </h2>

Don't use ***quotes*** for any argument on the terminal command line. This will have an error.