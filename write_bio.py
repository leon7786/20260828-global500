import sys, os

def write_bio(folder_name, content):
    target_path = os.path.join('/root/1CT-Share/20260828-global500/Founder', folder_name, 'founder.md')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    sz = os.path.getsize(target_path)
    print(f"Successfully wrote {folder_name}/founder.md -> {sz:,} bytes ({sz/1024:.1f} KB)")

if __name__ == '__main__':
    print("write_bio helper ready")
