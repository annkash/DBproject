from tkinter import ttk
from gui import view
import customtkinter
import tkinter as tk
from gui import model
from pandastable import Table
import pandas as pd

class Controller:

    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.open_table = False

    def get_list_db(self):
        return self._model.get_list_db()

    def delete_database(self, database, delete_database_window):
        self._model.delete_database(database)
        delete_database_window.destroy()
        delete_database_window.update()

    def get_list_tables(self, database):
        return self._model.get_list_tables(database)

    def get_columns(self, database, table):
        return self._model.get_columns(database, table)

    def add_data_to_table(self,database, table, data_entries, info_label):
        data_list = []
        for i in range(0, len(data_entries)):
            data_list.append(data_entries[i].get())
        if '' in data_list:
            info_label.configure(text='Некоторые поля не заполнены', text_color='red')
            pass
        else:
            self._model.add_data_to_table(database, table, data_list)
            info_label.configure(text='Данные добавлены', text_color='green')

    def delete_row(self, database, table, row, info_label):
        self._model.delete_row(database, table, row)
        info_label.configure(text='строка удалена', text_color='green')

    def clear_table(self, database, table, clear_table_window):
        self._model.clear_table(database, table)
        clear_table_window.destroy()
        clear_table_window.update()

    def create_database(self, database, create_database_window):
        self._model.create_database(database)
        create_database_window.destroy()
        create_database_window.update()

    def change_row(self, database, table, id, num_col, value, pt, info_label, form_frame, rowclicked):
        self._model.change_row(database, table, id, num_col, value)
        if (num_col!=0):
            pt.model.setValueAt(value, rowclicked, num_col)
            info_label.configure(text='изменения сохранены', text_color='green')
        for widget in form_frame.winfo_children():
            widget.destroy()

    def delete_students_to_city(self, database, city, info_label):
        if (city == ''):
            info_label.configure(text='введите город', text_color='red')
        else:
            self._model.delete_students_to_city(database, city)
            info_label.configure(text='данные удалены', text_color='green')

    def find_students_to_city(self, database, city, info_label):
        if (city == ''):
            info_label.configure(text='введите город', text_color='red')
        else:
            return self._model.find_students_to_city(database, city)