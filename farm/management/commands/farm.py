import threading
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
import os.path

users = [ ["dougc93@hotmail.com", "berryking2"], ["candysmith5@live.com", "jimmyeatworld1"], ["penelopesweet88@live.com","jimmyeatworld1"], ["dalecarnegie1@live.com","jimmyeatworld1"],
		["vannianoubis@live.com","bigapple3"]]
cookies = []
words = []
pointList = []
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

class Command(BaseCommand):
	def handle(self, *args, **options):
		main()

class farmThread(threading.Thread):
	def __init__(self, counter):
		threading.Thread.__init__(self)
		self.driver = webdriver.PhantomJS()
		self.counter = counter
	def run(self):
		login(self.driver, users[self.counter][0], users[self.counter][1])
		search(self.driver)
		clickRewardLinks(self.driver)
		checkPoints(self.driver, users[self.counter][0])
		self.driver.close()

def main():
	readDictionary()
	farmers = []
	# initiate threads
	for i in range(len(users)):
		farmers.append(farmThread(i))
	# run threads
	for i in range(len(users)):
		farmers[i].start()
	# synchronize
	for farmer in farmers:
		farmer.join()
	for number in pointList:
		print number
	# thread = farmThread(0)
	# thread.start()


# login to a user
def login(driver, username, password):
	driver.get("http://hotmail.com")
	cookies.append(driver.get_cookies())
	user = driver.find_element_by_name("login")
	user.send_keys(username)
	pw = driver.find_element_by_name("passwd")
	pw.send_keys(password)
	pw.submit()
	print driver.title + ": " + str(username)
	driver.get("http://bing.com")
	# wait for cookie
	time.sleep(10)
	print username + " successfully logged in"

# check we're on the bing website
def bingCheck(driver):
	# should output an error here
	if "Bing" not in driver.title:
		print "NOT ON BING"
		driver.close()

# perform searches for win
def search(driver):
	counter = 0;
	for i in range(30):
		word = words[random.randint(0, len(words)-1)]
		driver.get("http://bing.com")
		time.sleep(3)
		searchBar = driver.find_element_by_name("q")
		searchBar.clear()
		searchBar.send_keys(word, Keys.ENTER)
		

# everyday there are some random links for points. click em
def clickRewardLinks(driver):
	driver.get("http://www.bing.com/rewards/dashboard")
	parent_handle = driver.current_window_handle	
	blocks = driver.find_elements_by_class_name("tile")
	for i in range(len(driver.find_elements_by_class_name("tile"))):
		links = driver.find_elements_by_class_name("tile")
		links[i].click()
		driver.switch_to_window(driver.window_handles[-1])
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		time.sleep(2)

# acquire dictionary for search
def readDictionary():
	f = open(PROJECT_ROOT + '/farm/management/commands/words.txt', 'r')
	for line in f:
		words.append(' '.join(line.split()))

def checkPoints(driver, name):
	driver.get("http://www.bing.com/rewards/dashboard")
	time.sleep(3)
	points = driver.find_element_by_class_name("data-value-text")
	pointList.append(name + ":    \t" + points.text)

if __name__ == "__main__":
	main()


