{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    # @NOTE: Replace the path with your actual path to the chromedriver\n",
    "    executable_path = {\"executable_path\": \"C:/Users/austin.edrington/Desktop/Resources/chromedriver.exe\"}\n",
    "    return Browser(\"chrome\", **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "NASA's Opportunity Rover Mission on Mars Comes to End\n",
      "\n",
      "\n",
      "\n",
      "NASA's Opportunity Mars rover mission is complete after 15 years on Mars. Opportunity's record-breaking exploration laid the groundwork for future missions to the Red Planet.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "url = \"https://mars.nasa.gov/news/\"\n",
    "response = requests.get(url)    \n",
    "\n",
    "soup = bs(response.text, 'html.parser')\n",
    "news_title = soup.find('div',class_='content_title').get_text()\n",
    "news = soup.find('div',class_='rollover_description_inner').get_text()\n",
    "print(news_title)\n",
    "print(news)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "response = requests.get(url)\n",
    "    \n",
    "soup = bs(response.text, 'html.parser')\n",
    "image = soup.find('article', style=\"background-image\")\n",
    "print(image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight sol 80 (2019-02-16), high -16/3F, low -95/-139F, pressure at 7.23hPa, winds from the WNW at 10.7 mph gusting to 32.3 mph'"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://twitter.com/marswxreport?lang=en'\n",
    "response = requests.get(url)\n",
    "\n",
    "soup = bs(response.text, 'html.parser')\n",
    "Tweet = soup.find_all('div', class_='js-tweet-text-container')[1]\n",
    "\n",
    "mars_weather = Tweet.text.strip()\n",
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<table class=\"tablepress tablepress-id-mars\" id=\"tablepress-mars\">\n",
       " <tbody>\n",
       " <tr class=\"row-1 odd\">\n",
       " <td class=\"column-1\"><strong>Equatorial Diameter:</strong></td><td class=\"column-2\">6,792 km<br/>\n",
       " </td>\n",
       " </tr>\n",
       " <tr class=\"row-2 even\">\n",
       " <td class=\"column-1\"><strong>Polar Diameter:</strong></td><td class=\"column-2\">6,752 km<br/>\n",
       " </td>\n",
       " </tr>\n",
       " <tr class=\"row-3 odd\">\n",
       " <td class=\"column-1\"><strong>Mass:</strong></td><td class=\"column-2\">6.42 x 10^23 kg (10.7% Earth)</td>\n",
       " </tr>\n",
       " <tr class=\"row-4 even\">\n",
       " <td class=\"column-1\"><strong>Moons:</strong></td><td class=\"column-2\">2 (<a href=\"https://space-facts.com/phobos/\">Phobos</a> &amp; <a href=\"https://space-facts.com/deimos/\">Deimos</a>)</td>\n",
       " </tr>\n",
       " <tr class=\"row-5 odd\">\n",
       " <td class=\"column-1\"><strong>Orbit Distance:</strong></td><td class=\"column-2\">227,943,824 km (1.52 AU)</td>\n",
       " </tr>\n",
       " <tr class=\"row-6 even\">\n",
       " <td class=\"column-1\"><strong>Orbit Period:</strong></td><td class=\"column-2\">687 days (1.9 years)<br/>\n",
       " </td>\n",
       " </tr>\n",
       " <tr class=\"row-7 odd\">\n",
       " <td class=\"column-1\"><strong>Surface Temperature: </strong></td><td class=\"column-2\">-153 to 20 °C</td>\n",
       " </tr>\n",
       " <tr class=\"row-8 even\">\n",
       " <td class=\"column-1\"><strong>First Record:</strong></td><td class=\"column-2\">2nd millennium BC</td>\n",
       " </tr>\n",
       " <tr class=\"row-9 odd\">\n",
       " <td class=\"column-1\"><strong>Recorded By:</strong></td><td class=\"column-2\">Egyptian astronomers</td>\n",
       " </tr>\n",
       " </tbody>\n",
       " </table>]"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://space-facts.com/mars/'\n",
    "response = requests.get(url)\n",
    "\n",
    "soup = bs(response.text, 'html.parser')\n",
    "table = soup.find_all('table', class_=\"tablepress tablepress-id-mars\")\n",
    "table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
