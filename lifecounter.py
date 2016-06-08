#magic lifecounter python 2.7
#by rin kemp 06/08/2016
import os
import sys
#cls by popcnt of stackoverflow
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()

#player life counts
player1 = 20
player2 = 20
player3 = 20
player4 = 20
player5 = 20
player6 = 20
player7 = 20
player8 = 20
#conditionals
playercount = 0
addorsubtract = 0
subtractamount = 0
addamount = 0
yesorno = 1
print "welcome to mtg lifecounter"
while 1 == 1:
	print "please input the player count"
	try:
		playercount = input()
	except:
		e = sys.exc_info()[0]
		print e
	if playercount < 2:
		print "please input a valid number"
	elif playercount == 2:
		while yesorno == 1:
			print "player1 life:"
			print player1
			print "player2 life:"
			print player2
			print "please type the number of the player you wish to alter"
			try:
				playercount = input()
			except:
				e = sys.exc_info()[0]
				print e
			if playercount == 1:
				print "type 1 for plus or 2 for minus"
				try:
					addorsubtract = input()
				except:
					e = sys.exc_info()[0]
					print e
				if addorsubtract == 1:
					print "please type add amount"
					try:
						addamount = input()
					except:
						e = sys.exc_info()[0]
						print e
					player1 = player1 + addamount
					cls()
					print "player 1s life is now"
					print player1
					print ""
					print ""
				elif addorsubtract == 2:
					print "please type subtract amount"
					try:
						subtractamount = input()
					except:
						e = sys.exc_info()[0]
						print e
					player1 = player1 - subtractamount
					cls()
					print "player 1s life is now"
					print player1
					print ""
					print ""
			elif playercount == 2:
				print "type 1 for plus or 2 for minus"
				try:
					addorsubtract = input()
				except:
					e = sys.exc_info()[0]
					print e
				if addorsubtract == 1:
					print "please type add amount"
					try:
						addamount = input()
					except:
						e = sys.exc_info()[0]
						print e
					player2 = player2 + addamount
					cls()
					print "player 2s life is now"
					print player2
					print ""
					print ""
				elif addorsubtract == 2:
					print "please type subtract amount"
					try:
						subtractamount = input()
					except:
						e = sys.exc_info()[0]
						print e
					player2 = player2 - subtractamount
					cls()
					print "player 2s life is now"
					print player2
					print ""
					print ""
			else:
				exit()
	elif playercount == 3:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
	elif playercount == 4:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "player4 life:"
				print player4
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
				elif playercount == 4:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 + addamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 - subtractamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""

	elif playercount == 5:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "player4 life:"
				print player4
				print "player5 life:"
				print player5
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
				elif playercount == 4:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 + addamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 - subtractamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
				
				elif playercount == 5:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 + addamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 - subtractamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""
	elif playercount == 6:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "player4 life:"
				print player4
				print "player5 life:"
				print player5
				print "player6 life:"
				print player6
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
				elif playercount == 4:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 + addamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 - subtractamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
				
				elif playercount == 5:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 + addamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 - subtractamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""

				elif playercount == 6:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 + addamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 - subtractamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
	elif playercount == 7:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "player4 life:"
				print player4
				print "player5 life:"
				print player5
				print "player6 life:"
				print player6
				print "player7 life:"
				print player7
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
				elif playercount == 4:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 + addamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 - subtractamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
				
				elif playercount == 5:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 + addamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 - subtractamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""

				elif playercount == 6:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 + addamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 - subtractamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
				elif playercount == 7:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player7 = player7 + addamount
						cls()
						print "player 7s life is now"
						print player7
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player7 = player7 - subtractamount
						cls()
						print "player 7s life is now"
						print player7
						print ""
						print ""

	elif playercount == 8:
			while yesorno == 1:
				cls()
				print "player1 life:" 
				print player1
				print "player2 life:" 
				print player2
				print "player3 life:"
				print player3
				print "player4 life:"
				print player4
				print "player5 life:"
				print player5
				print "player6 life:"
				print player6
				print "player7 life:"
				print player7
				print "player8 life:"
				print player8
				print "please type the number of the player you wish to alter"
				try:
					playercount = input()
				except:
					e = sys.exc_info()[0]
					print e
				if playercount == 1:
					print "type 1 for plus or 2 for minus"
					addorsubtract = input()
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 + addamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player1 = player1 - subtractamount
						cls()
						print "player 1s life is now" 
						print player1
						print ""
						print ""
				elif playercount == 2:
					print "type 1 for plus or 2 for minus"
					try:	
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						addamount = input()
						player2 = player2 + addamount
						cls()
						print "player 2s life is now" 
						print player2
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player2 = player2 - subtractamount
						cls()
						print "player 2s life is now"
						print player2
						print ""
						print ""
				elif playercount == 3:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 + addamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player3 = player3 - subtractamount
						cls()
						print "player 3s life is now"
						print player3
						print ""
						print ""
				elif playercount == 4:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 + addamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player4 = player4 - subtractamount
						cls()
						print "player 4s life is now"
						print player4
						print ""
						print ""
				
				elif playercount == 5:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 + addamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player5 = player5 - subtractamount
						cls()
						print "player 5s life is now"
						print player5
						print ""
						print ""

				elif playercount == 6:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 + addamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player6 = player6 - subtractamount
						cls()
						print "player 6s life is now"
						print player6
						print ""
						print ""
				elif playercount == 7:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player7 = player7 + addamount
						cls()
						print "player 7s life is now"
						print player7
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player7 = player7 - subtractamount
						cls()
						print "player 7s life is now"
						print player7
						print ""
						print ""
				elif playercount == 8:
					print "type 1 for plus or 2 for minus"
					try:
						addorsubtract = input()
					except:
						e = sys.exc_info()[0]
						print e
					if addorsubtract == 1:
						print "please type add amount"
						try:
							addamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player8 = player8 + addamount
						cls()
						print "player 8s life is now"
						print player8
						print ""
						print ""
					elif addorsubtract == 2:
						print "please type subtract amount"
						try:
							subtractamount = input()
						except:
							e = sys.exc_info()[0]
							print e
						player8 = player8 - subtractamount
						cls()
						print "player 8s life is now"
						print player8
						print ""
						print ""

