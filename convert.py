# convert.py
import pymupdf4llm
from pathlib import Path
import sys

def convert_pdf_to_markdown(pdf_path):
    """Chuyển đổi một file PDF sang Markdown"""
    try:
        print(f"📄 Converting: {pdf_path}")
        
        # Chuyển đổi PDF sang Markdown
        md_text = pymupdf4llm.to_markdown(str(pdf_path), page_chunks=False) # Thêm page_chunks=False để có 1 file md duy nhất
        
        # Tạo đường dẫn output (giữ nguyên cấu trúc thư mục)
        md_path = pdf_path.with_suffix('.md')
        
        # Ghi file Markdown
        md_path.write_text(md_text, encoding='utf-8')
        
        print(f"✅ Converted successfully: {md_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {str(e)}")
        return False

def main():
    # Tìm tất cả file PDF trong thư mục hiện hành và thư mục con
    pdf_files = list(Path('.').rglob('*.pdf'))
    
    if not pdf_files:
        print("⚠️ No PDF files found in repository")
        sys.exit(0)
    
    print(f"🔍 Found {len(pdf_files)} PDF file(s)")
    print("-" * 60)
    
    # Chuyển đổi từng file
    success_count = 0
    failed_count = 0
    
    for pdf_file in pdf_files:
        # Bỏ qua các thư mục ẩn như .git
        if any(part.startswith('.') for part in pdf_file.parts):
            continue
            
        if convert_pdf_to_markdown(pdf_file):
            success_count += 1
        else:
            failed_count += 1
    
    print("-" * 60)
    print("✨ Conversion complete!")
    print(f"   ✅ Success: {success_count}")
    print(f"   ❌ Failed: {failed_count}")
    
    # Exit với code 1 nếu có lỗi để báo cho GitHub Actions biết
    if failed_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
