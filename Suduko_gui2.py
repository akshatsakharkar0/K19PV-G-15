from tkinter import *
from tkinter import messagebox

import pygame

pygame.font.init() 


root=Tk(className="Sudoku")
root.iconbitmap('abcde/sudoku1.png')
root.geometry("500x600")

def menu_about():
    response=messagebox.showinfo("About us","Developed by : Akshat Sakharkar(11905137),\n \t     Avinash p(11903059) \nContact us:  \nE-mail: liveitsudoku@gmail.com \nPhone: +91 xxxxxxxxxx  \nGet more info at www.liveitsudoku.org")

def instruction():
	response=messagebox.showinfo("Instruction","Use Keyboard ")

menu_bar=Menu(root)
root.config(menu=menu_bar)


file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Main menu",command=None)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)


help_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="instruction",command=instruction)
help_menu.add_separator()
help_menu.add_command(label="About us",command= menu_about)

def sudoku_game():
	
	screen = pygame.display.set_mode((500, 600)) 

	 
	pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING") 
	img = pygame.image.load('abcde/1.png') 
	pygame.display.set_icon(img) 

	x = 0
	y = 0
	dif = 500 / 9
	val = 0
	
	grid =[ 
			[7, 8, 0, 4, 0, 0, 1, 2, 0], 
			[6, 0, 0, 0, 7, 5, 0, 0, 9], 
			[0, 0, 0, 6, 0, 1, 0, 7, 8], 
			[0, 0, 7, 0, 4, 0, 2, 6, 0], 
			[0, 0, 1, 0, 5, 0, 9, 3, 0], 
			[9, 0, 4, 0, 6, 0, 0, 0, 5], 
			[0, 7, 0, 3, 0, 0, 0, 1, 2], 
			[1, 2, 0, 0, 0, 7, 4, 0, 0], 
			[0, 4, 9, 2, 0, 6, 0, 0, 7] 
		] 

	 
	font1 = pygame.font.SysFont("comicsans", 40) 
	font2 = pygame.font.SysFont("comicsans", 20) 
	def get_cord(pos): 
		global x 
		x = pos[0]//dif 
		global y 
		y = pos[1]//dif 

	
	def draw_box(): 
		for i in range(2): 
			pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7) 
			pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7) 

			 
	def draw(): 
		 
			
		for i in range (9): 
			for j in range (9): 
				if grid[i][j]!= 0: 

					 
					pygame.draw.rect(screen, (245,199,26), (i * dif, j * dif, dif + 1, dif + 1)) 

					 
					text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0)) 
					screen.blit(text1, (i * dif + 15, j * dif + 15)) 
				 
		for i in range(10): 
			if i % 3 == 0 : 
				thick = 7
			else: 
				thick = 1
			pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick) 
			pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	 

		 
	def draw_val(val): 
		text1 = font1.render(str(val), 1, (0, 0, 0)) 
		screen.blit(text1, (x * dif + 15, y * dif + 15))	 

	
	def raise_error1(): 
		text1 = font1.render("WRONG !!!", 1, (0, 0, 0)) 
		screen.blit(text1, (20, 570)) 
	def raise_error2(): 
		text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0)) 
		screen.blit(text1, (20, 570)) 

	 
	def valid(m, i, j, val): 
		for it in range(9): 
			if m[i][it]== val: 
				return False
			if m[it][j]== val: 
				return False
		it = i//3
		jt = j//3
		for i in range(it * 3, it * 3 + 3): 
			for j in range (jt * 3, jt * 3 + 3): 
				if m[i][j]== val: 
					return False
		return True

	 
	def solve(grid, i, j): 
		
		while grid[i][j]!= 0: 
			if i<8: 
				i+= 1
			elif i == 8 and j<8: 
				i = 0
				j+= 1
			elif i == 8 and j == 8: 
				return True
		pygame.event.pump()	 
		for it in range(1, 10): 
			if valid(grid, i, j, it)== True: 
				grid[i][j]= it 
				global x, y 
				x = i 
				y = j 
				 
				screen.fill((255, 255, 255)) 
				draw() 
				draw_box() 
				pygame.display.update() 
				pygame.time.delay(20) 
				if solve(grid, i, j)== 1: 
					return True
				else: 
					grid[i][j]= 0
				 
				screen.fill((255, 255, 255)) 
			
				draw() 
				draw_box() 
				pygame.display.update() 
				pygame.time.delay(50)	 
		return False

	 
	def instruction(): 
		text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0)) 
		text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0)) 
		screen.blit(text1, (20, 520))		 
		screen.blit(text2, (20, 540)) 

	 
	def result(): 
		text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0)) 
		screen.blit(text1, (20, 570))	 
	run = True
	flag1 = 0
	flag2 = 0
	rs = 0
	error = 0
	 
	while run: 
		
		 
		screen.fill((255, 255, 255)) 
		 
		for event in pygame.event.get(): 
			 
			if event.type == pygame.QUIT: 
				run = False
				 
			if event.type == pygame.MOUSEBUTTONDOWN: 
				flag1 = 1
				pos = pygame.mouse.get_pos() 
				get_cord(pos) 
				 
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_LEFT: 
					x-= 1
					flag1 = 1
				if event.key == pygame.K_RIGHT: 
					x+= 1
					flag1 = 1
				if event.key == pygame.K_UP: 
					y-= 1
					flag1 = 1
				if event.key == pygame.K_DOWN: 
					y+= 1
					flag1 = 1	
				if event.key == pygame.K_1: 
					val = 1
				if event.key == pygame.K_2: 
					val = 2	
				if event.key == pygame.K_3: 
					val = 3
				if event.key == pygame.K_4: 
					val = 4
				if event.key == pygame.K_5: 
					val = 5
				if event.key == pygame.K_6: 
					val = 6
				if event.key == pygame.K_7: 
					val = 7
				if event.key == pygame.K_8: 
					val = 8
				if event.key == pygame.K_9: 
					val = 9
				if event.key == pygame.K_RETURN: 
					flag2 = 1
				 
				if event.key == pygame.K_r: 
					rs = 0
					error = 0
					flag2 = 0
					grid =[ 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0], 
					[0, 0, 0, 0, 0, 0, 0, 0, 0] 
					] 
				 
				if event.key == pygame.K_d: 
					rs = 0
					error = 0
					flag2 = 0
					grid =[ 
						[7, 8, 0, 4, 0, 0, 1, 2, 0], 
						[6, 0, 0, 0, 7, 5, 0, 0, 9], 
						[0, 0, 0, 6, 0, 1, 0, 7, 8], 
						[0, 0, 7, 0, 4, 0, 2, 6, 0], 
						[0, 0, 1, 0, 5, 0, 9, 3, 0], 
						[9, 0, 4, 0, 6, 0, 0, 0, 5], 
						[0, 7, 0, 3, 0, 0, 0, 1, 2], 
						[1, 2, 0, 0, 0, 7, 4, 0, 0], 
						[0, 4, 9, 2, 0, 6, 0, 0, 7] 
					] 
		if flag2 == 1: 
			if solve(grid, 0, 0)== False: 
				error = 1
			else: 
				rs = 1
			flag2 = 0	
		if val != 0:			 
			draw_val(val) 
			 
			if valid(grid, int(x), int(y), val)== True: 
				grid[int(x)][int(y)]= val 
				flag1 = 0
			else: 
				grid[int(x)][int(y)]= 0
				raise_error2() 
			val = 0	
			
		if error == 1: 
			raise_error1() 
		if rs == 1: 
			result()		 
		draw() 
		if flag1 == 1: 
			draw_box()	 
		instruction()	 

		
		pygame.display.update() 

		 
	pygame.quit()

def main_window():
	main_frame=Frame(root,bg="#028A0F")
	main_frame.pack(fill=BOTH,expand=True)

        
	top_label = Label(main_frame,text='Lets play Sudoku',bg="#000080",fg='white',font=40)
	top_label.pack(pady=50)   

	
	new_game_button=Button(main_frame,text="New game",bg='#FDFF00',relief=RAISED,padx=30,pady=20,font=30,command=sudoku_game)
	new_game_button.pack(pady=20)

	
	exit_game_button=Button(main_frame,text="Exit",bg='#FDFF00',relief=RAISED,padx=30,pady=20,font=30,command=root.destroy)
	exit_game_button.pack()

	

main_window()

root.resizable(False,False)
root.mainloop()
