import hmac
import hashlib

def hmac_codes(secret_key, num=200):
    codes = set()
    counter = 0
    while len(codes) < num:
        digest = hmac.new(secret_key.encode(), str(counter).encode(), hashlib.sha256).hexdigest()
        code = digest[:16].upper()  # 取哈希值前16位
        print(code)
        codes.add(code)
        counter += 1
    return list(codes)

# 使用示例（需保存secret_key用于验证）
secret = "your_app_secret_2025"
activation_codes = hmac_codes(secret)