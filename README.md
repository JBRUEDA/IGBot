# IGBot
Instagram bot to follow a fixed amount of followers from an account.


### How can you use it?
1. Set up chromedriver
   - Download chromedriver from [this URL](https://chromedriver.chromium.org/).
   - Unzip the file and move it to `/usr/local/bin`
2. Create `secrets.py` in the same directory as `main.py` and define the following variables:

   ```
   username = "your instagram username"
   pw = "your instagram password"
   target = "the instagram account from which you want to get followers"
   ```
3. You're now ready to use the bot by just running `main.py`

## Disclaimer
This has only been tested in Ubuntu
