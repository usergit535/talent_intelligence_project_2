"""
main.py
Master System Orchestrator - Runs dynamic company discovery from 4 job networks
and loops each company through verification pipeline layers.
"""

import os
import sys
# Force Python to look inside the local workspace path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from playwright.sync_api import sync_playwright
from config.config import HEADLESS, PAGE_TIMEOUT, get_random_user_agent
from scraper.company_discovery import discover_companies
from scraper.hiring_checker import check_hiring
from scraper.social_media_finder import enrich_socials
from scraper.data_exporter import validate_and_deduplicate, export_excel, export_json
from scraper.logger import get_logger

log = get_logger("scraper.main")

def run_pipeline(seed_companies: list[dict]):
    """Iterates through dynamically scraped targets via Playwright page sessions."""
    log.info("🚀 Launching Master Talent Intelligence Processing Loop...")
    log.info(f"📋 Ingested {len(seed_companies)} target profiles from the ingestion pool.")

    raw_enriched_dataset = []

    with sync_playwright() as pw:
        selected_ua = get_random_user_agent()
        log.info(f"🌐 Spinning up Chromium Instance (Headless={HEADLESS})")
        
        browser = pw.chromium.launch(headless=HEADLESS)
        ctx = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=selected_ua
        )
        page = ctx.new_page()
        page.set_default_timeout(PAGE_TIMEOUT)

        for idx, company in enumerate(seed_companies, start=1):
            name = company.get("company_name", "Unknown Entity")
            log.info(f"🔄 [{idx}/{len(seed_companies)}] Processing Data Sweep -> '{name}'")
            
            working_record = dict(company)
            
            # --- Stage 1: Check Careers / Job Hiring Status ---
            try:
                working_record = check_hiring(working_record, page)
            except Exception as e:
                log.error(f"❌ Error during hiring status analysis for {name}: {e}")

            # --- Stage 2: Track Down Social Links & Profiles ---
            try:
                working_record = enrich_socials(working_record, page)
            except Exception as e:
                log.error(f"❌ Error during social link discovery for {name}: {e}")

            raw_enriched_dataset.append(working_record)
            log.info(f"✨ [{idx}/{len(seed_companies)}] Synchronized updates finalized for '{name}'")

        browser.close()
        log.info("🔒 Playwright orchestration workspace torn down cleanly.")

    # --- Stage 3: Clean, Deduplicate and Save to File System ---
    try:
        log.info("扫 Commencing post-processing data validation and consolidation...")
        cleaned_records = validate_and_deduplicate(raw_enriched_dataset)
        
        log.info("📊 Formatting corporate documentation models...")
        excel_out = export_excel(cleaned_records)
        json_out = export_json(cleaned_records)
        
        log.info("🎉 System Pipeline Processing Run Completed Successfully!")
    except Exception as e:
        log.critical(f"💥 Failed to complete output document compilation: {e}")


if __name__ == "__main__":
    try:
        # Dynamically crawl the 4 directory networks
        log.info("🔍 Initiating dynamic source discovery phase across 4 networks...")
        live_scraped_companies = discover_companies()
        
        # Verify if any companies were discovered before starting processing loop
        if live_scraped_companies:
            run_pipeline(live_scraped_companies)
        else:
            log.warning("⚠️ Dynamic sweep returned 0 results from live indices. Loop aborted.")
            
    except KeyboardInterrupt:
        log.warning("\n⚠️ Execution context killed via terminal signal. Exiting.")
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        sys.exit(1)