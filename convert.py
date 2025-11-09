# convert.py - Enhanced Version
import pymupdf4llm
from pathlib import Path
import sys
from datetime import datetime

def should_convert(pdf_path):
    """
    Kiểm tra xem file PDF có cần được convert không.
    Trả về True nếu:
    - File MD chưa tồn tại
    - File PDF mới hơn file MD (đã được cập nhật)
    """
    md_path = pdf_path.with_suffix('.md')
    
    # Nếu file MD chưa tồn tại -> cần convert
    if not md_path.exists():
        return True
    
    # So sánh thời gian chỉnh sửa
    pdf_mtime = pdf_path.stat().st_mtime
    md_mtime = md_path.stat().st_mtime
    
    # Nếu PDF mới hơn MD -> cần convert lại
    if pdf_mtime > md_mtime:
        return True
    
    return False

def convert_pdf_to_markdown(pdf_path):
    """Chuyển đổi một file PDF sang Markdown"""
    try:
        print(f"📄 Converting: {pdf_path}")
        
        # Chuyển đổi PDF sang Markdown với các tùy chọn tối ưu
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path), 
            page_chunks=False,  # Không chia nhỏ theo trang
            write_images=False  # Không trích xuất ảnh (tăng tốc độ)
        )
        
        # Tạo đường dẫn output
        md_path = pdf_path.with_suffix('.md')
        
        # Ghi file Markdown
        md_path.write_text(md_text, encoding='utf-8')
        
        print(f"✅ Converted: {md_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🚀 PDF to Markdown Converter - Smart Mode")
    print("=" * 60)
    
    # Tìm tất cả file PDF
    all_pdf_files = list(Path('.').glob('**/*.pdf'))
    pdf_files = [f for f in all_pdf_files if '.git' not in f.parts]
    
    if not pdf_files:
        print("⚠️  No PDF files found in repository")
        sys.exit(0)
    
    print(f"
📊 Scanning {len(pdf_files)} PDF file(s)...
")
    
    # Phân loại files
    to_convert = []
    skipped = []
    
    for pdf_file in pdf_files:
        if should_convert(pdf_file):
            to_convert.append(pdf_file)
        else:
            skipped.append(pdf_file)
    
    # Báo cáo
    print("📋 Conversion Plan:")
    print(f"   🔄 To convert: {len(to_convert)}")
    print(f"   ⏭️  To skip: {len(skipped)}")
    print()
    
    if skipped:
        print("⏭️  Skipped files (already converted & up-to-date):")
        for f in skipped:
            md_path = f.with_suffix('.md')
            print(f"   • {f} → {md_path.name} ✓")
        print()
    
    if not to_convert:
        print("✨ All PDF files are already converted and up-to-date!")
        print("   No conversion needed.")
        sys.exit(0)
    
    print("🔄 Converting files:")
    print("-" * 60)
    
    # Chuyển đổi
    success_count = 0
    failed_count = 0
    
    for i, pdf_file in enumerate(to_convert, 1):
        print(f"
[{i}/{len(to_convert)}]", end=" ")
        if convert_pdf_to_markdown(pdf_file):
            success_count += 1
        else:
            failed_count += 1
    
    # Tổng kết
    print("
" + "=" * 60)
    print("✨ Conversion Summary")
    print("=" * 60)
    print(f"Total PDFs found:     {len(pdf_files)}")
    print(f"Skipped (up-to-date): {len(skipped)}")
    print(f"Converted:            {success_count}")
    print(f"Failed:               {failed_count}")
    print("=" * 60)
    
    # Exit với code 1 nếu có lỗi
    if failed_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()