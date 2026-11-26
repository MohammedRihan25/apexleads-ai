#!/usr/bin/env python3
"""
ApexLeads AI — Master Command Center & Operations CLI
One-click harvesting, sample generation, deliverable export, and dashboard orchestration.
"""

import argparse
import asyncio
import http.server
import os
import socketserver
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
STOREFRONT_DIR = BASE_DIR / "storefront"
DELIVERABLES_DIR = BASE_DIR

def print_banner():
    print("""
    ============================================================
       ▲ ApexLeads.AI — Autonomous B2B Lead Infrastructure
       Asynchronous High-Ticket Pipeline & Lead Delivery
    ============================================================
    """)

def run_harvest(niche: str, location: str, count: int, only_verified: bool = True):
    """Executes the autonomous lead harvesting and DNS MX verification engine."""
    print(f"[*] Starting Autonomous Harvest for Niche: '{niche}' in Location: '{location}' (Target: {count} leads)...")
    try:
        from lead_engine import harvest_and_verify_pipeline
        leads, out_path = asyncio.run(harvest_and_verify_pipeline(niche, location, count))
        print(f"\n[✓ SUCCESS] Exported {len(leads)} verified leads to:")
        print(f"    --> {out_path}")
        print("\n[✓] Golden Guarantee Check: All delivered records checked against live mail servers.")
    except Exception as e:
        print(f"[!] Error during harvest: {e}")

def run_sample():
    """Generates the standard 15-lead free sample sheet used for client acquisition."""
    print("[*] Synthesizing 15-Lead High-Converting Sample Deliverable...")
    try:
        from lead_engine import harvest_and_verify_pipeline
        leads, out_path = asyncio.run(harvest_and_verify_pipeline("marketing agency", "United States", 15))
        sample_path = BASE_DIR / "sample_client_deliverable.csv"
        print(f"[✓] Sample sheet refreshed at: {sample_path}")
    except Exception as e:
        print(f"[!] Sample generation error: {e}")

def run_status():
    """Displays local deliverables, orders, and operational status."""
    print("\n--- ApexLeads AI Operational Status ---")
    csv_files = list(BASE_DIR.glob("*.csv"))
    print(f"Deliverables Ready in Workspace: {len(csv_files)}")
    for f in csv_files:
        print(f"  • {f.name} ({f.stat().st_size} bytes)")
    
    # Check storefront
    has_storefront = (STOREFRONT_DIR / "index.html").exists()
    print(f"B2B Storefront Landing Page: {'[READY]' if has_storefront else '[MISSING]'}")

def run_serve(port: int = 8080):
    """Launches local web server for the B2B Storefront."""
    os.chdir(STOREFRONT_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n[✓] ApexLeads AI Storefront is LIVE at: http://127.0.0.1:{port}")
        print("Press Ctrl+C to stop the preview server.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="ApexLeads AI Master Command Center")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Harvest command
    p_harvest = subparsers.add_parser("harvest", help="Harvest and verify leads for a client")
    p_harvest.add_argument("--niche", type=str, default="marketing", help="Target industry/niche")
    p_harvest.add_argument("--location", type=str, default="Austin", help="Target city/state/country")
    p_harvest.add_argument("--count", type=int, default=10, help="Number of leads to harvest")

    # Sample command
    subparsers.add_parser("sample", help="Generate 15-lead free sample for prospect outreach")

    # Status command
    subparsers.add_parser("status", help="Show workspace deliverables and pipeline status")

    # Serve command
    p_serve = subparsers.add_parser("serve", help="Preview the B2B storefront locally")
    p_serve.add_argument("--port", type=int, default=8080, help="Local preview port")

    args = parser.parse_args()

    if args.command == "harvest":
        run_harvest(args.niche, args.location, args.count)
    elif args.command == "sample":
        run_sample()
    elif args.command == "status":
        run_status()
    elif args.command == "serve":
        run_serve(args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
