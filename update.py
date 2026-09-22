import urllib.request
import ssl

# Danh sách link nguồn (Có thể thêm các link dự phòng khác vào danh sách này)
SOURCES = [
    "https://thcoban.github.io/thtt/tttt.m3u"
]

def fetch_m3u():
    context = ssl._create_unverified_context()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for url in SOURCES:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=context, timeout=15) as response:
                content = response.read().decode('utf-8', errors='ignore')
                # Kiểm tra nội dung phải đúng định dạng M3U và có dữ liệu
                if "#EXTM3U" in content and len(content) > 100:
                    print(f"Lấy dữ liệu thành công từ: {url}")
                    return content
        except Exception as e:
            print(f"Lỗi khi tải từ {url}: {e}")
    return None

new_content = fetch_m3u()

if new_content:
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Đã cập nhật playlist.m3u mới nhất!")
else:
    # Nếu nguồn bị die, giữ nguyên file cũ để tiếp tục xem các link stream trực tiếp
    print("Nguồn bị lỗi hoặc die. Giữ nguyên file playlist.m3u hiện tại!")
