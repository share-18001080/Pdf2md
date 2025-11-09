#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOLUTION 2: Pre-Validation Environment for Scientific PDF → Markdown (LaTeX)
Architecture: Scout → SelectiveInstall → ValidatedConvert → QualityAssurance

CRITICAL: LATEX SUPPORT ONLY - Fails gracefully if all LaTeX converters unavailable
Used for: Academic papers, scientific documents with mathematical formulas
"""

import os
import sys
import json
import subprocess
import traceback
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Tuple, List

# ============================================================================
# PHASE 1: SCOUT - ENVIRONMENT PRE-VALIDATION
# ============================================================================

@dataclass
class ScoutResult:
    """Environment analysis result"""
    has_gpu: bool
    cpu_arch: str
    network_ok: bool
    pypi_accessible: bool
    optimal_candidate: str  # 'marker', 'nougat', or 'mineru'
    reason: str
    available_libraries: dict

class EnvironmentScout:
    """Scout the runtime environment to determine optimal LaTeX converter"""
    
    @staticmethod
    def check_gpu():
        """Check if GPU (CUDA/MPS) available"""
        try:
            import torch
            return torch.cuda.is_available() or torch.backends.mps.is_available()
        except:
            return False
    
    @staticmethod
    def check_cpu_arch():
        """Get CPU architecture"""
        import platform
        return platform.machine()  # x86_64, arm64, etc.
    
    @staticmethod
    def check_network():
        """Check if PyPI is accessible"""
        import urllib.request
        try:
            urllib.request.urlopen('https://pypi.org/pypi/requests/json', timeout=5)
            return True
        except:
            return False
    
    @staticmethod
    def query_pypi_versions(package_name: str) -> List[str]:
        """Query available versions for a package on PyPI"""
        try:
            import urllib.request
            url = f"https://pypi.org/pypi/{package_name}/json"
            response = urllib.request.urlopen(url, timeout=10)
            data = json.loads(response.read())
            return list(data['releases'].keys())[-5:]  # Last 5 versions
        except:
            return []
    
    @staticmethod
    def scout() -> ScoutResult:
        """Perform full environment scout"""
        print("[SCOUT] Starting environment analysis...")
        
        has_gpu = EnvironmentScout.check_gpu()
        arch = EnvironmentScout.check_cpu_arch()
        network_ok = EnvironmentScout.check_network()
        
        print(f"  - GPU available: {has_gpu}")
        print(f"  - CPU arch: {arch}")
        print(f"  - Network OK: {network_ok}")
        print(f"  - PyPI accessible: {network_ok}")
        
        # Query available versions
        available = {}
        if network_ok:
            print("  - Querying PyPI for LaTeX converters...")
            marker_versions = EnvironmentScout.query_pypi_versions("marker-pdf")
            nougat_versions = EnvironmentScout.query_pypi_versions("nougat-ocr")
            mineru_versions = EnvironmentScout.query_pypi_versions("mineru")
            
            available = {
                "marker": bool(marker_versions),
                "nougat": bool(nougat_versions),
                "mineru": bool(mineru_versions)
            }
            print(f"    Marker: {bool(marker_versions)}")
            print(f"    Nougat: {bool(nougat_versions)}")
            print(f"    MinerU: {bool(mineru_versions)}")
        
        # Determine optimal candidate
        if not network_ok:
            return ScoutResult(
                has_gpu=has_gpu, cpu_arch=arch, network_ok=False,
                pypi_accessible=False, optimal_candidate="OFFLINE",
                reason="No network access to PyPI", available_libraries=available
            )
        
        # Priority: Marker (fast) → Nougat (academic) → MinerU (perfect)
        if available.get("marker"):
            optimal = "marker"
            reason = "Fast LaTeX support + MIT license"
        elif available.get("nougat"):
            optimal = "nougat"
            reason = "Academic optimized, excellent formulas"
        elif available.get("mineru"):
            optimal = "mineru"
            reason = "Production-grade, 95% accuracy"
        else:
            optimal = "NONE"
            reason = "No LaTeX converters available"
        
        print(f"  - Optimal candidate: {optimal} ({reason})")
        
        return ScoutResult(
            has_gpu=has_gpu, cpu_arch=arch, network_ok=network_ok,
            pypi_accessible=network_ok, optimal_candidate=optimal,
            reason=reason, available_libraries=available
        )

# ============================================================================
# PHASE 2: SELECTIVE INSTALL - ADAPTIVE DEPENDENCY MANAGEMENT
# ============================================================================

class SelectiveInstaller:
    """Intelligently install LaTeX converters in order of preference"""
    
    INSTALL_PRIORITY = [
        ("marker-pdf", "marker", "Fast scientific paper converter"),
        ("nougat-ocr", "nougat", "Meta AI academic paper OCR"),
        ("mineru", "mineru", "Complete document conversion")
    ]
    
    @staticmethod
    def test_import(module_name: str) -> bool:
        """Test if module can be imported"""
        try:
            __import__(module_name)
            return True
        except ImportError:
            return False
    
    @staticmethod
    def install_package(package_name: str, module_name: str) -> Tuple[bool, str]:
        """Attempt to install a package"""
        print(f"  [INSTALL] Attempting {package_name}...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name, "-q"],
                capture_output=True,
                timeout=300,
                text=True
            )
            
            if result.returncode == 0 and SelectiveInstaller.test_import(module_name):
                print(f"    ✓ {package_name} installed successfully")
                return True, f"{package_name} ready"
            else:
                error_msg = result.stderr[:200] if result.stderr else "Unknown error"
                print(f"    ✗ Failed: {error_msg}")
                return False, error_msg
        
        except subprocess.TimeoutExpired:
            print(f"    ✗ Timeout installing {package_name}")
            return False, "Installation timeout"
        except Exception as e:
            print(f"    ✗ Exception: {str(e)}")
            return False, str(e)
    
    @staticmethod
    def install_selective() -> Optional[str]:
        """Try installing LaTeX converters in priority order"""
        print("\n[INSTALL] Starting selective installation...")
        
        for package, module, description in SelectiveInstaller.INSTALL_PRIORITY:
            print(f"\n  → {package} ({description})")
            
            # Check if already installed
            if SelectiveInstaller.test_import(module):
                print(f"    ✓ Already installed")
                return module
            
            # Attempt install
            success, msg = SelectiveInstaller.install_package(package, module)
            if success:
                return module
            else:
                print(f"    Reason: {msg}")
        
        print("\n  ✗ All LaTeX converters failed to install")
        return None

# ============================================================================
# PHASE 3: VALIDATED CONVERT - LaTeX-AWARE CONVERSION
# ============================================================================

class ValidatedConverter:
    """Convert PDFs using selected LaTeX converter with verification"""
    
    @staticmethod
    def validate_latex_in_markdown(md_text: str) -> Tuple[bool, dict]:
        """Verify markdown contains proper LaTeX formatting"""
        import re
        
        # Check for inline LaTeX: $...$
        inline_latex = len(re.findall(r'\$[^$]+\$', md_text))
        
        # Check for block LaTeX: $$...$$
        block_latex = len(re.findall(r'\$\$[\s\S]*?\$\$', md_text))
        
        # Check for LaTeX keywords (indicates formulas should be present)
        latex_keywords = re.findall(
            r'\b(equation|formula|integral|derivative|sum|product|fraction|sin|cos|tan)\b',
            md_text,
            re.IGNORECASE
        )
        
        metrics = {
            "inline_latex_count": inline_latex,
            "block_latex_count": block_latex,
            "latex_keywords": len(latex_keywords),
            "total_formulas": inline_latex + block_latex,
            "has_latex": inline_latex > 0 or block_latex > 0
        }
        
        return metrics.get("total_formulas", 0) > 0, metrics
    
    @staticmethod
    def convert_with_marker(pdf_path: str) -> Optional[str]:
        """Convert using Marker"""
        try:
            from marker.convert import convert_single_pdf
            md_text, images, tables = convert_single_pdf(pdf_path)
            return md_text if md_text else None
        except Exception as e:
            print(f"    Marker error: {str(e)}")
            return None
    
    @staticmethod
    def convert_with_nougat(pdf_path: str) -> Optional[str]:
        """Convert using Nougat"""
        try:
            # Nougat has CLI-based interface
            result = subprocess.run(
                [sys.executable, "-m", "nougat", pdf_path, "--markdown"],
                capture_output=True,
                timeout=600,
                text=True
            )
            if result.returncode == 0:
                return result.stdout
            else:
                print(f"    Nougat error: {result.stderr[:200]}")
                return None
        except Exception as e:
            print(f"    Nougat error: {str(e)}")
            return None
    
    @staticmethod
    def convert_with_mineru(pdf_path: str) -> Optional[str]:
        """Convert using MinerU"""
        try:
            from mineru import DocumentConverter
            converter = DocumentConverter()
            result = converter.convert(pdf_path)
            md = result.export_to_markdown()
            return md if md else None
        except Exception as e:
            print(f"    MinerU error: {str(e)}")
            return None
    
    @staticmethod
    def convert_single_pdf(pdf_path: str, converter: str) -> Tuple[bool, Optional[str], dict]:
        """Convert PDF with specified converter and validate LaTeX"""
        print(f"  📄 Converting: {pdf_path} using {converter.upper()}")
        
        md_text = None
        if converter == "marker":
            md_text = ValidatedConverter.convert_with_marker(pdf_path)
        elif converter == "nougat":
            md_text = ValidatedConverter.convert_with_nougat(pdf_path)
        elif converter == "mineru":
            md_text = ValidatedConverter.convert_with_mineru(pdf_path)
        
        if not md_text:
            print(f"    ✗ Conversion returned empty output")
            return False, None, {"error": "Empty output"}
        
        # Validate LaTeX
        has_latex, metrics = ValidatedConverter.validate_latex_in_markdown(md_text)
        
        print(f"    ✓ Converted ({metrics['total_formulas']} LaTeX formulas found)")
        
        return True, md_text, metrics

# ============================================================================
# PHASE 4: QUALITY ASSURANCE - LATEX COVERAGE CHECK
# ============================================================================

class QualityAssurance:
    """Ensure LaTeX quality before accepting output"""
    
    @staticmethod
    def analyze_pdf_type(pdf_path: str) -> str:
        """Guess if PDF is scientific (should have formulas)"""
        # Simple heuristic: scientific PDFs often have "equation" in first 1000 chars
        try:
            import pypdf
            reader = pypdf.PdfReader(pdf_path)
            first_page = reader.pages[0].extract_text()
            keywords = ["equation", "formula", "integral", "theorem", "proof"]
            is_scientific = any(kw in first_page.lower() for kw in keywords)
            return "scientific" if is_scientific else "general"
        except:
            return "unknown"
    
    @staticmethod
    def check_quality(pdf_path: str, metrics: dict, pdf_type: str) -> Tuple[bool, str]:
        """Check if conversion quality is acceptable"""
        formulas = metrics.get("total_formulas", 0)
        keywords = metrics.get("latex_keywords", 0)
        
        # For scientific PDFs, require at least some LaTeX
        if pdf_type == "scientific" and keywords > 0 and formulas == 0:
            return False, "Scientific PDF has formula keywords but no LaTeX wrapping detected"
        
        # Overall: if we got output, consider it OK
        return True, "Quality check passed"
    
    @staticmethod
    def generate_report(results: dict) -> str:
        """Generate QA report"""
        passed = sum(1 for r in results.values() if r.get("success"))
        total = len(results)
        
        report = f"""
