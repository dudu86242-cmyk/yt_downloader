import streamlit as st
import yt_dlp
import os

st.title("🎬 የዩቲዩብ ቪዲዮ ማውረጃ (YouTube Downloader)")

url = st.text_input("እባክዎ የዩቲዩብ ሊንክ (URL) እዚህ ጋር ያስገቡ:")

if url:
    if st.button("ቪዲዮውን አውርድ"):
        try:
            with st.spinner("ቪዲዮው እየወረደ ነው፣ እባክዎ ይጠብቁ..."):
                download_path = os.path.expanduser("~/Downloads")
                ydl_opts = {
                    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                    'format': 'best',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            st.success(f"ቪዲዮው በተሳካ ሁኔታ ወርዷል! ማውረድ አቃፊዎን (Downloads folder) ይፈትሹ።")
        except Exception as e:
            st.error(f"ስህተት ተፈጥሯል: {e}")