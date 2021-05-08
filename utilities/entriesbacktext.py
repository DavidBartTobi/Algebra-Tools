# def Entries(self):
#     self.x_entry = ttk.Entry(self.top, width=6, justify='center')
#     self.x_entry.grid(row=1, column=1, pady=20)
#     self.y_entry = ttk.Entry(self.top, width=6, justify='center')
#     self.y_entry.grid(row=2, column=1, pady=(0, 20))
#
#     self.x_entry.insert(0, 'X')
#     self.y_entry.insert(0, 'Y ')
#     self.x_entry.configure(state=DISABLED)
#     self.y_entry.configure(state=DISABLED)
#
#     def on_click_x(event):
#         self.x_entry.configure(state=NORMAL)
#         self.x_entry.delete(0, END)
#
#         # make the callback only work once
#         self.x_entry.unbind('<Button-1>')
#
#     def on_click_y(event):
#         self.y_entry.configure(state=NORMAL)
#         self.y_entry.delete(0, END)
#
#         # make the callback only work once
#         self.y_entry.unbind('<Button-1>')
#
#     self.x_entry.bind('<Button-1>', on_click_x)
#     self.y_entry.bind('<Button-1>', on_click_y)
