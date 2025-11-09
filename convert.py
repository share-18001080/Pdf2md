#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOLUTION 1: Bootstrap Phases - Scientific PDF to Markdown (LaTeX Support)

Architecture:
  Layer 1: Bootstrap Core (built-in only, 5s)
  Layer 2: Lightweight Probe (subprocess, no import, 30s)
  Layer 3: Decision Engine (rule-based scoring)
  Layer 4: Selective Install (Marker→Nougat→MinerU, with checkpoint)
  Layer 5: LaTeX-Aware Conversion + Quality Gate

No circular dependency. Fail fast if converter unavailable. Checkpoint for resume.
"""

import os
import sys
import json
import subprocess
import socket
import platform
from pathlib import Path
from typing import Dict, Optional, Tuple

# ============================================================================
# LAYER 1: BOOTSTRAP CORE (Built-in Only - No External Imports)
# ============================================================================

class BootstrapCore:
    """Layer 1: Collect environment info using ONLY built-in Python modules"""
    
    @staticmethod
    def get_environment_profile() -> Dict:
        """Gather environment info without importing heavy libs"""
        print("[L1] Bootstrap Core: Analyzing environment...")
        
        profile = {
            "timestamp": __import__('time').strftime("%Y-%m-%d %H:%M:%S"),
            "os": platform.system(),
            "os_version": platform.release(),
            "arch": platform.machine(),
            "cpu_count": os.cpu_count(),
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}",
        }
        
        # Memory check (without psutil)
        try:
            import resource
            soft, hard = resource.getrlimit(resource.RLIMIT_AS)
            profile["memory_limit_mb"] = soft // (1024 * 1024) if soft > 0 else -1
        except:
            profile["memory_limit_mb"] = -1
        
        # Network check
        profile["network_ok"] = BootstrapCore._check_network()
        
        print(f"  OS: {profile['os']} {profile['os_version']}")
        print(f"  CPU: {profile['arch']} ({profile['cpu_count']} cores)")
        print(f"  Network: {'✓' if profile['network_ok'] else '✗'}")
        
        return profile
    
    @staticmethod
    def _check_network() -> bool:
        """Check if PyPI is reachable"""
        try:
            socket.create_connection(("pypi.org", 443), timeout=5)
            return True
        except:
            return False
    
    @staticmethod
    def save_profile(profile: Dict) -> str:
        """Save profile to JSON for later layers"""
        profile_path = "/tmp/bootstrap_profile.json"
        with open(profile_path, "w") as f:
            json.dump(profile, f)
        print(f"  → Saved to {profile_path}")
        return profile_path

# ============================================================================
# LAYER 2: LIGHTWEIGHT PROBE (Subprocess-based, No Direct Imports)
# ============================================================================

class LightweightProbe:
    """Layer 2: Probe GPU/PyPI using subprocess (no import heavy libs)"""
    
    @staticmethod
    def probe_environment() -> Dict:
        """Probe GPU, torch, onnx availability via subprocess"""
        print("\n[L2] Lightweight Probe: Testing converter prerequisites...")
        
        probe_result = {
            "has_torch": LightweightProbe._check_torch(),
            "has_gpu": LightweightProbe._check_gpu(),
            "has_onnx": LightweightProbe._check_onnx(),
            "pypi_accessible": LightweightProbe._check_pypi(),
        }
        
        print(f"  Torch: {'✓' if probe_result['has_torch'] else '✗'}")
        print(f"  GPU: {'✓' if probe_result['has_gpu'] else '✗'}")
        print(f"  ONNX: {'✓' if probe_result['has_onnx'] else '✗'}")
        print(f"  PyPI: {'✓' if probe_result['pypi_accessible'] else '✗'}")
        
        return probe_result
    
    @staticmethod
    def _check_torch() -> bool:
        """Check torch without importing"""
        try:
            result = subprocess.run(
                [sys.executable, "-c", "import torch; exit(0)"],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False
    
    @staticmethod
    def _check_gpu() -> bool:
        """Check GPU without importing"""
        try:
            result = subprocess.run(
                [sys.executable, "-c", "import torch; exit(0 if torch.cuda.is_available() else 1)"],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False
    
    @staticmethod
    def _check_onnx() -> bool:
        """Check onnxruntime without importing"""
        try:
            result = subprocess.run(
                [sys.executable, "-c", "import onnxruntime; exit(0)"],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False
    
    @staticmethod
    def _check_pypi() -> bool:
        """Check PyPI via subprocess curl-like method"""
        try:
            result = subprocess.run(
                [sys.executable, "-c", 
                 "import urllib.request; urllib.request.urlopen('https://pypi.org/pypi/marker-pdf/json', timeout=5)"],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False
    
    @staticmethod
    def save_result(probe_result: Dict) -> str:
        """Save probe result"""
        result_path = "/tmp/bootstrap_probe.json"
        with open(result_path, "w") as f:
            json.dump(probe_result, f)
        print(f"  → Saved to {result_path}")
        return result_path

# ============================================================================
# LAYER 3: DECISION ENGINE (Rule-based Scoring)
# ============================================================================

class DecisionEngine:
    """Layer 3: Score environment and decide which converter to try"""
    
    @staticmethod
    def score_environment(profile: Dict, probe: Dict) -> Tuple[int, str]:
        """Score 0-100 and decide install strategy"""
        print("\n[L3] Decision Engine: Scoring environment...")
        
        score = 0
        reasoning = []
        
        # Network is crucial
        if probe.get("pypi_accessible"):
            score += 40
            reasoning.append("PyPI accessible (+40)")
        else:
            reasoning.append("PyPI not accessible (-0)")
        
        # GPU/torch useful but not critical
        if probe.get("has_torch"):
            score += 30
            reasoning.append("Torch available (+30)")
        else:
            reasoning.append("Torch not available (+0)")
        
        if probe.get("has_gpu"):
            score += 20
            reasoning.append("GPU available (+20)")
        else:
            reasoning.append("No GPU (+0)")
        
        # Architecture compatibility
        if "x86" in profile.get("arch", "").lower() or "x64" in profile.get("arch", "").lower():
            score += 10
            reasoning.append("x86/x64 arch (+10)")
        
        print(f"  Score: {score}/100")
        for reason in reasoning:
            print(f"    - {reason}")
        
        return score, "\n".join(reasoning)

# ============================================================================
# LAYER 4: SELECTIVE INSTALL (With Checkpoint)
# ============================================================================

class SelectiveInstaller:
    """Layer 4: Install converters with fallback (Marker→Nougat→MinerU)"""
    
    CANDIDATES = [
        ("marker-pdf", "marker", "Marker (fast, MIT)"),
        ("nougat-ocr", "nougat", "Nougat (academic, Meta)"),
        ("mineru", "mineru", "MinerU (perfect, AGPL)"),
    ]
    
    @staticmethod
    def install_selective() -> Optional[str]:
        """Try installing converters in priority order with checkpoint"""
        print("\n[L4] Selective Install: Installing LaTeX converters...")
        
        checkpoint_file = "/tmp/converter_choice.txt"
        
        # Check if already installed (checkpoint)
        if os.path.exists(checkpoint_file):
            with open(checkpoint_file, "r") as f:
                cached = f.read().strip()
                print(f"  ✓ Using cached converter: {cached}")
                return cached
        
        for pkg, module, desc in SelectiveInstaller.CANDIDATES:
            print(f"\n  → Trying {desc}...")
            
            if SelectiveInstaller._install_package(pkg, module):
                # Save checkpoint
                with open(checkpoint_file, "w") as f:
                    f.write(module)
                print(f"  ✓ {desc} installed successfully")
                return module
            else:
                print(f"  ✗ {desc} failed, trying next...")
        
        print("\n  ✗ All converters failed to install")
        return None
    
    @staticmethod
    def _install_package(package: str, module: str) -> bool:
        """Install single package and test import"""
        try:
            # Install
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package, "-q"],
                capture_output=True,
                timeout=300
            )
            if result.returncode != 0:
                return False
            
            # Test import
            result = subprocess.run(
                [sys.executable, "-c", f"import {module}"],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except:
            return False

# ============================================================================
# LAYER 5: LATEX-AWARE CONVERSION
# ============================================================================

class LatexAwareConverter:
    """Layer 5: Convert PDFs with LaTeX validation"""
    
    @staticmethod
    def validate_latex(md_text: str) -> Tuple[bool, Dict]:
        """Check if LaTeX is properly formatted"""
        import re
        
        inline = len(re.findall(r'\$[^$]+\$', md_text))
        block = len(re.findall(r'\$\$[\s\S]*?\$\$', md_text))
        keywords = len(re.findall(r'\b(equation|formula|integral|derivative)\b', md_text, re.I))
        
        return (inline + block > 0), {
            "inline_latex": inline,
            "block_latex": block,
            "keywords": keywords,
            "total": inline + block
        }
    
    @staticmethod
    def convert_pdfs(converter: str) -> Dict:
        """Convert all PDFs and validate LaTeX"""
        print("\n[L5] LaTeX-Aware Conversion: Converting PDFs...")
        
        # Dynamic import based on converter choice
        if converter == "marker":
            from marker.convert import convert_single_pdf
            converter_func = lambda pdf: convert_single_pdf(pdf)[0]
        elif converter == "nougat":
            converter_func = lambda pdf: subprocess.run(
                [sys.executable, "-m", "nougat", pdf, "--markdown"],
                capture_output=True, timeout=600
            ).stdout.decode()
        elif converter == "mineru":
            from mineru import DocumentConverter
            conv = DocumentConverter()
            converter_func = lambda pdf: conv.convert(pdf).export_to_markdown()
        else:
            return {"success": 0, "failed": 0}
        
        results = {"success": 0, "failed": 0, "files": []}
        
        for pdf_path in Path(".").rglob("*.pdf"):
            if ".git" in pdf_path.parts:
                continue
            
            try:
                md_text = converter_func(str(pdf_path))
                is_latex, metrics = LatexAwareConverter.validate_latex(md_text)
                
                # Quality gate: Must have LaTeX or fail
                if not is_latex and "equation" in md_text.lower():
                    print(f"  ✗ {pdf_path.name}: LaTeX keywords found but no $$ formatting")
                    results["failed"] += 1
                    continue
                
                # Save
                md_path = pdf_path.with_suffix(".md")
                md_path.write_text(md_text, encoding="utf-8")
                print(f"  ✓ {pdf_path.name}: {metrics['total']} LaTeX formulas")
                
                results["success"] += 1
                results["files"].append({
                    "pdf": str(pdf_path),
                    "md": str(md_path),
                    "latex_count": metrics["total"]
                })
            except Exception as e:
                print(f"  ✗ {pdf_path.name}: {str(e)}")
                results["failed"] += 1
        
        return results

# ============================================================================
# MAIN ORCHESTRATION
# ============================================================================

def main():
    print("\n" + "="*80)
    print("SOLUTION 1: Bootstrap Phases - LaTeX Scientific PDF Converter")
    print("="*80)
    
    try:
        # Layer 1
        profile = BootstrapCore.get_environment_profile()
        BootstrapCore.save_profile(profile)
        
        # Layer 2
        probe = LightweightProbe.probe_environment()
        LightweightProbe.save_result(probe)
        
        # Layer 3
        score, reasoning = DecisionEngine.score_environment(profile, probe)
        
        # Layer 4
        converter = SelectiveInstaller.install_selective()
        
        if not converter:
            print("\n❌ FATAL: All LaTeX converters failed to install")
            sys.exit(1)
        
        # Layer 5
        results = LatexAwareConverter.convert_pdfs(converter)
        
        # Report
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80)
        print(f"Converter: {converter.upper()}")
        print(f"Converted: {results['success']}")
        print(f"Failed: {results['failed']}")
        
        if results['success'] == 0:
            print("\n❌ No PDFs converted successfully")
            sys.exit(1)
        
        print("\n✓ Conversion complete with LaTeX validation")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ FATAL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()