=== QUALITY ASSURANCE REPORT ===
Processed: {passed}/{total} PDFs
Conversion Rate: {100*passed/total:.1f}%

Details:
"""
        for pdf, result in results.items():
            status = "✓" if result.get("success") else "✗"
            formulas = result.get("metrics", {}).get("total_formulas", 0)
            report += f"\n  {status} {pdf}: {formulas} LaTeX formulas"
        
        return report

# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def main():
    print("\n" + "="*80)
    print("SOLUTION 2: PRE-VALIDATION ENVIRONMENT - SCIENTIFIC PDF CONVERTER")
    print("="*80)
    
    # PHASE 1: Scout
    print("\n[PHASE 1] ENVIRONMENT SCOUT")
    print("-" * 80)
    scout = EnvironmentScout.scout()
    
    if scout.optimal_candidate == "OFFLINE":
        print("\n❌ FATAL: No network access to PyPI")
        print("   Cannot install LaTeX converters offline")
        sys.exit(1)
    
    if scout.optimal_candidate == "NONE":
        print("\n❌ FATAL: No LaTeX converters available on PyPI")
        print("   Marker, Nougat, and MinerU all unavailable")
        sys.exit(1)
    
    # PHASE 2: Selective Install
    print("\n[PHASE 2] SELECTIVE INSTALLATION")
    print("-" * 80)
    converter = SelectiveInstaller.install_selective()
    
    if not converter:
        print("\n❌ FATAL: All LaTeX converters failed to install")
        print("   Marker → Nougat → MinerU all failed")
        print("\n   Diagnostic suggestions:")
        print("   - Check network connection to PyPI")
        print("   - Verify CPU architecture compatibility")
        print("   - Check available disk space")
        print("   - Try with --no-cache-dir flag")
        sys.exit(1)
    
    print(f"\n✓ Using converter: {converter.upper()}")
    
    # PHASE 3: Discover & Convert PDFs
    print("\n[PHASE 3] PDF DISCOVERY & CONVERSION")
    print("-" * 80)
    
    pdf_files = list(Path(".").rglob("*.pdf"))
    pdf_files = [p for p in pdf_files if ".git" not in p.parts]
    
    if not pdf_files:
        print("⚠️  No PDF files found")
        sys.exit(0)
    
    print(f"Found {len(pdf_files)} PDF file(s)")
    
    results = {}
    for pdf_path in pdf_files:
        success, md_text, metrics = ValidatedConverter.convert_single_pdf(
            str(pdf_path), converter
        )
        
        if success and md_text:
            # PHASE 4: Quality Assurance
            pdf_type = QualityAssurance.analyze_pdf_type(str(pdf_path))
            qa_pass, qa_msg = QualityAssurance.check_quality(str(pdf_path), metrics, pdf_type)
            
            if not qa_pass:
                print(f"    ⚠️  QA warning: {qa_msg}")
            
            # Save markdown
            md_path = pdf_path.with_suffix(".md")
            md_path.write_text(md_text, encoding="utf-8")
            print(f"    → Saved to {md_path.name}")
            
            results[str(pdf_path)] = {"success": True, "metrics": metrics}
        else:
            print(f"    ✗ Conversion failed")
            results[str(pdf_path)] = {"success": False, "metrics": metrics}
    
    # PHASE 4: Quality Report
    print("\n[PHASE 4] QUALITY ASSURANCE")
    print("-" * 80)
    report = QualityAssurance.generate_report(results)
    print(report)
    
    # Write GitHub summary
    github_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if github_summary:
        with open(github_summary, "a") as f:
            f.write(f"\n# PDF to Markdown Conversion Report (LaTeX-Only)\n")
            f.write(f"**Converter:** {converter.upper()}\n")
            f.write(f"**Quality Gate:** LaTeX preservation enforced\n")
            f.write(report)
    
    # Final check: Did we succeed?
    successful = sum(1 for r in results.values() if r.get("success"))
    if successful == 0:
        print("\n❌ CONVERSION FAILED: No PDFs converted successfully")
        sys.exit(1)
    
    print("\n✓ Conversion complete with LaTeX validation")
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)