#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF to Markdown Converter - MARKER VERSION with LaTeX Support
Optimized for academic papers & technical documents with formulas
"""
import os
import sys
import traceback
from pathlib import Path

try:
    from marker.convert import convert_single_pdf
except ImportError:
    print("ERROR: marker-pdf not installed. Run: pip install marker-pdf")
    sys.exit(1)

# ============================================================================
# PHASE 1: ENVIRONMENT & VALIDATION
# ============================================================================

def validate_environment():
    """Validate prerequisites"""
    print("[INIT] Validating environment...")
    
    # Check Python version
    py_version = sys.version_info
    if py_version.major < 3 or py_version.minor < 8:
        print(f"ERROR: Python 3.8+ required, got {py_version.major}.{py_version.minor}")
        return False
    
    # Check Marker
    try:
        from marker.convert import convert_single_pdf
        print("[OK] Marker is available")
    except ImportError as e:
        print(f"ERROR: Marker import failed: {e}")
        return False
    
    # Check write permissions
    if not os.access(".", os.W_OK):
        print("ERROR: No write permission in current directory")
        return False
    print("[OK] Write permissions OK")
    
    return True

# ============================================================================
# PHASE 2: FILE DISCOVERY & FILTERING
# ============================================================================

def discover_pdfs():
    """Find all PDF files recursively"""
    print("\n[DISCOVER] Scanning for PDF files...")
    
    all_pdfs = []
    excluded = []
    
    for pdf_path in Path(".").rglob("*.pdf"):
        # Skip .git and hidden directories
        parts = pdf_path.parts
        if any(part.startswith(".") for part in parts):
            excluded.append(pdf_path)
            continue
        
        all_pdfs.append(pdf_path)
    
    print(f"[FOUND] {len(all_pdfs)} PDF(s) to process")
    print(f"[SKIP] {len(excluded)} PDF(s) in hidden directories")
    
    return sorted(all_pdfs)

# ============================================================================
# PHASE 3: SMART FILTERING (SKIP ALREADY CONVERTED)
# ============================================================================

def should_convert(pdf_path):
    """Check if PDF needs conversion"""
    md_path = pdf_path.with_suffix(".md")
    
    if not md_path.exists():
        return True, "MD file missing"
    
    # Compare timestamps
    pdf_time = pdf_path.stat().st_mtime
    md_time = md_path.stat().st_mtime
    
    if pdf_time > md_time:
        return True, "PDF is newer than MD"
    
    return False, "Already up-to-date"

def filter_pdfs(pdf_list):
    """Filter PDF list into convert/skip"""
    to_convert = []
    to_skip = []
    
    for pdf in pdf_list:
        should, reason = should_convert(pdf)
        if should:
            to_convert.append((pdf, reason))
        else:
            to_skip.append((pdf, reason))
    
    return to_convert, to_skip

# ============================================================================
# PHASE 4: CONVERSION WITH MARKER (LaTeX Support)
# ============================================================================

def convert_single_pdf_marker(pdf_path):
    """Convert one PDF to Markdown using Marker"""
    try:
        print(f"📄 Converting: {pdf_path}")
        
        # Marker returns (markdown, images, tables)
        md_text, images, tables = convert_single_pdf(pdf_path)
        
        if not md_text:
            return False, "Empty markdown output"
        
        md_path = pdf_path.with_suffix(".md")
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_text, encoding="utf-8")
        
        # Log image count if extracted
        if images:
            print(f"      -> {md_path.name} [OK] ({len(images)} images extracted)")
        else:
            print(f"      -> {md_path.name} [OK]")
        
        return True, "OK"
        
    except Exception as e:
        return False, str(e)

def batch_convert(pdf_list):
    """Convert multiple PDFs"""
    results = {"success": 0, "failed": 0, "errors": []}
    
    for i, (pdf_path, _) in enumerate(pdf_list, 1):
        print(f"  [{i}/{len(pdf_list)}]", end=" ")
        
        success, msg = convert_single_pdf_marker(pdf_path)
        if success:
            results["success"] += 1
        else:
            print(f"      -> FAILED: {msg}")
            results["failed"] += 1
            results["errors"].append((str(pdf_path), msg))
    
    return results

# ============================================================================
# PHASE 5: GITHUB INTEGRATION
# ============================================================================

def write_github_summary(total, skipped, converted, failed):
    """Write summary to GitHub Actions"""
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    
    if not step_summary:
        print("[WARN] GITHUB_STEP_SUMMARY not set, skipping GitHub summary")
        return
    
    try:
        content = (
            "# PDF to Markdown Conversion Report (Marker)\n\n"
            "## LaTeX Support ✅\n\n"
            f"- Total PDFs: **{total}**\n"
            f"- Skipped: **{skipped}**\n"
            f"- Converted: **{converted}**\n"
            f"- Failed: **{failed}**\n\n"
            "**Note:** Marker properly wraps LaTeX formulas in `$$...$$` format.\n"
        )
        
        with open(step_summary, "a", encoding="utf-8") as f:
            f.write(content)
        
        print("[OK] GitHub summary written")
    except Exception as e:
        print(f"[WARN] Failed to write GitHub summary: {e}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("\n" + "="*70)
    print("PDF to MARKDOWN CONVERTER - MARKER v7 (LaTeX Support)")
    print("="*70)
    
    # Phase 1: Validate
    if not validate_environment():
        sys.exit(1)
    
    # Phase 2: Discover
    pdf_list = discover_pdfs()
    if not pdf_list:
        print("\n[WARN] No PDF files found")
        return 0
    
    # Phase 3: Filter
    print("\n[FILTER] Checking for up-to-date conversions...")
    to_convert, to_skip = filter_pdfs(pdf_list)
    
    print(f"  To convert: {len(to_convert)}")
    print(f"  To skip: {len(to_skip)}")
    
    if to_skip:
        print("\n[SKIP] Already up-to-date:")
        for pdf, reason in to_skip:
            print(f"  - {pdf}")
    
    if not to_convert:
        print("\n[OK] All PDFs already converted!")
        write_github_summary(len(pdf_list), len(to_skip), 0, 0)
        return 0
    
    # Phase 4: Convert with Marker
    print("\n[CONVERT] Starting conversion with Marker (LaTeX support)...")
    print("-" * 70)
    results = batch_convert(to_convert)
    
    # Phase 5: Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Total PDFs found:  {len(pdf_list)}")
    print(f"Skipped:           {len(to_skip)}")
    print(f"Converted:         {results['success']}")
    print(f"Failed:            {results['failed']}")
    print("="*70)
    
    if results["errors"]:
        print("\n[ERRORS]")
        for pdf, error in results["errors"]:
            print(f"  {pdf}: {error}")
    
    # Write GitHub summary
    write_github_summary(
        len(pdf_list),
        len(to_skip),
        results["success"],
        results["failed"]
    )
    
    # Exit code
    if results["failed"] > 0:
        sys.exit(1)
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\n[FATAL] Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)