import streamlit as st
import hashlib
import pandas as pd
import sqlite3

def create_user():
    c.execute('CREATE TABLE IF NOT EXISTS userstable (username TEXT PRIMARY KEY, password TEXT)')

def add_user(username, password):
    # ユーザーが既に存在するかを確認
    c.execute('SELECT * FROM userstable WHERE username = ?', (username,))
    existing_user = c.fetchone()
    if existing_user:
        st.warning("そのユーザー名は既に使用されています")
    else:
        c.execute('INSERT INTO userstable (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data
