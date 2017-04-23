# WritingPromptChatbot

Description: In order to relieve some writer's block, we decided to make a simple sms chat bot to respond with random writing prompts from https://www.reddit.com/r/WritingPrompts/. We then decided to host a webservice to visualize key topics of these writing prompts in a word cloud.

url: http://ec2-54-89-244-128.compute-1.amazonaws.com/ (*Registered domain: www.storystorm.com)

Tech:
Flask Python
Html/CSS/Javascript
AWS EC2 Server instance
*Domain name

API:
https://github.com/jasondavies/d3-cloud : for animated word cloud features
reddit API: for providing random posts.
twilio: for sms messaging

