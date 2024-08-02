from flask import Flask, render_template_string

app = Flask(__name__)

html_content = '''

 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐇𝐀𝐒𝐒𝐀𝐍 𝐌𝐔𝐋𝐓𝐘 𝐒𝐄𝐑𝐕𝐄𝐑</title>
    <style>
        /* CSS for styling elements */
        body {
            overflow: hidden; /* Hide overflow to prevent scrollbars */
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .video-background {
            position: fixed;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1; /* Put the video behind everything */
            transform: translate(-50%, -50%);
        }
        .header {
            background-color: transparent;
            padding: 20px;
            text-align: center;
        }
        .header h1 {
            color: #fff;
            margin: 0;
            font-size: 28px;
            font-weight: bold;
        }
        .container {
        max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
         text-align: center;
         color: white;
         }
        input[type="username"], input[type="password"], input[type="submit"] {
            padding: 10px;
            margin: 10px;
            border-radius: 20px;
            border: 5px;
            color: black;
        }
        input[type="submit"] {
            background-color: Red;
            color: white;
            cursor: pointer;
        }
    </style>
    <script>
        function playVideo() {
            var video = document.getElementById('bg-video');
            video.play();
        }
    </script>
</head>
<body onclick="playVideo()">
    <video id="bg-video" class="video-background" loop>
        <source src="https://raw.githubusercontent.com/HassanRajput0/Video/main/Tecnología___Hintergrundbilder,_Hintergrund,_Pappe(360P).mp4">
        Your browser does not support the video tag.
    </video>
    <div class="container">
      <img src="https://i.ibb.co/BVPLFS1/20240719-163451.jpg">
        <div class="mb-3">
    <a href="https://heylink.me/devilking768">
        <button class="ABY">𝗠𝗔𝗗𝗘 𝗕𝗬 𝗪𝗔𝗥𝗥𝗜𝗢𝗨𝗥 𝗥𝗨𝗟𝗘𝗫</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://post-server-j0fp.onrender.com">
        <button class="GFG">𝗖𝗢𝗡𝗩𝗢+𝗣𝗢𝗦𝗧  :=</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://convo-server-22tn.onrender.com">
        <button class="ABB">𝗦𝗜𝗡𝗚𝗟𝗘 𝗧𝗢𝗞𝗘𝗡 𝗖𝗢𝗡𝗩𝗢</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://page-server-onya.onrender.com">
        <button class="ABK">𝗠𝗨𝗟𝗧I 𝗧𝗢𝗞𝗘𝗡 𝗣𝗢𝗦𝗧 </button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://satish-ki-ma-ki-chut.onrender.com">
        <button class="ABC">𝗦𝗜𝗡𝗚𝗟𝗘 𝗖𝗢𝗢𝗞𝗜𝗘 𝗣𝗢𝗦𝗧</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://multy-convo.onrender.com">
        <button class="ABD">𝗠𝗨𝗟𝗧𝗬 𝗧𝗢𝗞𝗘𝗡 𝗖𝗢𝗡𝗩𝗢</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://singal-post-z9hi.onrender.com">
        <button class="ABE">𝗦𝗜𝗡𝗚𝗟𝗘 𝗧𝗢𝗞𝗘𝗡 𝗣𝗢𝗦𝗧</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://i.ibb.co/fMsks05/Messenger-creation-355e01cf-042b-437a-94e3-0415c5187252.jpg">
        <button class="ABF">𝗦𝗘𝗡𝗧 𝗙𝗥𝗢𝗠 𝗪𝗘𝗕 : 𝗖𝗢𝗠𝗜𝗡𝗚 𝗦𝗢𝗢𝗡</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://i.ibb.co/VLhGGyP/Screenshot-2024-06-28-21-48-57-38.jpg">
        <button class="ABH">𝗕𝗼𝗼𝗸𝗺𝗮𝗿𝗸 𝗺𝘂𝗹𝘁𝗶 𝘁𝗼𝗸𝗲𝗻+𝗰𝗼𝗼𝗸𝗶𝗲 : 𝗰𝗼𝗺𝗶𝗻𝗴 𝘀𝗼𝗼𝗻</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://github.com/DeViiLXD/MULTI-COOKIE-SERVER-DEVIL">
        <button class="ABJ">𝗺𝘂𝗹𝘁𝘆 𝗰𝗼𝗼𝗸𝗶𝗲𝘀 : 𝗼𝗳𝗳𝗹𝗶𝗻𝗲 𝘀𝗲𝗿𝘃𝗲𝗿 𝗮𝗻𝗱 𝘄𝗶𝘁𝗵 𝗳𝗼𝗹𝗹𝗼𝘄 𝗺𝘆 𝗴𝗶𝘁𝗵𝘂𝗯 𝗮𝗰𝗼𝘂𝗻𝘁</button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://i.ibb.co/q7g5PCW/Screenshot-2024-06-30-12-52-50-60.jpg">
        <button class="ABK">𝐀𝐥𝐥- 𝘀𝗲𝗿𝘃𝗲𝗿 𝗮𝗻𝗱 𝘁𝗼𝗼𝗹𝘀 𝗯𝘆 𝗶𝘁𝘀 𝘁𝗵𝗲 𝗴𝗿𝗲𝗮𝘁𝗲𝘀𝘁 𝘄𝗮𝗿𝗿𝗶𝗼𝘂𝗿 𝗿𝘂𝗹𝗲𝘅 𝗢𝘄𝗻𝗲𝗿: 𝗔𝗹𝗼𝗻𝗲 𝗪𝗮𝗿𝗿𝗶𝗼𝘂𝗥 𝗗𝗲𝗩𝗶𝗟 𝗜𝗻𝘀𝗶𝗗𝗲 </button>
    </a>
    </div>
        <div class="mb-3">
    <a href="https://chat.whatsapp.com/IQOZmY5o2Ny7C8Zc5g0180">
        <button class="ABL">𝗪𝗔𝗥𝗥𝗜𝗢𝗨𝗥 𝗥𝗨𝗟𝗘𝗫 𝗦𝗘 𝗝𝗨𝗗𝗡𝗘 𝗞𝗘 𝗟𝗜𝗬𝗘 𝗖𝗟𝗜𝗖𝗞 𝗞𝗥𝗘</button>
    </a>
    <a href="http://localhost:8158/TEST2.html">
        <button class="ABZ">𝐇𝐨𝐦𝐞</button>
    </a> 
</body> 
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
