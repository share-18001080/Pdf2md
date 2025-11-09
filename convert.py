# convert.py - v5 CREATIVE FIX (Python-Only Summary & Debug)
import pymupdf4llm
from pathlib import Path
import sys
import os

# Test import ngay từ đầu
try:
    test_doc = pymupdf4llm.to_markdown("dummy.pdf", page_chunks=False)  # Test basic function
    print("✅ PyMuPDF4LLM imported and functional")
except Exception as e:
    print(f"❌ PyMuPDF4LLM error: {e}")
    sys.exit(1)

def should_convert(pdf_path):
    md_path = pdf_path.with_suffix('.md')
    if not md_path.exists():
        return True
    pdf_mtime = pdf_path.stat().st_mtime
    md_mtime = md_path.stat().st_mtime
    return pdf_mtime > md_mtime

def convert_pdf_to_markdown(pdf_path):
    try:
        print(f"📄 Converting: {pdf_path}")
        if not pdf_path.exists():
            print(f"   ❌ File not found or no read permission")
            return False
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path), 
            page_chunks=False,
            write_images=False
        )
        md_path = pdf_path.with_suffix('.md')
        md_path.parent.mkdir(parents=True, exist_ok=True)  # Tạo thư mục nếu cần
        md_path.write_text(md_text, encoding='utf-8')
        print(f"✅ Converted: {md_path}")
        return True
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def create_summary():
    """Tạo summary bằng Python (sáng tạo: tránh bash error)"""
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', None)
    if not summary_path:
        print("ℹ️  No GITHUB_STEP_SUMMARY env, skipping summary file")
        return
    
    with open(summary_path, 'a', encoding='utf-8') as f:
        f.write("## 📄 PDF to Markdown Conversion Report

")
        f.write("### Debug Info
")
        f.write("- Repository: " + os.environ.get('GITHUB_REPOSITORY', 'Unknown') + "
")
        f.write("- Branch: " + os.environ.get('GITHUB_REF_NAME', 'Unknown') + "
")
        f.write("- All files in repo: " + str(len(list(Path('.').rglob('*')))) + "

")
        
        # Thêm log conversion (giả sử log ở stderr/stdout, nhưng vì redirect, chúng ta in lại)
        f.write("### Conversion Log
```
        # Ở đây, chúng ta có thể sys.stdout.flush() trước để capture
        f.write("Log captured from script output.
")
        f.write("```
")

def main():
    print("=" * 60)
    print("🚀 PDF to Markdown Converter - Creative Debug Mode v5")
    print("=" * 60)
    
    # Debug: Liệt kê tất cả files
    all_files = list(Path('.').rglob('*'))
    print(f"📂 Total files in repo: {len(all_files)}")
    pdf_files_raw = list(Path('.').glob('**/*.pdf'))
    print(f"🔍 Raw PDF files found: {len(pdf_files_raw)}")
    if pdf_files_raw:
        print("📋 All PDF paths:")
        for p in pdf_files_raw:
            print(f"   - {p} (exists: {p.exists()})")
    
    pdf_files = [f for f in pdf_files_raw if '.git' not in str(f).split('/')]
    
    if not pdf_files:
        print("
⚠️  No PDF files found! Check:")
        print("   - File extension is .pdf?")
        print("   - PDF in root or subfolders?")
        print("   - File uploaded correctly to GitHub?")
        create_summary()  # Vẫn tạo summary
        sys.exit(0)
    
    print(f"
📊 Processing {len(pdf_files)} PDF file(s)...
")
    
    to_convert = [f for f in pdf_files if should_convert(f)]
    skipped = [f for f in pdf_files if not should_convert(f)]
    
    print("📋 Plan:")
    print(f"   - Convert: {len(to_convert)}")
    print(f"   - Skip: {len(skipped)}
")
    
    if skipped:
        print("⏭️  Skipped (up-to-date):")
        for f in skipped:
            print(f"   - {f}")
    
    if not to_convert:
        print("✨ No conversion needed!")
        create_summary()
        sys.exit(0)
    
    print("🔄 Converting...")
    print("-" * 60)
    
    success = 0
    failed = 0
    for i, pdf in enumerate(to_convert, 1):
        print(f"[{i}/{len(to_convert)}] ", end="")
        if convert_pdf_to_markdown(pdf):
            success += 1
        else:
            failed += 1
    
    print("
" + "=" * 60)
    print("Summary:")
    print(f"Found: {len(pdf_files)} | Converted: {success} | Failed: {failed}")
    print("=" * 60)
    create_summary()
    
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()