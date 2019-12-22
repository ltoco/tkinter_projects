import tkinter as tk
from tkinter import font, colorchooser, messagebox, filedialog
import tkinter.ttk as ttk

# Creating a main app which will hold everything
main_app = tk.Tk()
main_app.geometry('1200x800') #setting geometry of app
main_app.title('New Editor') #add title to app

############################## MAIN MENU ###############################
main_menu = tk.Menu() #Create menu which will hold file menu and other menus

### File Menu Icons
new_icon = tk.PhotoImage(file='icons/new.png')
open_icon = tk.PhotoImage(file='icons/open.png')
save_icon = tk.PhotoImage(file='icons/save.png')
save_as_icon = tk.PhotoImage(file='icons/save_as.png')
exit_icon = tk.PhotoImage(file='icons/exit.png')

### File Menu
file_menu = tk.Menu(main_menu, tearoff=False) #add file menu to the main menu
# Setting tearoff=False will prevent that menu detaching from its place


### Edit Menu Icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')


### Edit Menu
edit_menu = tk.Menu(main_menu, tearoff=False)


### View Menu Icons
tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')

### View Menu
view_menu = tk.Menu(main_menu, tearoff=False)


### Color Theme Icon
light_default_icon = tk.PhotoImage(file="icons/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons/light_plus.png")
dark_icon = tk.PhotoImage(file="icons/dark.png")
red_icon = tk.PhotoImage(file="icons/red.png")
monokai_icon = tk.PhotoImage(file="icons/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons/night_blue.png")

### Color Menu
color_theme_menu = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar() #declares a variable of string type which Tcl interpreter can understand
color_icon = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default ': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

 

### Cascade
main_menu.add_cascade(label='File', menu=file_menu) #enables to create hierarchical menu
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label='Color Theme', menu=color_theme_menu)

############### ----------- END MAIN MENU ------------ ################


############################## TOOLBAR  ###############################

tool_bar = tk.Label(main_app)
tool_bar.pack(side='top', fill=tk.X)

### Font Family Box
font_family = font.families() #Create a tuple of all the font families
font_family_choice = tk.StringVar()
 # Creates a combobox with font family as values and selected value stored in font_family_choice, readonly 
font_family_box = ttk.Combobox(tool_bar, values=font_family, textvariable=font_family_choice, width=30, state='readonly')
# font_family_box.pack(side='left')
font_family_box.grid(row=0, column=0, padx=5)
font_family_box.current(font_family.index('Arial')) #Sets current value on combobox to value corresponding to the passed index 

# Font Size Box
font_size = tuple(range(8,100,2))
font_size_choice = tk.IntVar()
font_size_box = ttk.Combobox(tool_bar, values=font_size, textvariable=font_size_choice, state="readonly", width=3)
font_size_box.grid(row=0, column=1, padx=5)
font_size_box.current(8)

# Bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_button = tk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)

# Italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_button = tk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)

# Underline button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_button = tk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)

# Font Color button
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_button = tk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)

# Align Center button
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_button = tk.Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=6, padx=5)

# Align Left button
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_button = tk.Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=7, padx=5)

# Align Right button
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_button = tk.Button(tool_bar, image=align_right_icon)
align_right_button.grid(row=0, column=8, padx=5)

############### ----------- END TOOLBAR  ------------ ################

############################## TEXT EDITOR ###############################

# Creates text editor with wordwrap = True and simulated 3D effects as FLAT(normal)
text_editor = tk.Text(main_app, wrap='word', relief=tk.FLAT)
# Create a scrollbar at the right of text editor
scroll_bar = tk.Scrollbar(main_app, command = text_editor.yview)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
# telling text editor that scroll bar belongs to him
text_editor['yscrollcommand'] = scroll_bar.set
# Setting focus on text editor always (cursor blinking)
text_editor.focus_set()
# Expand text editor in X and Y direction(BOTH), expand = True option tells the manager to assign additional space to the widget box if parent widget is made larger.
text_editor.pack(fill=tk.BOTH, expand=True)

