#!/usr/bin/env python3
"""
PDF Generator for Claudia Checkpoint System Documentation

This script converts the HTML documentation to PDF format for easy distribution
and offline reading.

Requirements:
    pip install weasyprint

Usage:
    python generate_pdf.py
"""

import os
import sys
from pathlib import Path

def generate_pdf():
    """Generate PDF from HTML documentation."""
    try:
        import weasyprint
    except ImportError:
        print("Error: weasyprint is not installed.")
        print("Please install it with: pip install weasyprint")
        print("\nNote: On some systems you may need additional dependencies:")
        print("  Ubuntu/Debian: sudo apt-get install python3-dev python3-pip python3-cffi python3-brotli libffi-dev shared-mime-info libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0")
        print("  macOS: brew install python3 libffi pango")
        sys.exit(1)

    # Get the current directory
    current_dir = Path(__file__).parent
    html_file = current_dir / "claudia-checkpoint-system-documentation.html"
    pdf_file = current_dir / "claudia-checkpoint-system-documentation.pdf"

    if not html_file.exists():
        print(f"Error: HTML file not found at {html_file}")
        sys.exit(1)

    print(f"Converting {html_file.name} to PDF...")
    
    try:
        # Convert HTML to PDF
        weasyprint.HTML(filename=str(html_file)).write_pdf(str(pdf_file))
        print(f"✅ PDF generated successfully: {pdf_file}")
        print(f"📄 File size: {pdf_file.stat().st_size / 1024 / 1024:.2f} MB")
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        sys.exit(1)

def main():
    """Main function."""
    print("🚀 Claudia Checkpoint System Documentation - PDF Generator")
    print("=" * 60)
    generate_pdf()
    print("\n✨ Done! You can now share the PDF documentation.")

if __name__ == "__main__":
    main()