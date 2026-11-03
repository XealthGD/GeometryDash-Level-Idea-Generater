import random
import time
import os
import streamlit as st
#python -m streamlit run app.py(type cmd in the path "C:\Users\orin\Desktop\app.py")
st.set_page_config(page_title="GD level generater", page_icon = "💜")
st.header("Gd level generater")
st.markdown("""
<style>
.stApp {
    background-color: #12001F;
    
    .stButton > button {
    background-color: #A020F0;
    color: white;
    border-radius: 12px;
    border: none;
}

.stButton > button:hover {
    background-color: #301934;
    color: #301934;
}
}
</style>
""", unsafe_allow_html=True)
if st.button("Generater idea", use_container_width=True):
    #os.system("cls")
    #print("\033[1;35mGd Level Idea Generator\n\033[0m")
    #input("\033[1;32m\nEnter to run\n\033[0m")
    word1 = ["Blood","Luminous","Ridiculous","Geometry","Hollow","Fizzy","Easy","Slow","Jolly","Real","Tidal","Sakupen","water"]
    word2 = ["Snazz","Bath","Wave","Tidal","Flatty","Meow","Candy","Grief","Fast","Filled","Mango","Hell","End"]
    diff = ["Easy","Normal","Hard","Harder","Insane","Easy demon","Medium demon","Hard demon","Insane demon","Extreme Demon"]
    vibes = ["Colorful","Flashy","Memory","chill glow","Cartoony","1.9 style","Hell","Simple glow","Simple mordern","2.0 style"]
    gamemodes = ["Cube", "Ship", "Ball", "Ufo", "Wave","Robot","Spider","Swing"]
    lengths = ["Medium","Short" , "Long", "XL"]
    sid = ["1","2","3","4","5","6","7","8","9","0"]
    sid2 = ["1","2","3","4","5","6"]
    colors = ["Purple","Pink","Red","Blue","Cyan","Orange","Yellow","Green"]
    Name = random.choice(word1) + " " + random.choice(word2)
    Difficulty = random.choice(diff)
    vibesrng = random.choice(vibes)
    gms = random.choice(gamemodes),random.choice(gamemodes),random.choice(gamemodes),random.choice(gamemodes),random.choice(gamemodes)
    lent = random.choice(lengths)
    rngids = "1" + random.choice(sid2) + random.choice(sid) + random.choice(sid) + random.choice(sid) + random.choice(sid) + random.choice(sid) + r"(Not guaranteed)"
    col1 = random.choice(colors)
    col2 = random.choice(colors)
    col3 = random.choice(colors)
   # print(f"\033[1;34m\nName: {Name}\033[0m \033[0;31m\nDifficulty: {Difficulty}\033[0m \033[0;95m\nDecor Style: {vibesrng}\033[0m \033[0;36m\nGamemodes: {gms}\033[0m \033[0;33m\nLength: {lent}\033[0 ,\033[0;32m\nSong Id = {rngids}\033[0m \033[0;36m\nColor Palette: {col1},{col2},{col3}\033[0m")
    #time.sleep(0.2)
    #input("\033[1;32m\nEnter to rerun\n\033[0m")
    st.divider()
    st.header(Name)
    st.write("Difficulty:", Difficulty)
    st.write("Decor Style:", vibesrng)
    st.write("gamemode sequence:", gms)
    st.write("lenght:", lent)
    st.write("Song:", rngids)
    st.write("color pallete:", col1, col2, col3)
