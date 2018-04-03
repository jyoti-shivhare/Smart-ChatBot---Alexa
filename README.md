# Smart AI ChatBot---Inspired by Mitsuku and Alexa

According to Oxford Dictionaries, a chatbot is

“A computer program designed to simulate conversation with human users, especially over the Internet.”
It is an assistant that communicates with us through text messages, a virtual companion that integrates into websites, applications or instant messengers and helps entrepreneurs to get closer to customers. Such a bot is an automated system of communication with users.

Derived from “chat robot”, "chatbots" allow for highly engaging, conversational experiences, through voice and text, that can be customized and used on mobile devices, web browsers, and on popular chat platforms such as Facebook Messenger, or Slack. 

With the advent of deep learning technologies such as text-to-speech, automatic speech recognition, and natural language processing, chatbots that simulate human conversation and dialogue can now be found in call center and customer service workflows, DevOps management, and as personal assistants.

![Explanation of how it works](https://www.wordstream.com/images/chatbots-how-chatbots-work.jpg)

I have used dictionaries of messaged and coversations. Next, I built a predictive model which will recognize the intent of these messages. 
For this, I used Supervised Learning,. A classifier (predictive model) has a number of tunable parameters which can be tuned using the training dataset. We keep tweeking the classifier till it gives the prediction on the training which is also called as fitting.
Then we will evaluate the performance of the classifier using the testing dataset( Containing new messages which the classifier hasn't seen before)

Nearest Neighbor Classification: We will look at the training data and based on the labelled intent in this dataset , we'll try to look for the labelled example that's most similar and use it's intent  as a best guess.
