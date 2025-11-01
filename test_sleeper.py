#!/usr/bin/env python3
"""
Test script for Sleeper API connectivity
"""

import requests

def test_sleeper_api():
    """Test basic Sleeper API connectivity"""
    print("Testing Sleeper API connectivity...")
    
    # Test NFL state endpoint
    try:
        response = requests.get("https://api.sleeper.app/v1/state/nfl")
        response.raise_for_status()
        nfl_state = response.json()
        print(f"✓ NFL State: Week {nfl_state['week']}, Season {nfl_state['season']}")
    except Exception as e:
        print(f"✗ NFL State test failed: {e}")
        return False
    
    # Test with a known public league (if available)
    print("\nAPI connectivity test passed!")
    print("\nTo test with your league:")
    print("1. Find your league ID from the Sleeper URL")
    print("2. Run: python sleeper_league_analyzer.py YOUR_LEAGUE_ID")
    
    return True

if __name__ == "__main__":
    test_sleeper_api()