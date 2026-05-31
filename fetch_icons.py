import urllib.request
import re
import os

apps = {
    'lich-van-nien': 'vn.weplay.lichvannien',
    'lich-nhu-y': 'com.appdev.lichnhuy',
    'lich-viet': 'com.appspace.lichviet',
    'nhac-ngay-gio': 'com.vnn.nhacngaygio'
}

def get_icon(app_id, filename):
    url = f"https://play.google.com/store/apps/details?id={app_id}&hl=en&gl=US"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Google Play stores the icon URL in a meta tag like:
        # <meta name="twitter:image" content="https://play-lh.googleusercontent.com/...">
        # or <img src="..." alt="Icon image" class="T75of ...">
        
        match = re.search(r'meta property="og:image" content="([^"]+)"', html)
        if match:
            img_url = match.group(1)
            print(f"Found icon for {app_id}: {img_url}")
            urllib.request.urlretrieve(img_url, filename)
            print(f"Saved to {filename}")
        else:
            print(f"Could not find icon for {app_id}")
    except Exception as e:
        print(f"Failed to fetch {app_id}: {e}")

if __name__ == "__main__":
    for name, pkg in apps.items():
        get_icon(pkg, f"{name}.png")