###------- Change font family and size
current_font_family = "Arial"
current_font_size = 24

def change_font(event=None):
	'''
	Change font style by keeping previous font style i.e. preserving bold, italics and underlined font
	1. Get current chosen font family and size
	2. Create a new font called new_font which has attributes of font currently present on editor
	3. Update size and family of newly created font
	4. Replace existing font present in text editor with new font

	# We need to pass an event as bind() requires an event, in our case we are passing <<ComboboxSelected>> as our event. As we are not using attributes of that event we do event=None
	'''
	global current_font_family
	global current_font_size

	current_font_family = font_family_choice.get()
	current_font_size = font_size_choice.get()
	new_font = tk.font.Font(font=text_editor['font'])
	new_font.config(size=current_font_size, family=current_font_family)
	text_editor.config(font=new_font)

font_family_box.bind('<<ComboboxSelected>>', change_font)
font_size_box.bind('<<ComboboxSelected>>', change_font)

text_editor.config(font=(current_font_family, current_font_size))

#------- Buttons functionality

### Bold button functionality
def change_to_bold():
	'''
	Change font style by preserving bold, italics, size, font family and underlined font
	1. Create a new font called new_font which has attributes of font currently present on editor
	2. Check for condition and update new font accordingly
	3. Replace existing font present in text editor with new font
	'''
	global current_font_family
	global current_font_size
	new_font = tk.font.Font(font=text_editor['font'])
	print(new_font.actual())
	if new_font.actual()['weight'] == 'normal':
		new_font.config(weight='bold')
		text_editor.configure(font=new_font)
	else:
		new_font.config(weight='normal')
		text_editor.configure(font=new_font)

bold_button.configure(command=change_to_bold)

### Underline button functionality
def change_to_underline():
	global current_font_family
	global current_font_size
	new_font = tk.font.Font(font=text_editor['font'])
	print(new_font.actual())
	if new_font.actual()['underline'] == 0:
		new_font.config(underline=1)
		text_editor.configure(font=new_font)
	else:
		new_font.config(underline=0)
		text_editor.configure(font=new_font)

underline_button.configure(command=change_to_underline)

### Italic button functionality
def change_to_italic():
	global current_font_family
	global current_font_size
	new_font = tk.font.Font(font=text_editor['font'])
	print(new_font.actual())
	if new_font.actual()['slant'] == 'roman':
		new_font.config(slant='italic')
		text_editor.configure(font=new_font)
	elif new_font.actual()['slant'] == 'italic':
		new_font.config(slant='roman')
		text_editor.configure(font=new_font)

italic_button.configure(command=change_to_italic)
############### ----------- END TEXT EDITOR ------------ ################

############################## STATUS BAR ###############################
status_bar = tk.Label(main_app, text="Status bar")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
############### ----------- END STATUS BAR ------------ ################

############################## MAIN MENU FUNCTIONALITY ###############################

# File menu commands
# adding commands to the file menu
file_menu.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N")
# compound = tk.LEFT aligns the iamge to left and label to right or else only image is shown
# accelerator = "Ctrl+N" will show what key combination to be used as shortcut
file_menu.add_command(label="open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O")
file_menu.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S")
file_menu.add_command(label="Save as", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S")
file_menu.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q")

# Edit menu commands
edit_menu.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V")
edit_menu.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X")
edit_menu.add_command(label="Clear all", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X")
edit_menu.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F")

# View menu commands
view_menu.add_checkbutton(label="Toolbar", image=tool_bar_icon, compound=tk.LEFT)
view_menu.add_checkbutton(label="Status bar", image=status_bar_icon, compound=tk.LEFT)

# Color theme commands
count = 0
for i in color_dict:
	color_theme_menu.add_radiobutton(label=i, image=color_icon[count], variable=theme_choice, compound=tk.LEFT)
	count+=1
############### ----------- END MAIN MENU FUNCTIONALITY ------------ ################

main_app.configure(menu=main_menu) # add main menu to app
main_app.mainloop()
