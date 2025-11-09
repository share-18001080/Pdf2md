# convert.py
import pymupdf4llm
from pathlib import Path
import sys

def convert_pdf_to_markdown(pdf_path):
    """Chuyển đổi một file PDF sang Markdown"""
    try:
        print(f"📄 Converting: {pdf_path}")
        md_text = pymupdf4llm.to_markdown(str(pdf_path), page_chunks=False)
        md_path = pdf_path.with_suffix('.md')
        md_path.write_text(md_text, encoding='utf-8')
        print(f"✅ Converted successfully: {md_path}")
        return True
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {str(e)}")
        return False

def main():
    # Sử dụng glob để tự động bỏ qua các file/thư mục bắt đầu bằng dấu chấm
    pdf_files = list(Path('.').glob('**/*.pdf'))
    
    # Lọc thủ công để chắc chắn bỏ qua thư mục .git
    pdf_files = [f for f in pdf_files if '.git' not in f.parts]

    if not pdf_files:
        print("⚠️ No PDF files found in repository")
        sys.exit(0)
    
    print(f"🔍 Found {len(pdf_files)} PDF file(s) to process:")
    for f in pdf_files:
        print(f"  - {f}")
    print("-" * 60)
    
    success_count = 0
    failed_count = 0
    
    for pdf_file in pdf_files:
        if convert_pdf_to_markdown(pdf_file):
            success_count += 1
        else:
            failed_count += 1
            
    print("-" * 60)
    print("✨ Conversion complete!")
    print(f"   ✅ Success: {success_count}")
    print(f"   ❌ Failed: {failed_count}")
    
    if failed_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()