#!/bin/python

import asyncio
import datetime
import random
import websockets
 
connected = set()

i=0

frames = [  '{"type":"recommandation","uuid":"10102","timestamp":1563210869792,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244543,"longitude":2.2435602}}',
'{"type":"notify","uuid":"10102","timestamp":1563210869807,"uuid":"10102","connected":true,"position":{"latitude":48.6246483,"longitude":2.2436406},"lane_id":0,"input_type":"raw_gnss","heading":192.6,"speed":372,"acceleration":4,"yaw_rate":-26}',
'{"type":"notify","uuid":"10102","timestamp":1563210870009,"uuid":"10102","connected":true,"position":{"latitude":48.6246483,"longitude":2.2436406},"lane_id":0,"input_type":"raw_gnss","heading":192.6,"speed":372,"acceleration":3,"yaw_rate":-26}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870094,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870296,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":792,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244679,"longitude":2.2435707}}',
'{"type":"notify","uuid":"10102","timestamp":1563210870412,"uuid":"10102","connected":true,"position":{"latitude":48.6246483,"longitude":2.2436406},"lane_id":0,"input_type":"raw_gnss","heading":192.6,"speed":372,"acceleration":3,"yaw_rate":-27}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870497,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":832,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244406,"longitude":2.2435497}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870497,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":832,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244406,"longitude":2.2435497}}',
'{"type":"notify","uuid":"10102","timestamp":1563210870614,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":3,"yaw_rate":-26}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870800,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210870800,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"notify","uuid":"10102","timestamp":1563210870916,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":4,"yaw_rate":-23}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871002,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871002,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"notify","uuid":"10102","timestamp":1563210871217,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":3,"yaw_rate":-23}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871304,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871304,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871547,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":800,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244624,"longitude":2.2435664}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871547,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":800,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244624,"longitude":2.2435664}}',
'{"type":"notify","uuid":"10102","timestamp":1563210871620,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":4,"yaw_rate":-23}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871807,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":852,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244262,"longitude":2.2435387}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210871807,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":852,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244262,"longitude":2.2435387}}',
'{"type":"notify","uuid":"10102","timestamp":1563210871822,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":2,"yaw_rate":-23}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210872009,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210872009,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":812,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244544,"longitude":2.2435603}}',
'{"type":"notify","uuid":"10102","timestamp":1563210872125,"uuid":"10102","connected":true,"position":{"latitude":48.6246140,"longitude":2.2436263},"lane_id":0,"input_type":"raw_gnss","heading":196.1,"speed":410,"acceleration":3,"yaw_rate":-22}',
'{"type":"recommandation","uuid":"10102","timestamp":1563210872254,"uuid":"10102","connected":true,"input_type":"gnss_raw_rtk","heading":206.8,"speed":821,"lane_id":0,"acceleration":0,"yaw_rate":0,"position":{"latitude":48.6244486,"longitude":2.2435558}}',]

 
async def pub_sub(websocket, path):
	global i
	while True:
		print(frames[i])
		await websocket.send(frames[i])
		await asyncio.sleep(0.3)
		i=(i+1)%len(frames)
		
             
start_server = websockets.serve(pub_sub, '127.0.0.1', 8081)
 
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
