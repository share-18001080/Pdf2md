# convert.py - v3 (Syntax Fixed)
import pymupdf4llm
from pathlib import Path
import sys

def should_convert(pdf_path):
    """Kiểm tra xem file PDF có cần được convert không."""
    md_path = pdf_path.with_suffix('.md')
    if not md_path.exists():
        return True
    
    pdf_mtime = pdf_path.stat().st_mtime
    md_mtime = md_path.stat().st_mtime
    
    if pdf_mtime > md_mtime:
        return True
    
    return False

def convert_pdf_to_markdown(pdf_path):
    """Chuyển đổi một file PDF sang Markdown."""
    try:
        print(f"📄 Converting: {pdf_path}")
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path), 
            page_chunks=False,
            write_images=False
        )
        md_path = pdf_path.with_suffix('.md')
        md_path.write_text(md_text, encoding='utf-8')
        print(f"✅ Converted: {md_path}")
        return True
    except Exception as e:
        print(f"❌ Error converting {pdf_path}: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🚀 PDF to Markdown Converter - Smart Mode v3")
    print("=" * 60)
    
    all_pdf_files = list(Path('.').glob('**/*.pdf'))
    pdf_files = [f for f in all_pdf_files if '.git' not in f.parts]
    
    if not pdf_files:
        print("
⚠️  No PDF files found in repository")
        sys.exit(0)
    
    print(f"
📊 Scanning {len(pdf_files)} PDF file(s)...
")
    
    to_convert = []
    skipped = []
    
    for pdf_file in pdf_files:
        if should_convert(pdf_file):
            to_convert.append(pdf_file)
        else:
            skipped.append(pdf_file)
            
    print("📋 Conversion Plan:")
    print(f"   - To convert: {len(to_convert)}")
    print(f"   - To skip:    {len(skipped)}
")
    
    if skipped:
        print("⏭️  Skipped files (already up-to-date):")
        for f in skipped:
            md_path = f.with_suffix('.md')
            # DÒNG 68 ĐÃ ĐƯỢC SỬA Ở ĐÂY
            print(f"   • {f} → {md_path.name} ✓")
        print()
    
    if not to_convert:
        print("✨ All PDF files are already converted and up-to-date!")
        print("   No conversion needed.")
        sys.exit(0)
    
    print("🔄 Converting files:")
    print("-" * 60)
    
    success_count = 0
    failed_count = 0
    
    for i, pdf_file in enumerate(to_convert, 1):
        print(f"
[{i}/{len(to_convert)}]", end=" ")
        if convert_pdf_to_markdown(pdf_file):
            success_count += 1
        else:
            failed_count += 1
            
    print("
" + "=" * 60)
    print("✨ Conversion Summary")
    print("=" * 60)
    print(f"Total PDFs found:     {len(pdf_files)}")
    print(f"Skipped (up-to-date): {len(skipped)}")
    print(f"Converted:            {success_count}")
    print(f"Failed:               {failed_count}")
    print("=" * 60)
    
    if failed_count > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()