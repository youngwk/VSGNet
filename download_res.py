wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1PXUG5MM87LIHjOpW-dIgoYqaNWc5zZA9' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1PXUG5MM87LIHjOpW-dIgoYqaNWc5zZA9" -O pre.zip && rm -rf /tmp/cookies.txt
unzip pre.zip && rm pre.zip
