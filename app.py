import twilio.twiml
import datetime
import sys
import json
import requests
import praw
import random
import string
from nltk.corpus import stopwords

#deal with words
translator=str.maketrans('','',string.punctuation)
stop = set(stopwords.words('english'))

from flask import Flask, request, redirect, Response, jsonify, render_template
#from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client

app = Flask(__name__)

# put your own credentials here
account_sid = "AC20f7ada53a2d3e4c21d9efcaba259cf7"
auth_token = "dc553ee77c173821f6f534ce7dd505bb"
twilio_num = "+19083605630"

clientID = 'tMDwX9bW48UbFw'
clientSecret = 'WVIX_qRYMi0knQBTBCszYwf_uzY'

client = Client(account_sid, auth_token)

word_counts = {} #{"Hello": 1, "test": 2, "Christmas": 5, "Pizza": 5, "Cya": 3, "Jingle": 4, "Mongo": 1, "Calzone": 3, "Madlyfe": 2}
rec_prompts = [] #["Test", "Test1", "Test2", "Test3", "Test4"]

prompt_len = 0

wp_subreddit = praw.Reddit(client_id=clientID,
				 client_secret=clientSecret,
				 user_agent='testscript').subreddit('WritingPrompts')		

#Add Sentence to word_counts
def word_counts_update(sent):

	#Replace punc
	sent_no_punc = sent.translate(translator)

	#Count important words
	for word in sent_no_punc.lower().split():
		if word.lower() not in stop:
			word_counts[word] = 1 if word.lower() not in word_counts else word_counts[word] + 1
		

@app.route("/getPrompt", methods=['POST'])
def getPrompt():
	global prompt_len
	"""Respond to incoming calls with a simple text message."""

	resp = twilio.twiml.Response()
	
	idea = request.values['Body'].lower()
	
	prompt = get_random_wp(idea)
	
	#Get Rid of Stopwords, clean text and populate dictionaries
	word_counts_update(idea)
	word_counts_update(prompt[4:])
	
	prompt_len += len(prompt)
	
	#Append Prompt
	rec_prompts.append(prompt)
	
	resp.message(prompt)
	
	print(str(resp))	
	
	return str(resp)
	
def get_random_wp(info):
	posts = [x for x in wp_subreddit.search(query=info, limit=5) if x.title.startswith('[WP]')]			
				
	if len(posts) == 0:
		return "[WP]Your idea is too weird ..."
		
	chosen_post = random.choice(posts).title
	
	return chosen_post

@app.route("/")
@app.route("/main")
def main():
	print(word_counts)
	return render_template('index.html')
	
@app.route('/getData', methods=['GET'])
def getData():
	global word_counts 
	global rec_prompts
	global prompt_len

	#WordCloud cache
	wc_output = list(map(lambda key: {"text": key, "size": 10 + word_counts[key] * 10}, word_counts.keys()))
	
	output = { "rp_output": rec_prompts[:4], "wc_output": wc_output }
	
	limit = 10
	
	#Clear Caches
	if len(rec_prompts) > limit or prompt_len > 1500:
		word_counts = {} 
		rec_prompts = rec_prompts[-(limit - 1):]
		for sent in rec_prompts:
			word_counts_update(sent[4:])
	
	return json.dumps(output);
	
#This is the page for our game	
@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')
	
if __name__ == "__main__":
	app.run(debug=True)